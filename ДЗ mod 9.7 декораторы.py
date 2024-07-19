
def is_prime(func):
    def wrapper(*args):
        original_result = func(*args)
        if original_result > 1:
            for i in range(2, int(original_result / 2) + 1):
                if (original_result % i) == 0:
                    print('составное')
                    break
            else:
                print('простое')
        else:
            print('составное')
        return original_result
    return wrapper

@is_prime
def sum_three(*args):
    res = 0
    for i in args:
        res += i
    return res

result = sum_three(2, 3, 6)
print(result)