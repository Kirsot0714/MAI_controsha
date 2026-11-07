def func_call_counter(func):
    qty_func_calls = {}

    def wrapper(a):
        func_hash = hash(func)
        if qty_func_calls.get(func_hash):
            qty_func_calls[func_hash] += 1
        else:
            qty_func_calls[func_hash] = 1
        print(f"The func '{func.__name__}' has been used {qty_func_calls[func_hash]}")
        return func(a)

    return wrapper


@func_call_counter
def just_func(n):
    return n**2


@func_call_counter
def just_func2(n):
    return n**3


for i in range(10):
    print(just_func(i))
    print(just_func2(i))
