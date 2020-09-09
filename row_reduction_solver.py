import numpy as np

# example input
equation = [
    np.array([5, 1, 4, 8,  54]),
    np.array([6, 5, 2, 1,  21]),
    np.array([4, 2, -1, -1,  -4]),
    np.array([4, 2, -1, -1,  -10])
]

# exception class if there's no solution
class NoSolutionException(Exception):
    pass
# exception class if there's infinite solutions
class InfiniteSolutionException(Exception):
    pass

# a debugger printer
def _print_formatted_equation(equation):
    print('----Reduced----')
    for row in equation:
        print('│', end=' ')
        print(', '.join([str(e) for e in row[:-1]]), end=' | ')
        print(row[-1], end='')
        print(' │')
        
def reduce(equation):
    """
    reduce(equation: list[np.ndarray]) -> solutions: list
    if there's no solution, a `NoSolutionException` will be raised.
    if there's infinite solution, an `InfiniteSolutionException` will be raised.
    """
    # it is simplified enough to give solution
    if len(equation) == 1:
        return [float(equation[0][1]) / equation[0][0]]
    
    # find the first row where the first entery is not zero.
    # Thanks to Mr. Peter for reminding me of that :D
    index = 0
    while equation[index][0] == 0:
        index += 1
    reducer = equation[index]
    
    reduced_equation = []
    
    # reduce equation
    for row in equation[index+1:]:
        # find least common multiplier
        fctr = np.lcm.reduce([reducer[0], row[0]])
        # hence obtain the factor to multiply to get that value
        # so that we can eliminate one variable
        factor_reducer = fctr // reducer[0]
        factor_row = fctr // row[0]
        # calculate the row
        # thanks to numpy makd
        reduced_row = reducer * factor_reducer - row * factor_row
        # remove the first term (must be zero) in the reduced equation
        reduced_row = reduced_row[1:]

        # check for exceptions
        if not False in [0 == e for e in reduced_row[:-1]]:
            if 0 == reduced_row[-1]:
                # infinite solution
                raise InfiniteSolutionException()
            else:
                raise NoSolutionException()
            
        # add the reduced row to the equation
        reduced_equation.append(reduced_row)
    
    # _print_formatted_equation(reduced_equation)
    
    # form new solution from the solved ones
    solutions = reduce(reduced_equation)
    # to make the values match (because they come in reversed order)
    rev_solutions = [e for e in reversed(solutions)]

    # check for error
    if len(reducer[1:-1]) != len(solutions):
        raise ArithmeticError('Factor length mismatch.')
    
    index = 0
    constant_to_subtract = 0
    
    for factor in reducer[1:-1]:
        constant_to_subtract += factor * rev_solutions[index]
        index += 1
    new_solution = float(reducer[-1] - constant_to_subtract) / reducer[0]
    
    solutions.append(new_solution)
    return [e for e in reversed(solutions)]

# test run
print(reduce(equation))
