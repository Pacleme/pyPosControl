import sys

import os
sys.path.insert(0, os.path.abspath('../..'))

# from pathlib import Path
# sys.path.insert(0, str(Path(__file__,'../../../python_files').resolve()))
# print(str(Path(__file__,'../../../python_files').resolve()))

# from ...python_files.models import ModelControl

import sphinx_rtd_theme

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'pyPosControl'
copyright = '2025, Clément PACAULT'
author = 'Clément PACAULT'
release = '0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    # 'sphinx.ext.githubpages',
    #'recommonmark',
    'sphinx_rtd_theme',
]

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# html_theme = 'alabaster'
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
# html_context = {'github_user_name': 'pacleme', 'github_repo_name': 'Pacleme.github.io','project_name': project}

# def skip(app, what, name, obj, would_skip, options):
#     if name == "__init__":
#         return False
#     return would_skip

# def setup(app):
#     app.connect("autodoc-skip-member", skip)