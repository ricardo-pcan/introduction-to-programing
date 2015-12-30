# The fibonacci succesion in recursevily form

def fibonacci( index ):
    if( index < 2 ):
        return index
    else:
        return fibonacci( index - 1 ) + fibonacci( index - 2 )

