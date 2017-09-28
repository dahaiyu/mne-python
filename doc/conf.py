# -*- coding: utf-8 -*-
#
# MNE documentation build configuration file, created by
# sphinx-quickstart on Fri Jun 11 10:45:48 2010.
#
# This file is execfile()d with the current directory set to its containing
# dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import inspect
import os
from os.path import relpath, dirname
import sys
from datetime import date
import sphinx_gallery  # noqa
import sphinx_bootstrap_theme
from numpydoc import numpydoc, docscrape  # noqa
import mne

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
curdir = os.path.dirname(__file__)
sys.path.append(os.path.abspath(os.path.join(curdir, '..', 'mne')))
sys.path.append(os.path.abspath(os.path.join(curdir, 'sphinxext')))

if not os.path.isdir('_images'):
    os.mkdir('_images')

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#needs_sphinx = '1.0'

# XXX This hack defines what extra methods numpydoc will document
docscrape.ClassDoc.extra_public_methods = mne.utils._doc_special_members

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom ones.

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.coverage',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.linkcode',
    'sphinx.ext.mathjax',
    'sphinx.ext.todo',
    'sphinx_gallery.gen_gallery',
    'numpydoc',
    'gen_commands',
]

autosummary_generate = True
autodoc_default_flags = ['inherited-members']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
#source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'MNE'
td = date.today()
copyright = u'2012-%s, MNE Developers. Last updated on %s' % (td.year,
                                                              td.isoformat())

nitpicky = True
needs_sphinx = '1.5'
suppress_warnings = ['image.nonlocal_uri']  # we intentionally link outside

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = mne.__version__
# The full version, including alpha/beta/rc tags.
release = version

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'

# List of documents that shouldn't be included in the build.
unused_docs = []

# List of directories, relative to source directory, that shouldn't be searched
# for source files.
exclude_trees = ['_build']
exclude_patterns = ['source/generated']

# The reST default role (used for this markup: `text`) to use for all
# documents.
#default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
#add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'  # friendly, manni, murphy, tango

# A list of ignored prefixes for module index sorting.
modindex_common_prefix = ['mne.']

# If true, keep warnings as "system message" paragraphs in the built documents.
#keep_warnings = False


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'bootstrap'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
html_theme_options = {
    'navbar_title': ' ',  # we replace this with an image
    'source_link_position': "nav",  # default
    'bootswatch_theme': "flatly",  # yeti paper lumen
    'navbar_sidebarrel': False,  # Render the next/prev links in navbar?
    'navbar_pagenav': False,
    'navbar_class': "navbar",
    'bootstrap_version': "3",  # default
    'navbar_links': [
        ("Install", "getting_started"),
        ("Documentation", "documentation"),
        ("API", "python_reference"),
        ("Examples", "auto_examples/index"),
        ("Contribute", "contributing"),
    ],
    }

# Add any paths that contain custom themes here, relative to this directory.
html_theme_path = sphinx_bootstrap_theme.get_html_theme_path()

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
#html_title = None

# A shorter title for the navigation bar.  Default is the same as html_title.
#html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
html_logo = "_static/mne_logo_small.png"

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
html_favicon = "_static/favicon.ico"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static', '_images']

# Add any extra paths that contain custom files (such as robots.txt or
# .htaccess) here, relative to this directory. These files are copied
# directly to the root of the documentation.
#html_extra_path = []

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
#html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
#html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
#html_additional_pages = {}

# If false, no module index is generated.
#html_domain_indices = True

# If false, no index is generated.
#html_use_index = True

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, links to the reST sources are added to the pages.
html_show_sourcelink = False

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
html_show_sphinx = False

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
#html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# variables to pass to HTML templating engine
build_dev_html = bool(int(os.environ.get('BUILD_DEV_HTML', False)))

html_context = {'use_google_analytics': True, 'use_twitter': True,
                'use_media_buttons': True, 'build_dev_html': build_dev_html}

# This is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = None

# Output file base name for HTML help builder.
htmlhelp_basename = 'mne-doc'


# -- Options for LaTeX output ---------------------------------------------

