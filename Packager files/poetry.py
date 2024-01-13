[[package]]
name = "aiohttp"
version = "3.8.3"
description = "Async http client/server framework (asyncio)"
category = "main"
optional = false
python-versions = ">=3.6"

[package.dependencies]
aiosignal = ">=1.1.2"
async-timeout = ">=4.0.0a3,<5.0"
attrs = ">=17.3.0"
charset-normalizer = ">=2.0,<3.0"
frozenlist = ">=1.1.1"
multidict = ">=4.5,<7.0"
yarl = ">=1.0,<2.0"

[package.extras]
speedups = ["aiodns", "brotli", "cchardet"]

[[package]]
name = "aiosignal"
version = "1.3.1"
description = "aiosignal: a list of registered asynchronous callbacks"
category = "main"
optional = false
python-versions = ">=3.7"

[package.dependencies]
frozenlist = ">=1.1.0"

[[package]]
name = "anyio"
version = "3.6.2"
description = "High level compatibility layer for multiple asynchronous event loop implementations"
category = "main"
optional = false
python-versions = ">=3.6.2"

[package.dependencies]
idna = ">=2.8"
sniffio = ">=1.1"

[package.extras]
doc = ["packaging", "sphinx-rtd-theme", "sphinx-autodoc-typehints (>=1.2.0)"]
test = ["coverage[toml] (>=4.5)", "hypothesis (>=4.0)", "pytest (>=7.0)", "pytest-mock (>=3.6.1)", "trustme", "contextlib2", "uvloop (<0.15)", "mock (>=4)", "uvloop (>=0.15)"]
trio = ["trio (>=0.16,<0.22)"]

[[package]]
name = "argon2-cffi"
version = "21.3.0"
description = "The secure Argon2 password hashing algorithm."
category = "main"
optional = false
python-versions = ">=3.6"

[package.dependencies]
argon2-cffi-bindings = "*"

[package.extras]
dev = ["pre-commit", "cogapp", "tomli", "coverage[toml] (>=5.0.2)", "hypothesis", "pytest", "sphinx", "sphinx-notfound-page", "furo"]
docs = ["sphinx", "sphinx-notfound-page", "furo"]
tests = ["coverage[toml] (>=5.0.2)", "hypothesis", "pytest"]

[[package]]
name = "argon2-cffi-bindings"
version = "21.2.0"
description = "Low-level CFFI bindings for Argon2"
category = "main"
optional = false
python-versions = ">=3.6"

[package.dependencies]
cffi = ">=1.0.1"

[package.extras]
dev = ["pytest", "cogapp", "pre-commit", "wheel"]
tests = ["pytest"]

[[package]]
name = "async-timeout"
version = "4.0.2"
description = "Timeout context manager for asyncio programs"
category = "main"
optional = false
python-versions = ">=3.6"

[[package]]
name = "attrs"
version = "22.2.0"
description = "Classes Without Boilerplate"
category = "main"
optional = false
python-versions = ">=3.6"

[package.extras]
cov = ["attrs", "coverage-enable-subprocess", "coverage[toml] (>=5.3)"]
dev = ["attrs"]
docs = ["furo", "sphinx", "myst-parser", "zope.interface", "sphinx-notfound-page", "sphinxcontrib-towncrier", "towncrier"]
tests = ["attrs", "zope.interface"]
tests-no-zope = ["hypothesis", "pympler", "pytest (>=4.3.0)", "pytest-xdist", "cloudpickle", "mypy (>=0.971,<0.990)", "pytest-mypy-plugins"]
tests_no_zope = ["hypothesis", "pympler", "pytest (>=4.3.0)", "pytest-xdist", "cloudpickle", "mypy (>=0.971,<0.990)", "pytest-mypy-plugins"]

[[package]]
name = "certifi"
version = "2022.12.7"
description = "Python package for providing Mozilla's CA Bundle."
category = "main"
optional = false
python-versions = ">=3.6"

[[package]]
name = "cffi"
version = "1.15.1"
description = "Foreign Function Interface for Python calling C code."
category = "main"
optional = false
python-versions = "*"

[package.dependencies]
pycparser = "*"

[[package]]
name = "charset-normalizer"
version = "2.1.1"
description = "The Real First Universal Charset Detector. Open, modern and actively maintained alternative to Chardet."
category = "main"
optional = false
python-versions = ">=3.6.0"

[package.extras]
unicode_backport = ["unicodedata2"]

[[package]]
name = "click"
version = "8.1.3"
description = "Composable command line interface toolkit"
category = "main"
optional = false
python-versions = ">=3.7"

