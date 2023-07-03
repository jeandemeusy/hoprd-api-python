# coding: utf-8

"""
    HOPRd Rest API v2

    This Rest API enables developers to interact with a hoprd node programatically.  # noqa: E501

    OpenAPI spec version: 2.0.0
    Contact: tech@hoprnet.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class AccountWithdrawBody(object):
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
        'currency': 'Currency',
        'amount': 'str',
        'recipient': 'NativeAddress'
    }

    attribute_map = {
        'currency': 'currency',
        'amount': 'amount',
        'recipient': 'recipient'
    }

    def __init__(self, currency=None, amount=None, recipient=None):  # noqa: E501
        """AccountWithdrawBody - a model defined in Swagger"""  # noqa: E501
        self._currency = None
        self._amount = None
        self._recipient = None
        self.discriminator = None
        self.currency = currency
        self.amount = amount
        self.recipient = recipient

    @property
    def currency(self):
        """Gets the currency of this AccountWithdrawBody.  # noqa: E501


        :return: The currency of this AccountWithdrawBody.  # noqa: E501
        :rtype: Currency
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this AccountWithdrawBody.


        :param currency: The currency of this AccountWithdrawBody.  # noqa: E501
        :type: Currency
        """
        if currency is None:
            raise ValueError("Invalid value for `currency`, must not be `None`")  # noqa: E501

        self._currency = currency

    @property
    def amount(self):
        """Gets the amount of this AccountWithdrawBody.  # noqa: E501

        Amount to withdraw in the currency's smallest unit.  # noqa: E501

        :return: The amount of this AccountWithdrawBody.  # noqa: E501
        :rtype: str
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this AccountWithdrawBody.

        Amount to withdraw in the currency's smallest unit.  # noqa: E501

        :param amount: The amount of this AccountWithdrawBody.  # noqa: E501
        :type: str
        """
        if amount is None:
            raise ValueError("Invalid value for `amount`, must not be `None`")  # noqa: E501

        self._amount = amount

    @property
    def recipient(self):
        """Gets the recipient of this AccountWithdrawBody.  # noqa: E501


        :return: The recipient of this AccountWithdrawBody.  # noqa: E501
        :rtype: NativeAddress
        """
        return self._recipient

    @recipient.setter
    def recipient(self, recipient):
        """Sets the recipient of this AccountWithdrawBody.


        :param recipient: The recipient of this AccountWithdrawBody.  # noqa: E501
        :type: NativeAddress
        """
        if recipient is None:
            raise ValueError("Invalid value for `recipient`, must not be `None`")  # noqa: E501

        self._recipient = recipient

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
        if issubclass(AccountWithdrawBody, dict):
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
        if not isinstance(other, AccountWithdrawBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