# The paper size ('letter' or 'a4').
# latex_paper_size = 'letter'

# The font size ('10pt', '11pt' or '12pt').
# latex_font_size = '10pt'

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass
# [howto/manual]).
latex_documents = [
#    ('index', 'MNE.tex', u'MNE Manual',
#     u'MNE Contributors', 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
latex_logo = "_static/logo.png"

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
latex_toplevel_sectioning = 'part'

# Additional stuff for the LaTeX preamble.
# latex_preamble = ''

# Documents to append as an appendix to all manuals.
# latex_appendices = []

# If false, no module index is generated.
#latex_domain_indices = True

trim_doctests_flags = True

# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {
    'python': ('http://docs.python.org', None),
    'numpy': ('http://docs.scipy.org/doc/numpy-dev', None),
    'scipy': ('http://scipy.github.io/devdocs', None),
    'matplotlib': ('http://matplotlib.org', None),
    'sklearn': ('http://scikit-learn.org/stable', None),
    'mayavi': ('http://docs.enthought.com/mayavi/mayavi', None),
    'nibabel': ('http://nipy.org/nibabel', None),
    'nilearn': ('http://nilearn.github.io', None),
    'surfer': ('https://pysurfer.github.io/', None),
}

examples_dirs = ['../examples', '../tutorials']
gallery_dirs = ['auto_examples', 'auto_tutorials']

try:
    mlab = mne.utils._import_mlab()
    find_mayavi_figures = True
    # Do not pop up any mayavi windows while running the
    # examples. These are very annoying since they steal the focus.
    mlab.options.offscreen = True
except Exception:
    find_mayavi_figures = False

sphinx_gallery_conf = {
    'doc_module': ('mne',),
    'reference_url': {
        'mne': None,
        'numpy': 'http://docs.scipy.org/doc/numpy',
        'scipy': 'http://docs.scipy.org/doc/scipy/reference',
        'matplotlib': 'http://matplotlib.org',
        'sklearn': 'http://scikit-learn.org/stable',
        'mayavi': 'http://docs.enthought.com/mayavi/mayavi',
        'nibabel': 'http://nipy.org/nibabel',
        'nilearn': 'http://nilearn.github.io',
        'surfer': 'https://pysurfer.github.io',
        },
    'examples_dirs': examples_dirs,
    'gallery_dirs': gallery_dirs,
    'find_mayavi_figures': find_mayavi_figures,
    'default_thumb_file': os.path.join('_static', 'mne_helmet.png'),
    'backreferences_dir': 'generated',
    'plot_gallery': 'True',  # Avoid annoying Unicode/bool default warning
    'download_section_examples': False,
    'thumbnail_size': (160, 112),
    'min_reported_time': 1.,
}

numpydoc_class_members_toctree = False


# -----------------------------------------------------------------------------
# Source code links (adapted from SciPy (doc/source/conf.py))
# -----------------------------------------------------------------------------

def linkcode_resolve(domain, info):
    """
    Determine the URL corresponding to Python object
    """
    if domain != 'py':
        return None

    modname = info['module']
    fullname = info['fullname']

    submod = sys.modules.get(modname)
    if submod is None:
        return None

    obj = submod
    for part in fullname.split('.'):
        try:
            obj = getattr(obj, part)
        except:
            return None

    try:
        fn = inspect.getsourcefile(obj)
    except:
        fn = None
    if not fn:
        try:
            fn = inspect.getsourcefile(sys.modules[obj.__module__])
        except:
            fn = None
    if not fn:
        return None

    try:
        source, lineno = inspect.getsourcelines(obj)
    except:
        lineno = None

    if lineno:
        linespec = "#L%d-L%d" % (lineno, lineno + len(source) - 1)
    else:
        linespec = ""

    fn = relpath(fn, start=dirname(mne.__file__))

    if 'dev' in mne.__version__:
        kind = 'master'
    else:
        kind = 'maint/%s' % ('.'.join(mne.__version__.split('.')[:2]))
    return "http://github.com/mne-tools/mne-python/blob/%s/mne/%s%s" % (  # noqa
       kind, fn, linespec)
