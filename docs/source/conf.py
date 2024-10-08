# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html
import sys, os
cwd = os.path.dirname(os.path.abspath(__file__))

sys.path.insert(1, os.path.abspath(os.path.join(cwd, '../../src')))

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'muTel'
copyright = '2024, Martín Alcalde Martínez'
author = 'Martín Alcalde Martínez'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.napoleon']

templates_path = ['_templates']
exclude_patterns = ['*dqm*', '*legacy*']



# -- Options for HTML output 
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']



# -- Napoleon settings -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/extensions/napoleon.html

master_doc = 'modules'

napoleon_google_docstring = True
napoleon_numpy_docstring = True
napoleon_include_init_with_doc = False
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = True
napoleon_use_admonition_for_examples = False
napoleon_use_admonition_for_notes = False
napoleon_use_admonition_for_references = False
napoleon_use_ivar = False
napoleon_use_param = True
napoleon_use_rtype = True
napoleon_preprocess_types = False
napoleon_type_aliases = None
napoleon_attr_annotations = True