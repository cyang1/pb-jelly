# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: rust/extensions.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import descriptor_pb2 as google_dot_protobuf_dot_descriptor__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='rust/extensions.proto',
  package='rust',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x15rust/extensions.proto\x12\x04rust\x1a google/protobuf/descriptor.proto:/\n\x06\x62ox_it\x12\x1d.google.protobuf.FieldOptions\x18\xd0\x86\x03 \x01(\x08:4\n\x0bgrpc_slices\x12\x1d.google.protobuf.FieldOptions\x18\xd3\x86\x03 \x01(\x08:-\n\x04type\x12\x1d.google.protobuf.FieldOptions\x18\xd4\x86\x03 \x01(\t:A\n\x19\x65rr_if_default_or_unknown\x12\x1c.google.protobuf.EnumOptions\x18\xd2\x86\x03 \x01(\x08:@\n\x15preserve_unrecognized\x12\x1f.google.protobuf.MessageOptions\x18\xd6\x86\x03 \x01(\x08:7\n\x08nullable\x12\x1d.google.protobuf.OneofOptions\x18\xd1\x86\x03 \x01(\x08:\x04true:;\n\x0cserde_derive\x12\x1c.google.protobuf.FileOptions\x18\xd5\x86\x03 \x01(\x08:\x05\x66\x61lse'
  ,
  dependencies=[google_dot_protobuf_dot_descriptor__pb2.DESCRIPTOR,])


BOX_IT_FIELD_NUMBER = 50000
box_it = _descriptor.FieldDescriptor(
  name='box_it', full_name='rust.box_it', index=0,
  number=50000, type=8, cpp_type=7, label=1,
  has_default_value=False, default_value=False,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key)
GRPC_SLICES_FIELD_NUMBER = 50003
grpc_slices = _descriptor.FieldDescriptor(
  name='grpc_slices', full_name='rust.grpc_slices', index=1,
  number=50003, type=8, cpp_type=7, label=1,
  has_default_value=False, default_value=False,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key)
TYPE_FIELD_NUMBER = 50004
type = _descriptor.FieldDescriptor(
  name='type', full_name='rust.type', index=2,
  number=50004, type=9, cpp_type=9, label=1,
  has_default_value=False, default_value=b"".decode('utf-8'),
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key)
ERR_IF_DEFAULT_OR_UNKNOWN_FIELD_NUMBER = 50002
err_if_default_or_unknown = _descriptor.FieldDescriptor(
  name='err_if_default_or_unknown', full_name='rust.err_if_default_or_unknown', index=3,
  number=50002, type=8, cpp_type=7, label=1,
  has_default_value=False, default_value=False,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key)
PRESERVE_UNRECOGNIZED_FIELD_NUMBER = 50006
preserve_unrecognized = _descriptor.FieldDescriptor(
  name='preserve_unrecognized', full_name='rust.preserve_unrecognized', index=4,
  number=50006, type=8, cpp_type=7, label=1,
  has_default_value=False, default_value=False,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key)
NULLABLE_FIELD_NUMBER = 50001
nullable = _descriptor.FieldDescriptor(
  name='nullable', full_name='rust.nullable', index=5,
  number=50001, type=8, cpp_type=7, label=1,
  has_default_value=True, default_value=True,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key)
SERDE_DERIVE_FIELD_NUMBER = 50005
serde_derive = _descriptor.FieldDescriptor(
  name='serde_derive', full_name='rust.serde_derive', index=6,
  number=50005, type=8, cpp_type=7, label=1,
  has_default_value=True, default_value=False,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key)

DESCRIPTOR.extensions_by_name['box_it'] = box_it
DESCRIPTOR.extensions_by_name['grpc_slices'] = grpc_slices
DESCRIPTOR.extensions_by_name['type'] = type
DESCRIPTOR.extensions_by_name['err_if_default_or_unknown'] = err_if_default_or_unknown
DESCRIPTOR.extensions_by_name['preserve_unrecognized'] = preserve_unrecognized
DESCRIPTOR.extensions_by_name['nullable'] = nullable
DESCRIPTOR.extensions_by_name['serde_derive'] = serde_derive
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

google_dot_protobuf_dot_descriptor__pb2.FieldOptions.RegisterExtension(box_it)
google_dot_protobuf_dot_descriptor__pb2.FieldOptions.RegisterExtension(grpc_slices)
google_dot_protobuf_dot_descriptor__pb2.FieldOptions.RegisterExtension(type)
google_dot_protobuf_dot_descriptor__pb2.EnumOptions.RegisterExtension(err_if_default_or_unknown)
google_dot_protobuf_dot_descriptor__pb2.MessageOptions.RegisterExtension(preserve_unrecognized)
google_dot_protobuf_dot_descriptor__pb2.OneofOptions.RegisterExtension(nullable)
google_dot_protobuf_dot_descriptor__pb2.FileOptions.RegisterExtension(serde_derive)

# @@protoc_insertion_point(module_scope)