[package.dependencies]
colorama = {version = "*", markers = "platform_system == \"Windows\""}

[[package]]
name = "colorama"
version = "0.4.6"
description = "Cross-platform colored terminal text."
category = "main"
optional = false
python-versions = "!=3.0.*,!=3.1.*,!=3.2.*,!=3.3.*,!=3.4.*,!=3.5.*,!=3.6.*,>=2.7"

[[package]]
name = "cryptography"
version = "38.0.4"
description = "cryptography is a package which provides cryptographic recipes and primitives to Python developers."
category = "main"
optional = false
python-versions = ">=3.6"

[package.dependencies]
cffi = ">=1.12"

[package.extras]
docs = ["sphinx (>=1.6.5,!=1.8.0,!=3.1.0,!=3.1.1)", "sphinx-rtd-theme"]
docstest = ["pyenchant (>=1.6.11)", "twine (>=1.12.0)", "sphinxcontrib-spelling (>=4.0.1)"]
pep8test = ["black", "flake8", "flake8-import-order", "pep8-naming"]
sdist = ["setuptools-rust (>=0.11.4)"]
ssh = ["bcrypt (>=3.1.5)"]
test = ["pytest (>=6.2.0)", "pytest-benchmark", "pytest-cov", "pytest-subtests", "pytest-xdist", "pretend", "iso8601", "pytz", "hypothesis (>=1.11.4,!=3.79.2)"]

[[package]]
name = "debugpy"
version = "1.6.5"
description = "An implementation of the Debug Adapter Protocol for Python"
category = "dev"
optional = false
python-versions = ">=3.7"

[[package]]
name = "flask"
version = "2.2.2"
description = "A simple framework for building complex web applications."
category = "main"
optional = false
python-versions = ">=3.7"

[package.dependencies]
click = ">=8.0"
itsdangerous = ">=2.0"
Jinja2 = ">=3.0"
Werkzeug = ">=2.2.2"

[package.extras]
async = ["asgiref (>=3.2)"]
dotenv = ["python-dotenv"]

[[package]]
name = "frozenlist"
version = "1.3.3"
description = "A list-like structure which implements collections.abc.MutableSequence"
category = "main"
optional = false
python-versions = ">=3.7"

[[package]]
name = "h11"
version = "0.14.0"
description = "A pure-Python, bring-your-own-I/O implementation of HTTP/1.1"
category = "main"
optional = false
python-versions = ">=3.7"

[[package]]
name = "httpcore"
version = "0.17.0"
description = "A minimal low-level HTTP client."
category = "main"
optional = false
python-versions = ">=3.7"

[package.dependencies]
anyio = ">=3.0,<5.0"
certifi = "*"
h11 = ">=0.13,<0.15"
sniffio = ">=1.0.0,<2.0.0"

[package.extras]
http2 = ["h2 (>=3,<5)"]
socks = ["socksio (>=1.0.0,<2.0.0)"]

[[package]]
name = "httpx"
version = "0.24.0"
description = "The next generation HTTP client."
category = "main"
optional = false
python-versions = ">=3.7"

[package.dependencies]
certifi = "*"
httpcore = ">=0.15.0,<0.18.0"
idna = "*"
sniffio = "*"

[package.extras]
brotli = ["brotli", "brotlicffi"]
cli = ["click (>=8.0.0,<9.0.0)", "pygments (>=2.0.0,<3.0.0)", "rich (>=10,<14)"]
http2 = ["h2 (>=3,<5)"]
socks = ["socksio (>=1.0.0,<2.0.0)"]

[[package]]
name = "idna"
version = "3.4"
description = "Internationalized Domain Names in Applications (IDNA)"
category = "main"
optional = false
python-versions = ">=3.5"

[[package]]
name = "iso8601"
version = "1.1.0"
description = "Simple module to parse ISO 8601 dates"
category = "main"
optional = false
python-versions = ">=3.6.2,<4.0"

[[package]]
name = "itsdangerous"
version = "2.1.2"
description = "Safely pass data to untrusted environments and back."
category = "main"
optional = false
python-versions = ">=3.7"

[[package]]
name = "jedi"
version = "0.18.2"
description = "An autocompletion tool for Python that can be used for text editors."
category = "dev"
optional = false
python-versions = ">=3.6"

[package.dependencies]
parso = ">=0.8.0,<0.9.0"

