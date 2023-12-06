# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_command(
    "databricks workspace show",
    is_preview=True,
)
class Show(AAZCommand):
    """Show the workspace.

    :example: Show the workspace.
        az databricks workspace show --resource-group MyResourceGroup --name MyWorkspace
    """

    _aaz_info = {
        "version": "2018-04-01",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.databricks/workspaces/{}", "2018-04-01"],
        ]
    }

    def _handler(self, command_args):
        super()._handler(command_args)
        self._execute_operations()
        return self._output()

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )
        _args_schema.workspace_name = AAZStrArg(
            options=["--workspace-name", "--name", "-n"],
            help="The name of the workspace.",
            required=True,
            id_part="name",
            fmt=AAZStrArgFormat(
                max_length=64,
                min_length=3,
            ),
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.WorkspacesGet(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class WorkspacesGet(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200]:
                return self.on_200(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Databricks/workspaces/{workspaceName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "GET"

        @property
        def error_format(self):
            return "ODataV4Format"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
                **self.serialize_url_param(
                    "workspaceName", self.ctx.args.workspace_name,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2018-04-01",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        def on_200(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200
            )

        _schema_on_200 = None

        @classmethod
        def _build_schema_on_200(cls):
            if cls._schema_on_200 is not None:
                return cls._schema_on_200

            cls._schema_on_200 = AAZObjectType()

            _schema_on_200 = cls._schema_on_200
            _schema_on_200.id = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200.location = AAZStrType(
                flags={"required": True},
            )
            _schema_on_200.name = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200.properties = AAZObjectType(
                flags={"required": True, "client_flatten": True},
            )
            _schema_on_200.sku = AAZObjectType()
            _schema_on_200.tags = AAZDictType()
            _schema_on_200.type = AAZStrType(
                flags={"read_only": True},
            )

            properties = cls._schema_on_200.properties
            properties.authorizations = AAZListType()
            properties.created_by = AAZObjectType(
                serialized_name="createdBy",
            )
            _ShowHelper._build_schema_created_by_read(properties.created_by)
            properties.created_date_time = AAZStrType(
                serialized_name="createdDateTime",
                flags={"read_only": True},
            )
            properties.managed_resource_group_id = AAZStrType(
                serialized_name="managedResourceGroupId",
                flags={"required": True},
            )
            properties.parameters = AAZObjectType()
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )
            properties.storage_account_identity = AAZObjectType(
                serialized_name="storageAccountIdentity",
            )
            properties.ui_definition_uri = AAZStrType(
                serialized_name="uiDefinitionUri",
            )
            properties.updated_by = AAZObjectType(
                serialized_name="updatedBy",
            )
            _ShowHelper._build_schema_created_by_read(properties.updated_by)
            properties.workspace_id = AAZStrType(
                serialized_name="workspaceId",
                flags={"read_only": True},
            )
            properties.workspace_url = AAZStrType(
                serialized_name="workspaceUrl",
                flags={"read_only": True},
            )

            authorizations = cls._schema_on_200.properties.authorizations
            authorizations.Element = AAZObjectType()

            _element = cls._schema_on_200.properties.authorizations.Element
            _element.principal_id = AAZStrType(
                serialized_name="principalId",
                flags={"required": True},
            )
            _element.role_definition_id = AAZStrType(
                serialized_name="roleDefinitionId",
                flags={"required": True},
            )

            parameters = cls._schema_on_200.properties.parameters
            parameters.aml_workspace_id = AAZObjectType(
                serialized_name="amlWorkspaceId",
            )
            _ShowHelper._build_schema_workspace_custom_string_parameter_read(parameters.aml_workspace_id)
            parameters.custom_private_subnet_name = AAZObjectType(
                serialized_name="customPrivateSubnetName",
            )
            _ShowHelper._build_schema_workspace_custom_string_parameter_read(parameters.custom_private_subnet_name)
            parameters.custom_public_subnet_name = AAZObjectType(
                serialized_name="customPublicSubnetName",
            )
            _ShowHelper._build_schema_workspace_custom_string_parameter_read(parameters.custom_public_subnet_name)
            parameters.custom_virtual_network_id = AAZObjectType(
                serialized_name="customVirtualNetworkId",
            )
            _ShowHelper._build_schema_workspace_custom_string_parameter_read(parameters.custom_virtual_network_id)
            parameters.enable_no_public_ip = AAZObjectType(
                serialized_name="enableNoPublicIp",
            )
            _ShowHelper._build_schema_workspace_custom_boolean_parameter_read(parameters.enable_no_public_ip)
            parameters.encryption = AAZObjectType()
            parameters.load_balancer_backend_pool_name = AAZObjectType(
                serialized_name="loadBalancerBackendPoolName",
            )
            _ShowHelper._build_schema_workspace_custom_string_parameter_read(parameters.load_balancer_backend_pool_name)
            parameters.load_balancer_id = AAZObjectType(
                serialized_name="loadBalancerId",
            )
            _ShowHelper._build_schema_workspace_custom_string_parameter_read(parameters.load_balancer_id)
            parameters.nat_gateway_name = AAZObjectType(
                serialized_name="natGatewayName",
            )
            _ShowHelper._build_schema_workspace_custom_string_parameter_read(parameters.nat_gateway_name)
            parameters.prepare_encryption = AAZObjectType(
                serialized_name="prepareEncryption",
            )
            _ShowHelper._build_schema_workspace_custom_boolean_parameter_read(parameters.prepare_encryption)
            parameters.public_ip_name = AAZObjectType(
                serialized_name="publicIpName",
            )
            _ShowHelper._build_schema_workspace_custom_string_parameter_read(parameters.public_ip_name)
            parameters.require_infrastructure_encryption = AAZObjectType(
                serialized_name="requireInfrastructureEncryption",
            )
            _ShowHelper._build_schema_workspace_custom_boolean_parameter_read(parameters.require_infrastructure_encryption)
            parameters.resource_tags = AAZObjectType(
                serialized_name="resourceTags",
                flags={"read_only": True},
            )
            parameters.storage_account_name = AAZObjectType(
                serialized_name="storageAccountName",
            )
            _ShowHelper._build_schema_workspace_custom_string_parameter_read(parameters.storage_account_name)
            parameters.storage_account_sku_name = AAZObjectType(
                serialized_name="storageAccountSkuName",
            )
            _ShowHelper._build_schema_workspace_custom_string_parameter_read(parameters.storage_account_sku_name)
            parameters.vnet_address_prefix = AAZObjectType(
                serialized_name="vnetAddressPrefix",
            )
            _ShowHelper._build_schema_workspace_custom_string_parameter_read(parameters.vnet_address_prefix)

            encryption = cls._schema_on_200.properties.parameters.encryption
            encryption.type = AAZStrType(
                flags={"read_only": True},
            )
            encryption.value = AAZObjectType()

            value = cls._schema_on_200.properties.parameters.encryption.value
            value.key_name = AAZStrType(
                serialized_name="KeyName",
            )
            value.key_source = AAZStrType(
                serialized_name="keySource",
            )
            value.keyvaulturi = AAZStrType()
            value.keyversion = AAZStrType()

            resource_tags = cls._schema_on_200.properties.parameters.resource_tags
            resource_tags.type = AAZStrType(
                flags={"read_only": True},
            )
            resource_tags.value = AAZFreeFormDictType(
                flags={"required": True, "read_only": True},
            )

            storage_account_identity = cls._schema_on_200.properties.storage_account_identity
            storage_account_identity.principal_id = AAZStrType(
                serialized_name="principalId",
                flags={"read_only": True},
            )
            storage_account_identity.tenant_id = AAZStrType(
                serialized_name="tenantId",
                flags={"read_only": True},
            )
            storage_account_identity.type = AAZStrType(
                flags={"read_only": True},
            )

            sku = cls._schema_on_200.sku
            sku.name = AAZStrType(
                flags={"required": True},
            )
            sku.tier = AAZStrType()

            tags = cls._schema_on_200.tags
            tags.Element = AAZStrType()

            return cls._schema_on_200


class _ShowHelper:
    """Helper class for Show"""

    _schema_created_by_read = None

    @classmethod
    def _build_schema_created_by_read(cls, _schema):
        if cls._schema_created_by_read is not None:
            _schema.application_id = cls._schema_created_by_read.application_id
            _schema.oid = cls._schema_created_by_read.oid
            _schema.puid = cls._schema_created_by_read.puid
            return

        cls._schema_created_by_read = _schema_created_by_read = AAZObjectType()

        created_by_read = _schema_created_by_read
        created_by_read.application_id = AAZStrType(
            serialized_name="applicationId",
            flags={"read_only": True},
        )
        created_by_read.oid = AAZStrType(
            flags={"read_only": True},
        )
        created_by_read.puid = AAZStrType(
            flags={"read_only": True},
        )

        _schema.application_id = cls._schema_created_by_read.application_id
        _schema.oid = cls._schema_created_by_read.oid
        _schema.puid = cls._schema_created_by_read.puid

    _schema_workspace_custom_boolean_parameter_read = None

    @classmethod
    def _build_schema_workspace_custom_boolean_parameter_read(cls, _schema):
        if cls._schema_workspace_custom_boolean_parameter_read is not None:
            _schema.type = cls._schema_workspace_custom_boolean_parameter_read.type
            _schema.value = cls._schema_workspace_custom_boolean_parameter_read.value
            return

        cls._schema_workspace_custom_boolean_parameter_read = _schema_workspace_custom_boolean_parameter_read = AAZObjectType()

        workspace_custom_boolean_parameter_read = _schema_workspace_custom_boolean_parameter_read
        workspace_custom_boolean_parameter_read.type = AAZStrType(
            flags={"read_only": True},
        )
        workspace_custom_boolean_parameter_read.value = AAZBoolType(
            flags={"required": True},
        )

        _schema.type = cls._schema_workspace_custom_boolean_parameter_read.type
        _schema.value = cls._schema_workspace_custom_boolean_parameter_read.value

    _schema_workspace_custom_string_parameter_read = None

    @classmethod
    def _build_schema_workspace_custom_string_parameter_read(cls, _schema):
        if cls._schema_workspace_custom_string_parameter_read is not None:
            _schema.type = cls._schema_workspace_custom_string_parameter_read.type
            _schema.value = cls._schema_workspace_custom_string_parameter_read.value
            return

        cls._schema_workspace_custom_string_parameter_read = _schema_workspace_custom_string_parameter_read = AAZObjectType()

        workspace_custom_string_parameter_read = _schema_workspace_custom_string_parameter_read
        workspace_custom_string_parameter_read.type = AAZStrType(
            flags={"read_only": True},
        )
        workspace_custom_string_parameter_read.value = AAZStrType(
            flags={"required": True},
        )

        _schema.type = cls._schema_workspace_custom_string_parameter_read.type
        _schema.value = cls._schema_workspace_custom_string_parameter_read.value


__all__ = ["Show"]
