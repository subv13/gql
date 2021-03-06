# coding=utf-8
# future
from __future__ import absolute_import, unicode_literals

from typing import Any

import graphene
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator as DjangoPaginator
from graphene import ObjectType

from tablet.models import Product as ProductModel
from tablet.schema.helpers import filters_into_filter_args, sorters_into_order_by_args
from tablet.schema.products.types import Product
from tablet.schema.types import IntegerFilter, Paginator, SortOrder, StringFilter


class SortableFields(graphene.Enum):
    ID = "id"
    NAME = "name"
    CATEGORY = "category"


class Sorter(graphene.InputObjectType):
    field = SortableFields()
    order = SortOrder()


class Filter(graphene.InputObjectType):
    id = IntegerFilter()
    name = StringFilter()
    category = StringFilter()

    OR = graphene.List(lambda: Filter)
    AND = graphene.List(lambda: Filter)
    NOT = graphene.Field(lambda: Filter)


class ProductsPage(ObjectType):
    object_list = graphene.List(graphene.NonNull(Product), required=True)
    paginator = graphene.Field(Paginator, required=True)
    page_number = graphene.Int(required=True)

    @staticmethod
    def resolve_page_number(parent, info, **kwargs):
        return parent.number


def resolve_products(_parent, _info, page, per_page, sorters=None, filters=None):
    # type: (Any, Any, int, int, [Sorter], [Filter]) -> ProductsPage
    if not sorters:
        sorters = []

    if not filters:
        filters = []

    order_by_args = sorters_into_order_by_args(sorters)
    filter_args = filters_into_filter_args(filters)
    queryset = ProductModel.objects.order_by(*order_by_args).filter(filter_args)
    paginator = DjangoPaginator(queryset, per_page)

    try:
        return paginator.page(page)
    except PageNotAnInteger:
        return paginator.page(1)
    except EmptyPage:
        return paginator.page(paginator.num_pages)
