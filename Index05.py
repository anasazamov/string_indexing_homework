def main(s):
    """
    Given a variable s string of length five. Determine the number of digits involved in this variable.
    Args:
        s(str): parameter
    Returns:
        int: answer
    """
    length=0
    for i in s:
        
        if i.isnumeric() :
            length+=1
    return length
print(main("sds54sadsa465xcs6546"))