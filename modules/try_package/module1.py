import sys
import pack1

print("execute Module1")

# print(f"hello, I'm {__path__}")
print(f"hello, I'm {__name__}")
print(f"hello, I'm {__file__}")
print(f"hello, I import {pack1.__package__}")
print(f"This is sys module {sys.modules['pack1']}")


value = "module 1 special value"