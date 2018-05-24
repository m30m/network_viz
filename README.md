# Network Visualization

A tiny python library for visualizing word networks

# Installation

You can install this package directly from github using the following command:

```sh
pip3 install git+git://github.com/m30m/network_viz.git
```

# Usage

## Structure of clustering input

The input is a list of 3-tuples. The first and the second ones are nodes and the third one is weight;

```python
[('node-1', 'node-2', 0.5), ('node-1', 'node-3', 0.7), ('node-2', 'node-2', 0.3)]
```

## API

If you are using jupyter notebook:

```python
from network_viz import visualize_notebook

visualize_notebook(edges, size=900) # size parameter is the width and height of output svg
```

If you want the raw html:

```python
from network_viz import visualize

html = visualize(clusters, size=900)

with open('output.html','w') as output_file:
    output_file.write(html)
```
