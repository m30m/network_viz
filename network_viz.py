import json
import random
import string
from string import Template

import pkg_resources


def __get_random_id():
    return ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(6))


def __prepare_json(edges):
    nodes = []
    links = []
    for u, v, w in edges:
        nodes.append(u)
        nodes.append(v)
        links.append({"target": u, "source": v, "strength": float(w)})
    nodes = list(set(nodes))
    nodes_json = []
    for node in nodes:
        nodes_json.append({"id": node, "group": 0, "label": node, "level": 1})
    nodes_json = json.dumps(nodes_json)
    links_json = json.dumps(links)
    return nodes_json, links_json


def visualize(edges, size=960):
    resource_package = __name__
    template = pkg_resources.resource_filename(resource_package, 'template.html')
    tmpl = Template(open(template).read())
    nodes_json, links_json = __prepare_json(edges)
    return tmpl.safe_substitute(nodes_json=nodes_json, links_json=links_json, size=size)


def visualize_notebook(*args, **kwargs):
    html = visualize(*args, **kwargs)
    from IPython.core.display import display, HTML
    display(HTML(html))
