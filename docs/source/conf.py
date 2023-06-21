# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'LeetSolve'
copyright = '2023, Nhut Nguyen'
author = 'Nhut Nguyen'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'myst_parser',
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',    
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

master_doc = 'index'
# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'
html_logo = "img/logo-transparent-transformed.png"
html_theme_options = {
    'logo_only': True,
    'nosidebar': True,
}

source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    'pointsize': '12pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',        
}
latex_show_urls = 'footnote'

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'leetsolve.tex', 'The Problem Solver Guide To Coding',
     'Nhut Nguyen, Ph. D.', 'manual'),
]

