import sphinx_material
# -*- coding: utf-8 -*-
#
# Configuration file for the Sphinx documentation builder.
#
# This file does only contain a selection of the most common options. For a
# full list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'Seldon'
copyright = '2019, Seldon Team'
author = 'Seldon Team'

# The short X.Y version
version = ''
# The full version, including alpha/beta/rc tags
release = ''


# -- General configuration ---------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
        "m2r2",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = ['.rst', '.md']

# The master toctree document.
master_doc = 'index'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

exclude_patterns = []

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = None


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_material"

if html_theme == "sphinx_material":
    html_theme_options = {
        "google_analytics_account": "UA-54780881-2",
        "base_url": "https://docs.seldon.io/",
        "color_primary": "indigo",
        "color_accent": "teal",
        "repo_url": "https://github.com/SeldonIO/seldon-core",
        "repo_name": "Seldon Documentation",
        "nav_title": "Seldon Documentation Homepage",
        "globaltoc_depth": 4,
        "globaltoc_collapse": True,
        "globaltoc_includehidden": False,
        "repo_type": "github",
        "nav_links": [
            {
                "href": "https://docs.seldon.io/projects/seldon-core/en/latest/",
                "internal": False,
                "title": "🚀 Our Other Projects & Products:",
            },
            {
                "href": "https://docs.seldon.io/projects/seldon-core/en/latest/",
                "internal": False,
                "title": "Seldon Core",
            },
            {
                "href": "https://docs.seldon.io/projects/alibi/en/stable/",
                "internal": False,
                "title": "Alibi Explain",
            },
            {
                "href": "https://docs.seldon.io/projects/alibi-detect/en/stable/",
                "internal": False,
                "title": "Alibi Detect",
            },
            {
                "href": "https://mlserver.readthedocs.io/en/latest/",
                "internal": False,
                "title": "MLServer",
            },
            {
                "href": "https://tempo.readthedocs.io/en/latest/",
                "internal": False,
                "title": "Tempo SDK",
            },
            {
                "href": "https://deploy.seldon.io/",
                "internal": False,
                "title": "Seldon Deploy (Enterprise)",
            },
            {
                "href": "https://github.com/SeldonIO/seldon-deploy-sdk#seldon-deploy-sdk",
                "internal": False,
                "title": "Seldon Deploy SDK (Enterprise)",
            },
        ],
    }

    extensions.append("sphinx_material")
    html_theme_path = sphinx_material.html_theme_path()
    html_context = sphinx_material.get_html_context()

html_extra_path = ["_extra"]

html_sidebars = {"**": ["logo-text.html", "globaltoc.html", "localtoc.html"]}

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# The default sidebars (for documents that don't match any pattern) are
# defined by theme itself.  Builtin themes are using these templates by
# default: ``['localtoc.html', 'relations.html', 'sourcelink.html',
# 'searchbox.html']``.
#
# html_sidebars = {}

html_show_sphinx = False

# -- Options for HTMLHelp output ---------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'Seldondoc'


# -- Options for LaTeX output ------------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'Seldon.tex', 'Seldon Documentation',
     'Seldon Team', 'manual'),
]


# -- Options for manual page output ------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'seldon', 'Seldon Documentation',
     [author], 1)
]


# -- Options for Texinfo output ----------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'Seldon', 'Seldon Documentation',
     author, 'Seldon', 'One line description of project.',
     'Miscellaneous'),
]


# -- Options for Epub output -------------------------------------------------

# Bibliographic Dublin Core info.
epub_title = project

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
#
# epub_identifier = ''

# A unique identification for the text.
#
# epub_uid = ''

# A list of files that should not be packed into the epub file.
epub_exclude_files = ['search.html']
