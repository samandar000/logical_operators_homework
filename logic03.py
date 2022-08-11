def main(a,b):
    """
    Given two integers a, b,  check the following statement "Each of the numbers 'a' and 'b' is negative".
    Args:
        a(int): parameter a
        b(int): parameter b
    Returns:
        bool: answer
    """
    x1=a<0
    x2=b<0

    return x1 and x2 
print(main(-4,-4))

