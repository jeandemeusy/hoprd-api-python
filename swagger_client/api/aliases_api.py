# coding: utf-8

"""
    HOPRd Rest API v2

    This Rest API enables developers to interact with a hoprd node programatically.  # noqa: E501

    OpenAPI spec version: 2.0.0
    Contact: tech@hoprnet.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class AliasesApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def aliases_get_alias(self, alias, **kwargs):  # noqa: E501
        """aliases_get_alias  # noqa: E501

        Get the PeerId (Hopr address) that have this alias assigned to it.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.aliases_get_alias(alias, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str alias: Alias that we previously assigned to some PeerId. (required)
        :return: InlineResponse20012
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.aliases_get_alias_with_http_info(alias, **kwargs)  # noqa: E501
        else:
            (data) = self.aliases_get_alias_with_http_info(alias, **kwargs)  # noqa: E501
            return data

    def aliases_get_alias_with_http_info(self, alias, **kwargs):  # noqa: E501
        """aliases_get_alias  # noqa: E501

        Get the PeerId (Hopr address) that have this alias assigned to it.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.aliases_get_alias_with_http_info(alias, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str alias: Alias that we previously assigned to some PeerId. (required)
        :return: InlineResponse20012
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['alias']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method aliases_get_alias" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'alias' is set
        if ('alias' not in params or
                params['alias'] is None):
            raise ValueError("Missing the required parameter `alias` when calling `aliases_get_alias`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'alias' in params:
            path_params['alias'] = params['alias']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['keyScheme', 'passwordScheme']  # noqa: E501

        return self.api_client.call_api(
            '/aliases/{alias}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20012',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def aliases_get_aliases(self, **kwargs):  # noqa: E501
        """aliases_get_aliases  # noqa: E501

        Get all aliases you set previously and thier corresponding peer IDs.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.aliases_get_aliases(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: InlineResponse2006
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.aliases_get_aliases_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.aliases_get_aliases_with_http_info(**kwargs)  # noqa: E501
            return data

    def aliases_get_aliases_with_http_info(self, **kwargs):  # noqa: E501
        """aliases_get_aliases  # noqa: E501

        Get all aliases you set previously and thier corresponding peer IDs.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.aliases_get_aliases_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: InlineResponse2006
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method aliases_get_aliases" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['keyScheme', 'passwordScheme']  # noqa: E501

        return self.api_client.call_api(
            '/aliases/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2006',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def aliases_remove_alias(self, alias, **kwargs):  # noqa: E501
        """aliases_remove_alias  # noqa: E501

        Unassign an alias from a PeerId. You can always assign back alias to that PeerId using /aliases endpoint.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.aliases_remove_alias(alias, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str alias: Alias that we want to remove. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.aliases_remove_alias_with_http_info(alias, **kwargs)  # noqa: E501
        else:
            (data) = self.aliases_remove_alias_with_http_info(alias, **kwargs)  # noqa: E501
            return data

    def aliases_remove_alias_with_http_info(self, alias, **kwargs):  # noqa: E501
        """aliases_remove_alias  # noqa: E501

        Unassign an alias from a PeerId. You can always assign back alias to that PeerId using /aliases endpoint.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.aliases_remove_alias_with_http_info(alias, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str alias: Alias that we want to remove. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['alias']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method aliases_remove_alias" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'alias' is set
        if ('alias' not in params or
                params['alias'] is None):
            raise ValueError("Missing the required parameter `alias` when calling `aliases_remove_alias`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'alias' in params:
            path_params['alias'] = params['alias']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['keyScheme', 'passwordScheme']  # noqa: E501

        return self.api_client.call_api(
            '/aliases/{alias}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def aliases_set_alias(self, **kwargs):  # noqa: E501
        """aliases_set_alias  # noqa: E501

        Instead of using HOPR address, we can assign HOPR address to a specific name called alias. Give an address a more memorable alias and use it instead of Hopr address. Aliases are kept locally and are not saved or shared on the network.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.aliases_set_alias(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AliasesBody body:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.aliases_set_alias_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.aliases_set_alias_with_http_info(**kwargs)  # noqa: E501
            return data

    def aliases_set_alias_with_http_info(self, **kwargs):  # noqa: E501
        """aliases_set_alias  # noqa: E501

        Instead of using HOPR address, we can assign HOPR address to a specific name called alias. Give an address a more memorable alias and use it instead of Hopr address. Aliases are kept locally and are not saved or shared on the network.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.aliases_set_alias_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AliasesBody body:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method aliases_set_alias" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['keyScheme', 'passwordScheme']  # noqa: E501

        return self.api_client.call_api(
            '/aliases/', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
