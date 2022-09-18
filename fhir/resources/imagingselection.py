# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/ImagingSelection
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""
import typing

from pydantic import Field, root_validator
from pydantic.error_wrappers import ErrorWrapper, ValidationError
from pydantic.errors import MissingError, NoneIsNotAllowedError

from . import backboneelement, domainresource, fhirtypes


class ImagingSelection(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A set of images produced in single study (one or more series of references
    images).
    Representation of the content produced in a DICOM imaging study. A study
    comprises a set of series, each of which includes a set of Service-Object
    Pair Instances (SOP Instances - images or other data) acquired or produced
    in a common context.  A series is of only one modality (e.g. X-ray, CT, MR,
    ultrasound), but a study may have multiple series of different modalities.
    """

    resource_type = Field("ImagingSelection", const=True)

    basedOn: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="basedOn",
        title="Request fulfilled",
        description=(
            "A list of the diagnostic requests that resulted in this imaging study "
            "being performed."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=[
            "CarePlan",
            "ServiceRequest",
            "Appointment",
            "AppointmentResponse",
            "Task",
        ],
    )

    bodySite: fhirtypes.CodeableConceptType = Field(
        None,
        alias="bodySite",
        title="Body part examined",
        description=(
            "The anatomic structures examined. See DICOM Part 16 Annex L (http://di"
            "com.nema.org/medical/dicom/current/output/chtml/part16/chapter_L.html)"
            " for DICOM to SNOMED-CT mappings. The bodySite may indicate the "
            "laterality of body part imaged; if so, it shall be consistent with any"
            " content of ImagingSelection.series.laterality."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    category: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="category",
        title="Imaging Selection purpose text or code",
        description=(
            "Imaging Selection purpose text or code."
        ),
        # if property is element of this resource.
        element_required=True,
        element_property=True,
    )

    code: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="code",
        title="Imaging Selection purpose text or code",
        description=(
            "Imaging Selection purpose text or code."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    code__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_code", title="Extension field for ``code``."
    )

    derivedFrom: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="derivedFrom",
        title="v",
        description=(
            "The imaging study from which the imaging selection is derived."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=[
            "ImagingStudy"
        ],
    )

    endpoint: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="endpoint",
        title="Study access endpoint",
        description=(
            "The network service providing access (e.g., query, view, or retrieval)"
            " for the study. See implementation notes for information about using "
            "DICOM endpoints. A study-level endpoint applies to each series in the "
            "study, unless overridden by a series-level endpoint with the same "
            "Endpoint.connectionType."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Endpoint"],
    )

    focus: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="focus",
        title=(
            "Related resource that is the focus for the imaging selection"
        ),
        description=(
            "Related resource that is the focus for the imaging selection."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=[
            "ImagingSelection"
        ],
    )

    frameOfReferenceUid: fhirtypes.Id = Field(
        None,
        alias="frameOfReferenceUid",
        title="The Frame of Reference UID for the selected images",
        description="The Frame of Reference UID for the selected images.",
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )

    identifier: typing.List[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="Identifiers for ImagingSelection",
        description=(
            "Identifiers for the ImagingSelection."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    imageRegion: typing.List[fhirtypes.ImagingSelectionImageRegionType] = Field(
        None,
        alias="imageRegion",
        title="A specific 3D region in a DICOM frame of reference",
        description=(
            "A specific 3D region in a DICOM frame of reference."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    instance: typing.List[fhirtypes.ImagingSelectionInstanceType] = Field(
        None,
        alias="instance",
        title="A single SOP instance from the series",
        description=(
            "A single SOP instance within the series, e.g. an image, or "
            "presentation state."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    issued: fhirtypes.Instant = Field(
        None,
        alias="issued",
        title="Date/Time this version was made available",
        description=(
            "The date and time this version of the observation was made available "
            "to providers, typically after the results have been reviewed and "
            "verified."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    performer: typing.List[fhirtypes.ImagingStudySeriesPerformerType] = Field(
        None,
        alias="performer",
        title="Who performed the series",
        description="Indicates who or what performed the series and how they were involved.",
        # if property is element of this resource.
        element_property=True,
    )

    seriesNumber: fhirtypes.UnsignedInt = Field(
        None,
        alias="seriesNumber",
        title="DICOM Series Number",
        description="DICOM Series Number.",
        # if property is element of this resource.
        element_property=True,
    )

    seriesUid: fhirtypes.Id = Field(
        None,
        alias="seriesUid",
        title="DICOM Series Instance UID",
        description="DICOM Series Instance UID.",
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )

    studyUid: fhirtypes.Id = Field(
        None,
        alias="studyUid",
        title="DICOM Study Instance UID",
        description="DICOM Study Instance UID.",
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )

    status: fhirtypes.Code = Field(
        None,
        alias="status",
        title="available | entered-in-error | unknown",
        description="The current state of the ImagingSelection.",
        # if property is element of this resource.
        element_property=True,
        element_required=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=[
            "available",
            "entered-in-error",
            "unknown",
        ],
    )
    subject: fhirtypes.ReferenceType = Field(
        ...,
        alias="subject",
        title="Who or what is the subject of the imaging selection",
        description="The subject, typically a patient, of the imaging study.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Patient", "Device", "Group"],
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ImagingSelection`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "meta",
            "implicitRules",
            "language",
            "text",
            "contained",
            "extension",
            "modifierExtension",
            "identifier",
            "status",
            "subject",
            "issued",
            "performer",
            "basedOn",
            "category",
            "code",
            "studyUid",
            "derivedFrom",
            "endpoint",
            "seriesUid",
            "seriesNumber",
            "frameOfReferenceUid",
            "bodySite",
            "focus",
            "instance",
            "imageRegion"
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_1431(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("code", "code__ext")]
        # required_fields = [("status", "code", "code__ext")]
        _missing = object()

        def _fallback():
            return ""

        errors: typing.List["ErrorWrapper"] = []
        for name, ext in required_fields:
            field = cls.__fields__[name]
            ext_field = cls.__fields__[ext]
            value = values.get(field.alias, _missing)
            if value not in (_missing, None):
                continue
            ext_value = values.get(ext_field.alias, _missing)
            missing_ext = True
            if ext_value not in (_missing, None):
                if isinstance(ext_value, dict):
                    missing_ext = len(ext_value.get("extension", [])) == 0
                elif (
                    getattr(ext_value.__class__, "get_resource_type", _fallback)()
                    == "FHIRPrimitiveExtension"
                ):
                    if ext_value.extension and len(ext_value.extension) > 0:
                        missing_ext = False
                else:
                    validate_pass = True
                    for validator in ext_field.type_.__get_validators__():
                        try:
                            ext_value = validator(v=ext_value)
                        except ValidationError as exc:
                            errors.append(ErrorWrapper(exc, loc=ext_field.alias))
                            validate_pass = False
                    if not validate_pass:
                        continue
                    if ext_value.extension and len(ext_value.extension) > 0:
                        missing_ext = False
            if missing_ext:
                if value is _missing:
                    errors.append(ErrorWrapper(MissingError(), loc=field.alias))
                else:
                    errors.append(
                        ErrorWrapper(NoneIsNotAllowedError(), loc=field.alias)
                    )
        if len(errors) > 0:
            raise ValidationError(errors, cls)  # type: ignore

        return values


class ImagingSelectionInstance(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A single SOP instance from the series.
    A single SOP instance within the series, e.g. an image, or presentation
    state.
    """

    resource_type = Field("ImagingSelectionInstance", const=True)

    imageRegion: typing.List[fhirtypes.ImagingSelectionInstanceImageRegionType] = Field(
        None,
        alias="imageRegion",
        title="A specific 2D region in a DICOM frame of reference",
        description=(
            "A specific 2D region in a DICOM frame of reference."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    number: fhirtypes.UnsignedInt = Field(
        None,
        alias="number",
        title="The number of this instance in the series",
        description="The number of instance in the series.",
        # if property is element of this resource.
        element_property=True,
    )

    subset: typing.List[fhirtypes.String] = Field(
        None,
        alias="subset",
        title="The selected subset of the SOP Instance",
        description=(
            "The selected subset of the SOP Instance."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    sopClass: fhirtypes.CodingType = Field(
        None,
        alias="sopClass",
        title="DICOM class type",
        description="DICOM instance  type.",
        # if property is element of this resource.
        element_property=True,
    )

    uid: fhirtypes.Id = Field(
        None,
        alias="uid",
        title="DICOM SOP Instance UID",
        description="The DICOM SOP Instance UID for this image or other DICOM content.",
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )

    uid__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_uid", title="Extension field for ``uid``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ImagingSelectionInstance`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "uid",
            "number",
            "sopClass",
            "subset",
            "imageRegion"
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_2851(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("uid", "uid__ext")]
        _missing = object()

        def _fallback():
            return ""

        errors: typing.List["ErrorWrapper"] = []
        for name, ext in required_fields:
            field = cls.__fields__[name]
            ext_field = cls.__fields__[ext]
            value = values.get(field.alias, _missing)
            if value not in (_missing, None):
                continue
            ext_value = values.get(ext_field.alias, _missing)
            missing_ext = True
            if ext_value not in (_missing, None):
                if isinstance(ext_value, dict):
                    missing_ext = len(ext_value.get("extension", [])) == 0
                elif (
                    getattr(ext_value.__class__, "get_resource_type", _fallback)()
                    == "FHIRPrimitiveExtension"
                ):
                    if ext_value.extension and len(ext_value.extension) > 0:
                        missing_ext = False
                else:
                    validate_pass = True
                    for validator in ext_field.type_.__get_validators__():
                        try:
                            ext_value = validator(v=ext_value)
                        except ValidationError as exc:
                            errors.append(ErrorWrapper(exc, loc=ext_field.alias))
                            validate_pass = False
                    if not validate_pass:
                        continue
                    if ext_value.extension and len(ext_value.extension) > 0:
                        missing_ext = False
            if missing_ext:
                if value is _missing:
                    errors.append(ErrorWrapper(MissingError(), loc=field.alias))
                else:
                    errors.append(
                        ErrorWrapper(NoneIsNotAllowedError(), loc=field.alias)
                    )
        if len(errors) > 0:
            raise ValidationError(errors, cls)  # type: ignore

        return values


class ImagingSelectionInstanceImageRegion(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A single SOP instance from the series.
    A single SOP instance within the series, e.g. an image, or presentation
    state.
    """

    resource_type = Field("ImagingSelectionInstanceImageRegion", const=True)

    coordinate: typing.List[fhirtypes.Decimal] = Field(
        None,
        alias="coordinate",
        title="Specifies the coordinates that define the image region",
        description=(
            "Specifies the coordinates that define the image region."
            "This repeating element order: The values are an ordered set of (x, y) coordinates."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    regionType: fhirtypes.Code = Field(
        None,
        alias="regionType",
        title="point | polyline | interpolated | circle | ellipse",
        description="point | polyline | interpolated | circle | ellipse.",
        # if property is element of this resource.
        element_property=True,
        element_required=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=[
            "point",
            "polyline",
            "interpolated",
            "circle",
            "ellipse"
        ],
    )

    regionType__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_regionType", title="Extension field for ``regionType``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ImagingSelectionInstanceImageRegion`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "regionType",
            "coordinate"
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_2851(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("regionType", "regionType__ext")]
        _missing = object()

        def _fallback():
            return ""

        errors: typing.List["ErrorWrapper"] = []
        for name, ext in required_fields:
            field = cls.__fields__[name]
            ext_field = cls.__fields__[ext]
            value = values.get(field.alias, _missing)
            if value not in (_missing, None):
                continue
            ext_value = values.get(ext_field.alias, _missing)
            missing_ext = True
            if ext_value not in (_missing, None):
                if isinstance(ext_value, dict):
                    missing_ext = len(ext_value.get("extension", [])) == 0
                elif (
                    getattr(ext_value.__class__, "get_resource_type", _fallback)()
                    == "FHIRPrimitiveExtension"
                ):
                    if ext_value.extension and len(ext_value.extension) > 0:
                        missing_ext = False
                else:
                    validate_pass = True
                    for validator in ext_field.type_.__get_validators__():
                        try:
                            ext_value = validator(v=ext_value)
                        except ValidationError as exc:
                            errors.append(ErrorWrapper(exc, loc=ext_field.alias))
                            validate_pass = False
                    if not validate_pass:
                        continue
                    if ext_value.extension and len(ext_value.extension) > 0:
                        missing_ext = False
            if missing_ext:
                if value is _missing:
                    errors.append(ErrorWrapper(MissingError(), loc=field.alias))
                else:
                    errors.append(
                        ErrorWrapper(NoneIsNotAllowedError(), loc=field.alias)
                    )
        if len(errors) > 0:
            raise ValidationError(errors, cls)  # type: ignore

        return values


class ImagingSelectionImageRegion(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A single SOP instance from the series.
    A single SOP instance within the series, e.g. an image, or presentation
    state.
    """

    resource_type = Field("ImagingSelectionImageRegion", const=True)

    coordinate: typing.List[fhirtypes.Decimal] = Field(
        None,
        alias="coordinate",
        title="Specifies the coordinates that define the image region",
        description=(
            "Specifies the coordinates that define the image region."
            "TThis repeating element order: The values are an ordered set of (x, y, z) coordinates."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    regionType: fhirtypes.Code = Field(
        None,
        alias="regionType",
        title="point | multipoint | polyline | polygon | ellipse | ellipsoid",
        description="point | multipoint | polyline | polygon | ellipse | ellipsoid.",
        # if property is element of this resource.
        element_property=True,
        element_required=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=[
            "point",
            "multipoint",
            "polyline",
            "interpolated",
            "circle",
            "ellipse"
        ],
    )

    regionType__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_regionType", title="Extension field for ``regionType``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ImagingSelectionImageRegion`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "regionType",
            "coordinate"
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_2851(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("regionType", "regionType__ext")]
        _missing = object()

        def _fallback():
            return ""

        errors: typing.List["ErrorWrapper"] = []
        for name, ext in required_fields:
            field = cls.__fields__[name]
            ext_field = cls.__fields__[ext]
            value = values.get(field.alias, _missing)
            if value not in (_missing, None):
                continue
            ext_value = values.get(ext_field.alias, _missing)
            missing_ext = True
            if ext_value not in (_missing, None):
                if isinstance(ext_value, dict):
                    missing_ext = len(ext_value.get("extension", [])) == 0
                elif (
                    getattr(ext_value.__class__, "get_resource_type", _fallback)()
                    == "FHIRPrimitiveExtension"
                ):
                    if ext_value.extension and len(ext_value.extension) > 0:
                        missing_ext = False
                else:
                    validate_pass = True
                    for validator in ext_field.type_.__get_validators__():
                        try:
                            ext_value = validator(v=ext_value)
                        except ValidationError as exc:
                            errors.append(ErrorWrapper(exc, loc=ext_field.alias))
                            validate_pass = False
                    if not validate_pass:
                        continue
                    if ext_value.extension and len(ext_value.extension) > 0:
                        missing_ext = False
            if missing_ext:
                if value is _missing:
                    errors.append(ErrorWrapper(MissingError(), loc=field.alias))
                else:
                    errors.append(
                        ErrorWrapper(NoneIsNotAllowedError(), loc=field.alias)
                    )
        if len(errors) > 0:
            raise ValidationError(errors, cls)  # type: ignore

        return values
