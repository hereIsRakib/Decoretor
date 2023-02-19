def my_decoretor(func):
    def wrap_func():
        print('******')
        func()
        print('*******')

    return wrap_func


# @my_decoretor
def hello():
    print('Helloo')


a=my_decoretor(hello)
a()
# now using decoretor

@my_decoretor
def bye():
    print('Bye')

bye()
