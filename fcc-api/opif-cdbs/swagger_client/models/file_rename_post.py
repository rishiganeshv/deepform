# coding: utf-8

"""
    OPIF Service Data API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 0.9.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class FileRenamePost(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'file_id': 'str',
        'file_name': 'str',
        'entity_id': 'str',
        'service_code': 'str'
    }

    attribute_map = {
        'file_id': 'fileId',
        'file_name': 'fileName',
        'entity_id': 'entityId',
        'service_code': 'serviceCode'
    }

    def __init__(self, file_id=None, file_name=None, entity_id=None, service_code=None):  # noqa: E501
        """FileRenamePost - a model defined in Swagger"""  # noqa: E501
        self._file_id = None
        self._file_name = None
        self._entity_id = None
        self._service_code = None
        self.discriminator = None
        if file_id is not None:
            self.file_id = file_id
        if file_name is not None:
            self.file_name = file_name
        if entity_id is not None:
            self.entity_id = entity_id
        if service_code is not None:
            self.service_code = service_code

    @property
    def file_id(self):
        """Gets the file_id of this FileRenamePost.  # noqa: E501

        Unique Id of the file.  # noqa: E501

        :return: The file_id of this FileRenamePost.  # noqa: E501
        :rtype: str
        """
        return self._file_id

    @file_id.setter
    def file_id(self, file_id):
        """Sets the file_id of this FileRenamePost.

        Unique Id of the file.  # noqa: E501

        :param file_id: The file_id of this FileRenamePost.  # noqa: E501
        :type: str
        """

        self._file_id = file_id

    @property
    def file_name(self):
        """Gets the file_name of this FileRenamePost.  # noqa: E501

        New name of the specified file  # noqa: E501

        :return: The file_name of this FileRenamePost.  # noqa: E501
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        """Sets the file_name of this FileRenamePost.

        New name of the specified file  # noqa: E501

        :param file_name: The file_name of this FileRenamePost.  # noqa: E501
        :type: str
        """

        self._file_name = file_name

    @property
    def entity_id(self):
        """Gets the entity_id of this FileRenamePost.  # noqa: E501

        Unique Entity Id.  # noqa: E501

        :return: The entity_id of this FileRenamePost.  # noqa: E501
        :rtype: str
        """
        return self._entity_id

    @entity_id.setter
    def entity_id(self, entity_id):
        """Sets the entity_id of this FileRenamePost.

        Unique Entity Id.  # noqa: E501

        :param entity_id: The entity_id of this FileRenamePost.  # noqa: E501
        :type: str
        """

        self._entity_id = entity_id

    @property
    def service_code(self):
        """Gets the service_code of this FileRenamePost.  # noqa: E501

        Entity service code.  # noqa: E501

        :return: The service_code of this FileRenamePost.  # noqa: E501
        :rtype: str
        """
        return self._service_code

    @service_code.setter
    def service_code(self, service_code):
        """Sets the service_code of this FileRenamePost.

        Entity service code.  # noqa: E501

        :param service_code: The service_code of this FileRenamePost.  # noqa: E501
        :type: str
        """

        self._service_code = service_code

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(FileRenamePost, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, FileRenamePost):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
