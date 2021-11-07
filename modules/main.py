import os.path
import types
import sys

module_name = "module1"
module_file = "mdl1_src.py"
module_path = "."

module_rel_file_path = os.path.join(module_path, module_file)
module_abs_file_path = os.path.abspath(module_rel_file_path)

# Read source code
with open(module_rel_file_path, 'r') as code_file:
    src_code = code_file.read()

mod = types.ModuleType(module_name)
mod.__file__ = module_abs_file_path

#set a ref in sys.modules
sys.modules[module_name] = mod

# compile
code = compile(src_code, filename=module_abs_file_path, mode="exec")
print(code)
# execute source code
exec(code, mod.__dict__)

mod.hello()