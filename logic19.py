def main(x):
    """
    Given an integer x, return true if x is palindrome integer.
    An integer is a palindrome when it reads the same backward as forward.

    Args:
        x(int): parameter x
    Returns:
        bool: answer
    """
    x > 9 and x < 1000
    x1= x%10
    x //= 10

    x2 = x%10
    x//=10

    x3 = x%10
    x //= 10
   
     
    print ( x1 == x2 or x1 == x3 )

main(11)