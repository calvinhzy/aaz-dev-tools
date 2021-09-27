from schematics.models import Model
from schematics.types import ListType, BaseType, DictType, ModelType, BooleanType, FloatType, IntType, StringType, PolyModelType
from .reference import ReferenceField, Linkable
from .fields import DataTypeFormatEnum, RegularExpressionField, XmsClientNameField, XmsExternalField, XmsDiscriminatorValueField, XmsClientFlattenField, XmsMutabilityField, XmsClientDefaultField, XNullableField, XmsAzureResourceField
from .xml import XML
from .external_documentation import ExternalDocumentation
from .x_ms_enum import XmsEnumField
from .fields import XmsSecretField, XAccessibilityField, XAzSearchDeprecatedField, XSfClientLibField, XApimCodeNillableField, XCommentField, XAbstractField, XClientNameField
from swagger.utils import exceptions

from command.model.configuration import CMDIntegerFormat, CMDStringFormat, CMDFloatFormat, CMDArrayFormat, CMDObjectFormat, CMDSchemaEnum, CMDSchemaEnumItem

from command.model.configuration import CMDSchemaDefault,\
    CMDStringSchema, CMDStringSchemaBase, \
    CMDByteSchema, CMDByteSchemaBase, \
    CMDBinarySchema, CMDBinarySchemaBase, \
    CMDDateSchema, CMDDateSchemaBase, \
    CMDDateTimeSchema, CMDDateTimeSchemaBase, \
    CMDPasswordSchema, CMDPasswordSchemaBase, \
    CMDDurationSchema, CMDDurationSchemaBase, \
    CMDUuidSchema, CMDUuidSchemaBase, \
    CMDIntegerSchema, CMDIntegerSchemaBase, \
    CMDInteger32Schema, CMDInteger32SchemaBase, \
    CMDInteger64Schema, CMDInteger64SchemaBase, \
    CMDBooleanSchema, CMDBooleanSchemaBase, \
    CMDFloatSchema, CMDFloatSchemaBase, \
    CMDFloat32Schema, CMDFloat32SchemaBase, \
    CMDFloat64Schema, CMDFloat64SchemaBase, \
    CMDObjectSchema, CMDObjectSchemaBase, CMDObjectSchemaDiscriminator, \
    CMDArraySchema, CMDArraySchemaBase, \
    CMDClsSchema, CMDClsSchemaBase


def _additional_properties_claim_function(_, data):
    if isinstance(data, bool):
        return bool
    elif isinstance(data, dict):
        return Schema
    else:
        return None


def _items_claim_function(_, data):
    if isinstance(data, dict):
        return Schema
    elif isinstance(data, list):
        return ListType(ModelType(Schema))
    else:
        return None


