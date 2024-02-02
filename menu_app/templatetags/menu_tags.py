from django import template
from django.utils.datastructures import MultiValueDictKeyError
from django.utils.safestring import mark_safe

from ..models import MenuItem

register = template.Library()


@register.inclusion_tag('index.html', takes_context=True)
def draw_menu(context, menu_title):
    res = {}

    try:
        name = context['request'].GET['menu']
        item = [menu_item for menu_item in MenuItem.objects.filter(title=name)][0]

    except MultiValueDictKeyError:
        item = [menu_item for menu_item in MenuItem.objects.filter(title=menu_title)][0]

    parents = get_parents(item)
    children = get_children(item)

    res['parents'] = parents
    res['children'] = children

    return res


def get_parents(item):
    parents_list = []
    while item:
        parents_list.append(item)
        item = item.parent
    return parents_list[::-1]


def get_children(item):
    children_list = []
    for child in item.children.all():
        children_list.append(child)
    return children_list


@register.filter
def list_to_html(parents, children):
    html = '<ul>'
    level = 0

    for parent in parents:
        if level == 0:
            html += f'<li><a href="?menu={parent.title}">{parent.title}</a>'
        else:
            html += f'<ul><li><a href="?menu={parent.title}">{parent.title}</a>'
        level += 1

    html += '<ul>'
    for child in children:
        html += f'<li><a href="?menu={child.title}">{child.title}</a></li>'
    html += '</ul>'

    html += '</li></ul>' * (level - 1)

    return mark_safe(html)
