#!/usr/bin/python
# -*- coding: utf-8 -*-

from ansible.module_utils.openshift_common import OpenShiftAnsibleModule, OpenShiftAnsibleException

DOCUMENTATION = '''
module: openshift_v1_template_list
short_description: OpenShift TemplateList
description:
- Retrieve a list of templates. List operations provide a snapshot read of the underlying
  objects, returning a resource_version representing a consistent version of the listed
  objects.
version_added: 2.3.0
author: OpenShift (@openshift)
options:
  api_key:
    description:
    - Token used to connect to the API.
  cert_file:
    description:
    - Path to a certificate used to authenticate with the API.
    type: path
  context:
    description:
    - The name of a context found in the Kubernetes config file.
  debug:
    description:
    - Enable debug output from the OpenShift helper. Logging info is written to KubeObjHelper.log
    default: false
    type: bool
  force:
    description:
    - If set to C(True), and I(state) is C(present), an existing object will updated,
      and lists will be replaced, rather than merged.
    default: false
    type: bool
  host:
    description:
    - Provide a URL for acessing the Kubernetes API.
  key_file:
    description:
    - Path to a key file used to authenticate with the API.
    type: path
  kubeconfig:
    description:
    - Path to an existing Kubernetes config file. If not provided, and no other connection
      options are provided, the openshift client will attempt to load the default
      configuration file from I(~/.kube/config.json).
    type: path
  password:
    description:
    - Provide a password for connecting to the API. Use in conjunction with I(username).
  resource_definition:
    description:
    - Provide the YAML definition for the object, bypassing any modules parameters
      intended to define object attributes.
    type: dict
  src:
    description:
    - Provide a path to a file containing the YAML definition of the object. Mutually
      exclusive with I(resource_definition).
    type: path
  ssl_ca_cert:
    description:
    - Path to a CA certificate used to authenticate with the API.
    type: path
  state:
    description:
    - Determines if an object should be created, patched, or deleted. When set to
      C(present), the object will be created, if it does not exist, or patched, if
      parameter values differ from the existing object's attributes, and deleted,
      if set to C(absent). A patch operation results in merging lists and updating
      dictionaries, with lists being merged into a unique set of values. If a list
      contains a dictionary with a I(name) or I(type) attribute, a strategic merge
      is performed, where individual elements with a matching I(name_) or I(type)
      are merged. To force the replacement of lists, set the I(force) option to C(True).
    default: present
    choices:
    - present
    - absent
  username:
    description:
    - Provide a username for connecting to the API.
  verify_ssl:
    description:
    - Whether or not to verify the API server's SSL certificates.
    type: bool
requirements:
- openshift == 0.4.0
'''

EXAMPLES = '''
'''

RETURN = '''
api_version:
  description: Requested API version
  type: string
template_list:
  type: complex
  returned: when I(state) = C(present)
  contains:
    api_version:
      description:
      - APIVersion defines the versioned schema of this representation of an object.
        Servers should convert recognized schemas to the latest internal value, and
        may reject unrecognized values.
      type: str
    items:
      description:
      - Items is a list of templates
      type: list
      contains:
        api_version:
          description:
          - APIVersion defines the versioned schema of this representation of an object.
            Servers should convert recognized schemas to the latest internal value,
            and may reject unrecognized values.
          type: str
        kind:
          description:
          - Kind is a string value representing the REST resource this object represents.
            Servers may infer this from the endpoint the client submits requests to.
            Cannot be updated. In CamelCase.
          type: str
        labels:
          description:
          - labels is a optional set of labels that are applied to every object during
            the Template to Config transformation.
          type: complex
          contains: str, str
        message:
          description:
          - message is an optional instructional message that will be displayed when
            this template is instantiated. This field should inform the user how to
            utilize the newly created resources. Parameter substitution will be performed
            on the message before being displayed so that generated credentials and
            other parameters can be included in the output.
          type: str
        metadata:
          description:
          - Standard object's metadata.
          type: complex
        objects:
          description:
          - objects is an array of resources to include in this template. If a namespace
            value is hardcoded in the object, it will be removed during template instantiation,
            however if the namespace value is, or contains, a ${PARAMETER_REFERENCE},
            the resolved value after parameter substitution will be respected and
            the object will be created in that namespace.
          type: list
          contains:
            raw:
              description:
              - Raw is the underlying serialization of this object.
              type: str
        parameters:
          description:
          - parameters is an optional array of Parameters used during the Template
            to Config transformation.
          type: list
          contains:
            from:
              description:
              - From is an input value for the generator. Optional.
              type: str
            description:
              description:
              - Description of a parameter. Optional.
              type: str
            display_name:
              description:
              - "Optional: The name that will show in UI instead of parameter 'Name'"
              type: str
            generate:
              description:
              - 'generate specifies the generator to be used to generate random string
                from an input value specified by From field. The result string is
                stored into Value field. If empty, no generator is being used, leaving
                the result Value untouched. Optional. The only supported generator
                is "expression", which accepts a "from" value in the form of a simple
                regular expression containing the range expression "[a-zA-Z0-9]",
                and the length expression "a{length}". Examples: from | value -----------------------------
                "test[0-9]{1}x" | "test7x" "[0-1]{8}" | "01001100" "0x[A-F0-9]{4}"
                | "0xB3AF" "[a-zA-Z0-9]{8}" | "hW4yQU5i"'
              type: str
            name:
              description:
              - Name must be set and it can be referenced in Template Items using
                ${PARAMETER_NAME}. Required.
              type: str
            required:
              description:
              - 'Optional: Indicates the parameter must have a value. Defaults to
                false.'
              type: bool
            value:
              description:
              - Value holds the Parameter data. If specified, the generator will be
                ignored. The value replaces all occurrences of the Parameter ${Name}
                expression during the Template to Config transformation. Optional.
              type: str
    kind:
      description:
      - Kind is a string value representing the REST resource this object represents.
        Servers may infer this from the endpoint the client submits requests to. Cannot
        be updated. In CamelCase.
      type: str
    metadata:
      description:
      - Standard object's metadata.
      type: complex
'''


def main():
    try:
        module = OpenShiftAnsibleModule('template_list', 'v1')
    except OpenShiftAnsibleException as exc:
        # The helper failed to init, so there is no module object. All we can do is raise the error.
        raise Exception(exc.message)

    try:
        module.execute_module()
    except OpenShiftAnsibleException as exc:
        module.fail_json(msg="Module failed!", error=str(exc))


if __name__ == '__main__':
    main()
