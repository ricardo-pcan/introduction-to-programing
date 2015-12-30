# Iterative function for fibonacci
def fibonacci( index ):
    prev = 1
    prev_prev = 0
    for n in range ( 0, index - 1 ):
        current = prev_prev + prev
        prev_prev = prev
        prev = current
    return prev_prev

print fibonacci( 5 )
