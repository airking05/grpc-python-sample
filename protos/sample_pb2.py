# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: sample.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='sample.proto',
  package='',
  syntax='proto3',
  serialized_pb=_b('\n\x0csample.proto\x1a\x1bgoogle/protobuf/empty.proto\"\x14\n\x04\x46uga\x12\x0c\n\x04hago\x18\x01 \x01(\t\"*\n\x04Ping\x12\x0c\n\x04hoge\x18\x01 \x01(\t\x12\x14\n\x05\x66ugas\x18\x02 \x03(\x0b\x32\x05.Fuga\"\x14\n\x04Pong\x12\x0c\n\x04hage\x18\x01 \x01(\t2`\n\x0cSampleServer\x12\x16\n\x04Test\x12\x05.Ping\x1a\x05.Pong\"\x00\x12\x38\n\x04\x44ing\x12\x16.google.protobuf.Empty\x1a\x16.google.protobuf.Empty\"\x00\x62\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,])




_FUGA = _descriptor.Descriptor(
  name='Fuga',
  full_name='Fuga',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='hago', full_name='Fuga.hago', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=45,
  serialized_end=65,
)


_PING = _descriptor.Descriptor(
  name='Ping',
  full_name='Ping',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='hoge', full_name='Ping.hoge', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fugas', full_name='Ping.fugas', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=67,
  serialized_end=109,
)


_PONG = _descriptor.Descriptor(
  name='Pong',
  full_name='Pong',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='hage', full_name='Pong.hage', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=111,
  serialized_end=131,
)

_PING.fields_by_name['fugas'].message_type = _FUGA
DESCRIPTOR.message_types_by_name['Fuga'] = _FUGA
DESCRIPTOR.message_types_by_name['Ping'] = _PING
DESCRIPTOR.message_types_by_name['Pong'] = _PONG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Fuga = _reflection.GeneratedProtocolMessageType('Fuga', (_message.Message,), dict(
  DESCRIPTOR = _FUGA,
  __module__ = 'sample_pb2'
  # @@protoc_insertion_point(class_scope:Fuga)
  ))
_sym_db.RegisterMessage(Fuga)

Ping = _reflection.GeneratedProtocolMessageType('Ping', (_message.Message,), dict(
  DESCRIPTOR = _PING,
  __module__ = 'sample_pb2'
  # @@protoc_insertion_point(class_scope:Ping)
  ))
_sym_db.RegisterMessage(Ping)

Pong = _reflection.GeneratedProtocolMessageType('Pong', (_message.Message,), dict(
  DESCRIPTOR = _PONG,
  __module__ = 'sample_pb2'
  # @@protoc_insertion_point(class_scope:Pong)
  ))
_sym_db.RegisterMessage(Pong)



_SAMPLESERVER = _descriptor.ServiceDescriptor(
  name='SampleServer',
  full_name='SampleServer',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=133,
  serialized_end=229,
  methods=[
  _descriptor.MethodDescriptor(
    name='Test',
    full_name='SampleServer.Test',
    index=0,
    containing_service=None,
    input_type=_PING,
    output_type=_PONG,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Ding',
    full_name='SampleServer.Ding',
    index=1,
    containing_service=None,
    input_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_SAMPLESERVER)

DESCRIPTOR.services_by_name['SampleServer'] = _SAMPLESERVER

# @@protoc_insertion_point(module_scope)
