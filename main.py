import ctypes

num = ctypes.c_long(10)
ptr = ctypes.pointer(num)

print(f"{num = }\n{num.value = }")
print(f"{ptr = }\n{ptr.contents = }\n{ptr.contents.value = }")