[package.extras]
docs = ["Jinja2 (==2.11.3)", "MarkupSafe (==1.1.1)", "Pygments (==2.8.1)", "alabaster (==0.7.12)", "babel (==2.9.1)", "chardet (==4.0.0)", "commonmark (==0.8.1)", "docutils (==0.17.1)", "future (==0.18.2)", "idna (==2.10)", "imagesize (==1.2.0)", "mock (==1.0.1)", "packaging (==20.9)", "pyparsing (==2.4.7)", "pytz (==2021.1)", "readthedocs-sphinx-ext (==2.1.4)", "recommonmark (==0.5.0)", "requests (==2.25.1)", "six (==1.15.0)", "snowballstemmer (==2.1.0)", "sphinx-rtd-theme (==0.4.3)", "sphinx (==1.8.5)", "sphinxcontrib-serializinghtml (==1.1.4)", "sphinxcontrib-websupport (==1.2.4)", "urllib3 (==1.26.4)"]
qa = ["flake8 (==3.8.3)", "mypy (==0.782)"]
testing = ["Django (<3.1)", "attrs", "colorama", "docopt", "pytest (<7.0.0)"]

[[package]]
name = "jinja2"
version = "3.1.2"
description = "A very fast and expressive template engine."
category = "main"
optional = false
python-versions = ">=3.7"

[package.dependencies]
MarkupSafe = ">=2.0"

[package.extras]
i18n = ["Babel (>=2.7)"]

[[package]]
name = "markupsafe"
version = "2.1.2"
description = "Safely add untrusted strings to HTML/XML markup."
category = "main"
optional = false
python-versions = ">=3.7"

[[package]]
name = "multidict"
version = "6.0.4"
description = "multidict implementation"
category = "main"
optional = false
python-versions = ">=3.7"

[[package]]
name = "numpy"
version = "1.24.1"
description = "Fundamental package for array computing in Python"
category = "main"
optional = false
python-versions = ">=3.8"

[[package]]
name = "packaging"
version = "23.0"
description = "Core utilities for Python packages"
category = "dev"
optional = false
python-versions = ">=3.7"

[[package]]
name = "parso"
version = "0.8.3"
description = "A Python Parser"
category = "dev"
optional = false
python-versions = ">=3.6"

[package.extras]
qa = ["flake8 (==3.8.3)", "mypy (==0.782)"]
testing = ["docopt", "pytest (<6.0.0)"]

[[package]]
name = "passlib"
version = "1.7.4"
description = "comprehensive password hashing framework supporting over 30 schemes"
category = "main"
optional = false
python-versions = "*"

[package.dependencies]
argon2-cffi = {version = ">=18.2.0", optional = true, markers = "extra == \"argon2\""}

[package.extras]
argon2 = ["argon2-cffi (>=18.2.0)"]
bcrypt = ["bcrypt (>=3.1.0)"]
build_docs = ["sphinx (>=1.6)", "sphinxcontrib-fulltoc (>=1.2.0)", "cloud-sptheme (>=1.10.1)"]
totp = ["cryptography"]

[[package]]
name = "platformdirs"
version = "2.6.2"
description = "A small Python package for determining appropriate platform-specific dirs, e.g. a \"user data dir\"."
category = "dev"
optional = false
python-versions = ">=3.7"

[package.extras]
docs = ["furo (>=2022.12.7)", "proselint (>=0.13)", "sphinx-autodoc-typehints (>=1.19.5)", "sphinx (>=5.3)"]
test = ["appdirs (==1.4.4)", "covdefaults (>=2.2.2)", "pytest-cov (>=4)", "pytest-mock (>=3.10)", "pytest (>=7.2)"]

[[package]]
name = "pluggy"
version = "1.0.0"
description = "plugin and hook calling mechanisms for python"
category = "dev"
optional = false
python-versions = ">=3.6"

[package.extras]
testing = ["pytest-benchmark", "pytest"]
dev = ["tox", "pre-commit"]

[[package]]
name = "protobuf"
version = "4.21.12"
description = ""
category = "main"
optional = false
python-versions = ">=3.7"

[[package]]
name = "pycparser"
version = "2.21"
description = "C parser in Python"
category = "main"
optional = false
python-versions = ">=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*"

[[package]]
name = "pycryptodomex"
version = "3.16.0"
description = "Cryptographic library for Python"
category = "main"
optional = false
python-versions = ">=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*"

[[package]]
name = "pyflakes"
version = "2.5.0"
description = "passive checker of Python programs"
category = "dev"
optional = false
python-versions = ">=3.6"

[[package]]
name = "pyseto"
version = "1.7.0"
description = "A Python implementation of PASETO/PASERK."
category = "main"
optional = false
python-versions = ">=3.7,<4.0"

