# Throw of dice

A simple routine that decodes the notation xDy+z or xDy-z, where 

    x is the number of dice, 
    y is the nnumber of walls of each dice 
    and z is a natural number which is added or subtracted from the result
    permitted numbers of walls: D3, D4, D6, D8, D10, D12, D20, D100

If the notation is incorrect an exception Incorrect_Notation is thrown.