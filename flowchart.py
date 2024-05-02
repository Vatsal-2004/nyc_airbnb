import import_ipynb

notebook = import_ipynb.notebook('airbnb.ipynb')
code = notebook.code

print(code)