[package.dependencies]
cryptography = ">=36,<39"
iso8601 = ">=1.0.2,<2.0.0"
passlib = {version = ">=1.7.4,<2.0.0", extras = ["argon2"]}
pycryptodomex = ">=3.12.0,<4.0.0"

[package.extras]
docs = ["Sphinx[docs] (>=4.3.2,<6.0.0)", "sphinx-autodoc-typehints[docs] (==1.12.0)", "sphinx-rtd-theme[docs] (>=1.0.0,<2.0.0)"]

[[package]]
name = "python-lsp-jsonrpc"
version = "1.0.0"
description = "JSON RPC 2.0 server library"
category = "dev"
optional = false
python-versions = "*"

[package.dependencies]
ujson = ">=3.0.0"

[package.extras]
test = ["coverage", "pytest-cov", "pytest", "pyflakes", "pycodestyle", "pylint"]

[[package]]
name = "pytoolconfig"
version = "1.2.5"
description = "Python tool configuration"
category = "dev"
optional = false
python-versions = ">=3.7"

[package.dependencies]
packaging = ">=22.0"
platformdirs = {version = ">=1.4.4", optional = true, markers = "extra == \"global\""}
tomli = {version = ">=2.0.1", markers = "python_version < \"3.11\""}

[package.extras]
doc = ["tabulate (>=0.8.9)", "sphinx (>=4.5.0)"]
gendocs = ["sphinx (>=4.5.0)", "sphinx-autodoc-typehints (>=1.18.1)", "sphinx-rtd-theme (>=1.0.0)", "pytoolconfig"]
global = ["platformdirs (>=1.4.4)"]
validation = ["pydantic (>=1.7.4)"]

[[package]]
name = "replit"
version = "3.2.5"
description = "A library for interacting with features of repl.it"
category = "main"
optional = false
python-versions = ">=3.8,<4.0"

[package.dependencies]
aiohttp = ">=3.6.2,<4.0.0"
Flask = ">=2.0.0,<3.0.0"
protobuf = ">=4.21.8,<5.0.0"
pyseto = ">=1.6.11,<2.0.0"
requests = ">=2.25.1,<3.0.0"
typing_extensions = ">=3.7.4,<4.0.0"
Werkzeug = ">=2.0.0,<3.0.0"

[[package]]
name = "replit-python-lsp-server"
version = "1.15.9"
description = "Python Language Server for the Language Server Protocol"
category = "dev"
optional = false
python-versions = ">=3.7"

[package.dependencies]
jedi = ">=0.17.2,<0.19.0"
pluggy = ">=1.0.0"
pyflakes = {version = ">=2.5.0,<2.6.0", optional = true, markers = "extra == \"pyflakes\""}
python-lsp-jsonrpc = ">=1.0.0"
rope = {version = ">0.10.5", optional = true, markers = "extra == \"rope\""}
toml = ">=0.10.2"
ujson = ">=3.0.0"
whatthepatch = {version = ">=1.0.2,<2.0.0", optional = true, markers = "extra == \"yapf\""}
yapf = {version = "*", optional = true, markers = "extra == \"yapf\""}

[package.extras]
all = ["autopep8 (>=1.6.0,<1.7.0)", "flake8 (>=5.0.0,<5.1.0)", "mccabe (>=0.7.0,<0.8.0)", "pycodestyle (>=2.9.0,<2.10.0)", "pydocstyle (>=2.0.0)", "pyflakes (>=2.5.0,<2.6.0)", "pylint (>=2.5.0)", "rope (>=0.10.5)", "yapf", "whatthepatch"]
autopep8 = ["autopep8 (>=1.6.0,<1.7.0)"]
flake8 = ["flake8 (>=5.0.0,<5.1.0)"]
mccabe = ["mccabe (>=0.7.0,<0.8.0)"]
pycodestyle = ["pycodestyle (>=2.9.0,<2.10.0)"]
pydocstyle = ["pydocstyle (>=2.0.0)"]
pyflakes = ["pyflakes (>=2.5.0,<2.6.0)"]
pylint = ["pylint (>=2.5.0)"]
rope = ["rope (>0.10.5)"]
test = ["pylint (>=2.5.0)", "pytest", "pytest-cov", "coverage", "numpy (<1.23)", "pandas", "matplotlib", "pyqt5", "flaky"]
websockets = ["websockets (>=10.3)"]
yapf = ["yapf", "whatthepatch (>=1.0.2,<2.0.0)"]

[[package]]
name = "requests"
version = "2.28.2"
description = "Python HTTP for Humans."
category = "main"
optional = false
python-versions = ">=3.7, <4"

