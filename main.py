# Closure - what is it ?

def outer_func(name):
    # text = "Hello from outer_func function"
    text = name

    def inner_func():
        print(text)
    return inner_func


batman = outer_func("Bruce Wayne")
spiderman = outer_func("Peter Parker")

batman()
spiderman()
# print(batman)
# print(batman.__name__)
