"""Generates HTML grid for gallery examples"""
import os
import glob
import jinja2


here = os.path.dirname(os.path.abspath(__file__))
EXAMPLE_GLOB = "../examples/*_layer.py"
layer_names = sorted([os.path.basename(layer_name).replace('.py', '') for layer_name in glob.glob(EXAMPLE_GLOB)])


HTML_TEMPLATE = jinja2.Template(
    """
<style>
.wrapper {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  grid-gap: 1px;
}
.grid-cell {
  min-height: 60px;
  position: relative;

}
.thumb-text {
  z-index: 1;
  bottom: 0;
  left: 0;
  position: absolute;
  font-weight: 100;
  color: white;
}

.grid-cell:hover {
  filter: hue-rotate(3.142rad);
}

</style>

<div class='wrapper'>
{% for layer_name in layer_names %}
  {# Sphinx decides where these files get hosted but it's by default the directroy in the src tag #}
  <div class='grid-cell'>
      <a href="/{{layer_name}}.html">
    <img width="200" src="/_images/{{layer_name}}.png"></img>
      <div class='thumb-text'>{{ make_presentable(layer_name) }}</div></a>
  </div>
{% endfor %}
</div>
""")


def make_presentable(s):
    return s.replace('_', ' ').title().replace('json', 'Json')


def main():
    doc_source = HTML_TEMPLATE.render(
        layer_names=layer_names,
        make_presentable=make_presentable
    )
    with open(os.path.join(here, '../gallery/html/grid.html'), 'w+') as f:
        f.write(doc_source)


if __name__ == "__main__":
    main()