[package.dependencies]
certifi = ">=2017.4.17"
charset-normalizer = ">=2,<4"
idna = ">=2.5,<4"
urllib3 = ">=1.21.1,<1.27"

[package.extras]
socks = ["PySocks (>=1.5.6,!=1.5.7)"]
use_chardet_on_py3 = ["chardet (>=3.0.2,<6)"]

[[package]]
name = "rope"
version = "1.7.0"
description = "a python refactoring library..."
category = "dev"
optional = false
python-versions = ">=3.7"

[package.dependencies]
pytoolconfig = {version = ">=1.2.2", extras = ["global"]}

[package.extras]
dev = ["pytest (>=7.0.1)", "pytest-timeout (>=2.1.0)", "build (>=0.7.0)", "pre-commit (>=2.20.0)"]
doc = ["pytoolconfig", "sphinx (>=4.5.0)", "sphinx-autodoc-typehints (>=1.18.1)", "sphinx-rtd-theme (>=1.0.0)"]

[[package]]
name = "sniffio"
version = "1.3.0"
description = "Sniff out which async library your code is running under"
category = "main"
optional = false
python-versions = ">=3.7"

[[package]]
name = "toml"
version = "0.10.2"
description = "Python Library for Tom's Obvious, Minimal Language"
category = "dev"
optional = false
python-versions = ">=2.6, !=3.0.*, !=3.1.*, !=3.2.*"

[[package]]
name = "tomli"
version = "2.0.1"
description = "A lil' TOML parser"
category = "dev"
optional = false
python-versions = ">=3.7"

[[package]]
name = "typing-extensions"
version = "3.10.0.2"
description = "Backported and Experimental Type Hints for Python 3.5+"
category = "main"
optional = false
python-versions = "*"

[[package]]
name = "ujson"
version = "5.7.0"
description = "Ultra fast JSON encoder and decoder for Python"
category = "dev"
optional = false
python-versions = ">=3.7"

[[package]]
name = "urllib3"
version = "1.26.14"
description = "HTTP library with thread-safe connection pooling, file post, and more."
category = "main"
optional = false
python-versions = ">=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*, !=3.5.*"

[package.extras]
brotli = ["brotlicffi (>=0.8.0)", "brotli (>=1.0.9)", "brotlipy (>=0.6.0)"]
secure = ["pyOpenSSL (>=0.14)", "cryptography (>=1.3.4)", "idna (>=2.0.0)", "certifi", "urllib3-secure-extra", "ipaddress"]
socks = ["PySocks (>=1.5.6,!=1.5.7,<2.0)"]

[[package]]
name = "werkzeug"
version = "2.2.2"
description = "The comprehensive WSGI web application library."
category = "main"
optional = false
python-versions = ">=3.7"

[package.dependencies]
MarkupSafe = ">=2.1.1"

[package.extras]
watchdog = ["watchdog"]

[[package]]
name = "whatthepatch"
version = "1.0.3"
description = "A patch parsing and application library."
category = "dev"
optional = false
python-versions = ">=3.7"

[[package]]
name = "yapf"
version = "0.32.0"
description = "A formatter for Python code."
category = "dev"
optional = false
python-versions = "*"

[[package]]
name = "yarl"
version = "1.8.2"
description = "Yet another URL library"
category = "main"
optional = false
python-versions = ">=3.7"

[package.dependencies]
idna = ">=2.0"
multidict = ">=4.0"

[metadata]
lock-version = "1.1"
python-versions = ">=3.10.0,<3.11"
content-hash = "cc2a85912252ce10278369453f46a05ad51c848ee54cedfb6c7cfe44beddd9a3"

[metadata.files]
aiohttp = []
aiosignal = []
anyio = []
argon2-cffi = []
argon2-cffi-bindings = []
async-timeout = []
attrs = []
certifi = []
cffi = []
charset-normalizer = []
click = []
colorama = []
cryptography = []
debugpy = []
flask = []
frozenlist = []
h11 = []
httpcore = []
httpx = []
idna = []
iso8601 = []
itsdangerous = []
jedi = []
jinja2 = []
markupsafe = []
multidict = []
numpy = []
packaging = []
parso = []
passlib = []
platformdirs = []
pluggy = []
protobuf = []
pycparser = []
pycryptodomex = []
pyflakes = []
pyseto = []
python-lsp-jsonrpc = []
pytoolconfig = []
replit = []
replit-python-lsp-server = []
requests = []
rope = []
sniffio = []
toml = []
tomli = []
typing-extensions = []
ujson = []
urllib3 = []
werkzeug = []
whatthepatch = []
yapf = []
yarl = []