class Schema(Model, Linkable):
    """
    The Schema Object allows the definition of input and output data types. These types can be objects, but also primitives and arrays. This object is based on the JSON Schema Specification Draft 4 and uses a predefined subset of it. On top of this subset, there are extensions provided by this specification to allow for more complete documentation.
    Further information about the properties can be found in JSON Schema Core and JSON Schema Validation. Unless stated otherwise, the property definitions follow the JSON Schema specification as referenced here.
    """

    ref = ReferenceField()
    format = DataTypeFormatEnum()
    title = StringType()
    description = StringType()
    default = BaseType()

    # Validation keywords for numeric instances (number and integer)
    multiple_of = FloatType(
        min_value=0,
        serialized_name="multipleOf",
        deserialize_from="multipleOf"
    )
    maximum = FloatType()
    exclusive_maximum = BooleanType(
        serialized_name="exclusiveMaximum",
        deserialize_from="exclusiveMaximum",
    )
    minimum = FloatType()
    exclusive_minimum = BooleanType(
        serialized_name="exclusiveMinimum",
        deserialize_from="exclusiveMinimum"
    )

    # Validation keywords for strings
    max_length = IntType(
        min_value=0,
        serialized_name="maxLength",
        deserialize_from="maxLength"
    )
    min_length = IntType(
        min_value=0,
        serialized_name="minLength",
        deserialize_from="minLength"
    )
    pattern = RegularExpressionField()

    # Validation keywords for arrays
    items = PolyModelType(
        [ModelType("Schema"), ListType(ModelType("Schema"))],
        claim_function=_items_claim_function,
    )
    max_items = IntType(
        min_value=0,
        serialized_name="maxItems",
        deserialize_from="maxItems"
    )
    min_items = IntType(
        min_value=0,
        serialized_name="minItems",
        deserialize_from="minItems"
    )
    unique_items = BooleanType(
        serialized_name="uniqueItems",
        deserialize_from="uniqueItems"
    )

    # Validation keywords for objects
    max_properties = IntType(
        min_value=0,
        serialized_name="maxProperties",
        deserialize_from="maxProperties"
    )
    min_properties = IntType(
        min_value=0,
        serialized_name="minProperties",
        deserialize_from="minProperties"
    )
    required = ListType(StringType(), min_size=1)  # TODO:
    properties = DictType(
        ModelType("Schema"),
    )  # TODO:
    additional_properties = PolyModelType(
        [bool, ModelType("Schema")],
        claim_function=_additional_properties_claim_function,
        serialized_name="additionalProperties",
        deserialize_from="additionalProperties"
    )  # TODO:
    discriminator = StringType()  # Adds support for polymorphism. The discriminator is the schema property name that is used to differentiate between other schema that inherit this schema. The property name used MUST be defined at this schema and it MUST be in the required property list. When used, the value MUST be the name of this schema or any schema that inherits it.

    # Validation keywords for any instance type
    enum = ListType(BaseType())
    x_ms_enum = XmsEnumField()
    type = StringType(
        choices=["array", "boolean", "integer", "number", "object", "string"],  # https://datatracker.ietf.org/doc/html/draft-zyp-json-schema-04#section-3.5
    )
    all_of = ListType(
        ModelType("Schema"),
        serialized_name="allOf",
        deserialize_from="allOf"
    )  # TODO:

    read_only = BooleanType(
        serialized_name="readOnly",
        deserialize_from="readOnly"
    )  # TODO: # Relevant only for Schema "properties" definitions. Declares the property as "read only". This means that it MAY be sent as part of a response but MUST NOT be sent as part of the request. Properties marked as readOnly being true SHOULD NOT be in the required list of the defined schema. Default value is false.
    xml = ModelType(XML)  # TODO: # This MAY be used only on properties schemas. It has no effect on root schemas. Adds Additional metadata to describe the XML representation format of this property.
    external_docs = ModelType(
        ExternalDocumentation,
        serialized_name="externalDocs",
        deserialize_from="externalDocs"
    )  # TODO: # Additional external documentation for this schema.
    example = BaseType()  # TODO: # A free-form property to include an example of an instance for this schema.

    x_ms_client_name = XmsClientNameField()
    x_ms_external = XmsExternalField()
    x_ms_discriminator_value = XmsDiscriminatorValueField()
    x_ms_client_flatten = XmsClientFlattenField()
    x_ms_mutability = XmsMutabilityField()
    x_ms_client_default = XmsClientDefaultField()

    x_ms_azure_resource = XmsAzureResourceField() # indicates that the Definition Schema Object is a resource as defined by the Resource Manager API

    x_ms_secret = XmsSecretField()

    x_nullable = XNullableField()  # TODO: # when true, specifies that null is a valid value for the associated schema

    # specific properties
    _x_accessibility = XAccessibilityField()   # only used in ContainerRegistry Data plane
    _x_az_search_deprecated = XAzSearchDeprecatedField()  # only used in Search Data Plane
    _x_sf_clientlib = XSfClientLibField()  # only used in ServiceFabric Data Plane and ServiceFabricManagedClusters Mgmt Plane
    _x_apim_code_nillable = XApimCodeNillableField()  # only used in ApiManagement Mgmt Plane
    _x_comment = XCommentField()  # Only used in IoTCenter Mgmt Plane
    _x_abstract = XAbstractField()  # Only used in Logic Mgmt Plane and Web Mgmt Plane

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ref_instance = None
        self.disc_parent = None
        self.disc_children = {}

    @property
    def disc_instance(self):
        assert self.is_linked()
        if self.discriminator is not None:
            return self
        elif self.ref_instance is not None:
            return self.ref_instance.disc_instance
        return None

    def link(self, swagger_loader, *traces):
        if self.is_linked():
            return
        super().link(swagger_loader, *traces)

        if self.ref is not None:
            self.ref_instance, instance_traces = swagger_loader.load_ref(self.ref, *self.traces, 'ref')
            if isinstance(self.ref_instance, Linkable):
                self.ref_instance.link(swagger_loader, *instance_traces)

        if self.items is not None:
            if isinstance(self.items, list):
                for idx, item in enumerate(self.items):
                    item.link(swagger_loader, *self.traces, 'items', idx)
            else:
                self.items.link(swagger_loader, *self.traces, 'items')

        if self.properties is not None:
            for key, prop in self.properties.items():
                prop.link(swagger_loader, *self.traces, 'properties', key)

        if self.additional_properties is not None and isinstance(self.additional_properties, Schema):
            self.additional_properties.link(swagger_loader, *self.traces, 'additionalProperties')

        if self.all_of is not None:
            for idx, item in enumerate(self.all_of):
                item.link(swagger_loader, *self.traces, 'allOf', idx)

        self._link_disc()

    def _link_disc(self):
        if self.all_of is None:
            return
        for item in self.all_of:
            disc_parent = item.disc_instance
            if disc_parent is not None:
                if self.disc_parent is not None:
                    raise exceptions.InvalidSwaggerValueError(
                        msg="Multiple discriminator parents exists.",
                        key=self.traces, value=None
                    )
                self.disc_parent = disc_parent

                if self.x_ms_discriminator_value is not None:
                    disc_value = self.x_ms_discriminator_value
                elif len(self.traces) > 2 and self.traces[-2] == 'definitions':
                    disc_value = self.traces[-1]   # use the definition name as discriminator value
                else:
                    raise exceptions.InvalidSwaggerValueError(
                        msg="DiscriminatorValue is empty.",
                        key=self.traces, value=None
                    )
                if disc_value in self.disc_parent.disc_children:
                    raise exceptions.InvalidSwaggerValueError(
                        msg=f"Duplicated discriminator children for same value",
                        key=self.traces, value=disc_value
                    )
                self.disc_parent.disc_children[disc_value] = self

    def to_cmd_schema(self, traces, ref_link=None, in_base=False):
        if self in traces:
            assert isinstance(ref_link, str)
            schema_cls = f"@{ref_link.split('/')[-1]}"
            if in_base:
                model = CMDClsSchemaBase()
                model._type = schema_cls
            else:
                model = CMDClsSchema()
                model._type = schema_cls
            setattr(self, "_looped", True)
            if not hasattr(self, "_schema_cls"):
                setattr(self, "_schema_cls", schema_cls)
            else:
                assert self._schema_cls == schema_cls
            return model

        if self.ref_instance is not None:
            model = self.ref_instance.to_cmd_schema(traces=[*traces, self], ref_link=self.ref)
        elif self.type == "string":
            if self.format is None:
                if in_base:
                    model = CMDStringSchemaBase()
                else:
                    model = CMDStringSchema()
            elif self.format == "byte":
                if in_base:
                    model = CMDByteSchemaBase()
                else:
                    model = CMDByteSchema()
            elif self.format == "binary":
                if in_base:
                    model = CMDBinarySchemaBase()
                else:
                    model = CMDBinarySchema()
            elif self.format == "date":
                if in_base:
                    model = CMDDateSchemaBase()
                else:
                    model = CMDDateSchema()
            elif self.format == "date-time":
                if in_base:
                    model = CMDDateTimeSchemaBase()
                else:
                    model = CMDDateTimeSchema()
            elif self.format == "password":
                if in_base:
                    model = CMDPasswordSchemaBase()
                else:
                    model = CMDPasswordSchema()
            elif self.format == "duration":
                if in_base:
                    model = CMDDurationSchemaBase()
                else:
                    model = CMDDurationSchema()
            elif self.format == "uuid":
                if in_base:
                    model = CMDUuidSchemaBase()
                else:
                    model = CMDUuidSchema()
            else:
                raise exceptions.InvalidSwaggerValueError(
                    f"format is not supported", key=[self.type, self.format])
        elif self.type == "integer":
            if self.format is None:
                if in_base:
                    model = CMDIntegerSchemaBase()
                else:
                    model = CMDIntegerSchema()
            elif self.format == "int32":
                if in_base:
                    model = CMDInteger32SchemaBase()
                else:
                    model = CMDInteger32Schema()
            elif self.format == "int64":
                if in_base:
                    model = CMDInteger64SchemaBase()
                else:
                    model = CMDInteger64Schema()
            else:
                raise exceptions.InvalidSwaggerValueError(
                    f"format is not supported", key=[self.type, self.format])
        elif self.type == "boolean":
            if self.format is None:
                if in_base:
                    model = CMDBooleanSchemaBase()
                else:
                    model = CMDBooleanSchema()
            else:
                raise exceptions.InvalidSwaggerValueError(
                    f"format is not supported", key=[self.type, self.format])
        elif self.type == "number":
            if self.format is None:
                if in_base:
                    model = CMDFloatSchemaBase()
                else:
                    model = CMDFloatSchema()
            elif self.format == "float":
                if in_base:
                    model = CMDFloat32SchemaBase()
                else:
                    model = CMDFloat32Schema()
            elif self.format == "double":
                if in_base:
                    model = CMDFloat64SchemaBase()
                else:
                    model = CMDFloat64Schema()
            else:
                raise exceptions.InvalidSwaggerValueError(
                    f"format is not supported", key=[self.type, self.format])
        elif self.type == "array":
            if self.format is None:
                if in_base:
                    model = CMDArraySchemaBase()
                else:
                    model = CMDArraySchema()
            else:
                raise exceptions.InvalidSwaggerValueError(
                    f"format is not supported", key=[self.type, self.format])
        elif self.type == "object":
            if self.format is None:
                if in_base:
                    model = CMDObjectSchemaBase()
                else:
                    model = CMDObjectSchema()
            else:
                raise exceptions.InvalidSwaggerValueError(
                    f"format is not supported", key=[self.type, self.format])
        else:
            raise exceptions.InvalidSwaggerValueError(
                f"type is not supported", key=[self.type])

        if isinstance(model, CMDStringSchemaBase):
            model.fmt = self.build_cmd_string_format() or model.fmt
            model.enum = self.build_enum() or model.enum
        elif isinstance(model, CMDIntegerSchemaBase):
            model.fmt = self.build_cmd_integer_format() or model.fmt
            model.enum = self.build_enum() or model.enum
        elif isinstance(model, CMDBooleanSchemaBase):
            pass
        elif isinstance(model, CMDFloatSchemaBase):
            model.fmt = self.build_cmd_float_format() or model.fmt
            model.enum = self.build_enum() or model.enum
        elif isinstance(model, CMDArraySchemaBase):
            model.fmt = self.build_cmd_array_format() or model.fmt
            if self.items:
                assert isinstance(self.items, Schema)
                model.item = self.items.to_cmd_schema(traces=[*traces, self], in_base=True)
        elif isinstance(model, CMDObjectSchemaBase):
            model.fmt = self.build_cmd_object_format() or model.fmt

            prop_dict = {}
            for prop in model.props:
                prop_dict[prop.name] = prop

            if self.all_of:
                for item in self.all_of:
                    disc_parent = item.disc_instance
                    if disc_parent is not None and disc_parent in traces:
                        # if disc_parent already in trace, ignore
                        continue
                    v = item.to_cmd_schema(traces=[*traces, self], in_base=True)
                    for prop in v.props:
                        prop_dict[prop.name] = prop

            if self.properties:
                for name, p in self.properties:
                    assert isinstance(p, Schema)
                    prop = p.to_cmd_schema(traces=[*traces, self])
                    prop.name = name
                    prop_dict[name] = prop

            if self.required:
                for name in self.required:
                    prop_dict[name].required = True

            model.props = [*prop_dict.values()]

            if self.disc_children:
                model.discriminators = []
                assert self.discriminator is not None
                for disc_value, disc_child in self.disc_children:
                    disc = CMDObjectSchemaDiscriminator()
                    disc.prop = self.discriminator
                    disc.value = disc_value

                    v = disc_child.to_cmd_schema(traces=[*traces, self], in_base=True)
                    disc.props = [prop for prop in v.props if prop.name not in prop_dict]
                    disc.discriminators = v.discriminators
                    model.discriminators.append(disc)

            if getattr(self, "_looped", False):
                model.cls = self._schema_cls
                setattr(self, "_looped", False)

        if self.x_ms_client_default is not None:
            model.default = CMDSchemaDefault()
            model.default.value = self.x_ms_client_default

        elif self.default is not None:
            model.default = CMDSchemaDefault()
            model.default.value = self.default

        return model

    def build_cmd_string_format(self):
        assert self.type == "string"
        fmt_assigned = False

        fmt = CMDStringFormat()

        if self.pattern is not None:
            fmt.pattern = self.pattern
            fmt_assigned = True
        if self.max_length is not None:
            fmt.max_length = self.max_length
            fmt_assigned = True
        if self.min_length is not None:
            fmt.min_length = self.min_length
            fmt_assigned = True

        if not fmt_assigned:
            return None
        return fmt

    def build_cmd_integer_format(self):
        assert self.type == "integer"
        fmt_assigned = False
        fmt = CMDIntegerFormat()

        if self.maximum is not None:
            fmt.maximum = int(self.maximum)
            if self.exclusive_maximum and fmt.maximum == self.maximum:
                fmt.maximum -= 1
            fmt_assigned = True

        if self.minimum is not None:
            fmt.minimum = int(self.minimum)
            if self.exclusive_minimum and fmt.minimum == self.minimum:
                fmt.minimum += 1
            fmt_assigned = True

        if self.multiple_of is not None:
            fmt.multiple_of = self.multiple_of
            fmt_assigned = True

        if not fmt_assigned:
            return None
        return fmt

    def build_cmd_float_format(self):
        assert self.type == "number"
        fmt_assigned = False
        fmt = CMDFloatFormat()

        if self.maximum is not None:
            fmt.maximum = self.maximum
            if self.exclusive_maximum:
                fmt.exclusive_maximum = True
            fmt_assigned = True

        if self.minimum is not None:
            fmt.minimum = int(self.minimum)
            if self.exclusive_minimum:
                fmt.exclusive_minimum = True
            fmt_assigned = True

        if self.multiple_of is not None:
            fmt.multiple_of = self.multiple_of
            fmt_assigned = True

        if not fmt_assigned:
            return None
        return fmt

    def build_cmd_array_format(self):
        assert self.type == "array"
        fmt_assigned = False
        fmt = CMDArrayFormat()

        if self.unique_items:
            fmt.unique = True
            fmt_assigned = True

        if self.max_length is not None:
            fmt.max_length = self.max_length
            fmt_assigned = True

        if self.min_length is not None:
            fmt.min_length = self.min_length
            fmt_assigned = True

        if not fmt_assigned:
            return None
        return fmt

    def build_cmd_object_format(self):
        assert self.type == "object"
        fmt_assigned = False
        fmt = CMDObjectFormat()

        if self.max_properties is not None:
            fmt.max_properties = self.max_properties
            fmt_assigned = True
        if self.min_properties is not None:
            fmt.min_properties = self.min_properties
            fmt_assigned = True

        if not fmt_assigned:
            return None
        return fmt

    def build_enum(self):
        if not self.enum and not (self.x_ms_enum and self.x_ms_enum.values):
            return None
        enum = CMDSchemaEnum()
        enum.items = []
        if self.x_ms_enum and self.x_ms_enum.values:
            for v in self.x_ms_enum.values:
                item = CMDSchemaEnumItem()
                item.value = v.value
                if v.name:
                    # TODO: the name should be used as display name for argument
                    pass
                enum.items.append(item)
        elif self.enum:
            for v in self.enum:
                item = CMDSchemaEnumItem()
                item.value = v
                enum.items.append(item)
        return enum
