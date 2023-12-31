def solve(matrix, row, col):

    temp = []

    pointer = 0

    while len(matrix) != 0:

        for i in range(0, len(matrix)):

            for j in range(0, col):

                if j == pointer:

                    if float(matrix[i][j]) != 0:

                        count = 0

                        for k in range(0, len(temp)):

                            if matrix[i] == temp[k]:

                                count += 1

                        if count == 0:

                            for k in matrix:

                                if k == matrix[i]:

                                    temp.append(k)

                            pointer += 1

        for i in temp:

            for j in matrix:

                if i == j:

                    matrix.remove(i)

    matrix = temp

    print('\nRearrange Matrix:')

    print_matrix(matrix, row, col)

    row_count = 0

    step = 1

    while row_count < row:

        col_count = 0

        check = True

        while check:

            if col_count < col - 1:

                if float(matrix[row_count][col_count]) == 0:

                    col_count += 1

                else:

                    check = False

            else:

                check = False

        if row_count == col_count:

            jumper = 0

            if float(matrix[row_count][col_count]) != 1 and float(matrix[row_count][col_count]) != 0:

                divider = float(matrix[row_count][col_count])

                while jumper < col:

                    matrix[row_count][jumper] = float(matrix[row_count][jumper])/divider

                    jumper += 1

                print(f'\nStep {step}: R{row_count+1}/{round(divider, 2)}')

                step += 1

                print_matrix(matrix, row, col)

        next_row = 0

        while next_row < row:

            if next_row != row_count:
            
                if float(matrix[next_row][col_count]) != 0:

                    multiplier = float(matrix[next_row][col_count])

                    jumper = col_count

                    while jumper < col:

                        matrix[next_row][jumper] = float(matrix[next_row][jumper]) - (multiplier * float(matrix[row_count][jumper]))

                        jumper += 1

                    print(f'\nStep {step}: R{next_row+1}-(({round(multiplier, 2)})R{row_count+1})')

                    step += 1

                    print_matrix(matrix, row, col)

            next_row += 1

        row_count += 1

    new_matrix = []

    for i in range(0, row):

        temp = []

        for j in range(0, col):

            data = float(matrix[i][j])

            if data == -0:

                data = 0

            temp.append(data)

        new_matrix.append(temp)

    return new_matrix

def add(m1, m2, row, col):

    steps = []

    new_matrix = []

    for i in range(0, row):

        temp1 = []

        temp2 = []

        for j in range(0, col):

            temp1.append(float(m1[i][j]) + float(m2[i][j]))

            temp2.append(f'({str(m1[i][j])} + {str(m2[i][j])})')

        steps.append(temp2)

        new_matrix.append(temp1)

    print('\nThe Setup:')

    print_matrix(steps,row,col,False,True)

    return new_matrix

def subtract(m1, m2, row, col):

    steps = []

    new_matrix = []

    for i in range(0, row):

        temp1 = []

        temp2 = []

        for j in range(0, col):

            temp1.append(float(m1[i][j]) - float(m2[i][j]))

            temp2.append(f'({str(m1[i][j])} - {str(m2[i][j])})')

        steps.append(temp2)

        new_matrix.append(temp1)

    print('\nThe Setup:')

    print_matrix(steps,row,col,False,True)

    return new_matrix

def multiply(m1, m2, row1, col1, col2):

    steps = []

    new_matrix = []

    for i in range(0, row1):

        temp = []

        step_temp = []

        for j in range(0, col2):

            step = "("

            ans = 0

            for k in range(0,col1):

                data1 = str(m1[i][k])

                data2 = str(m2[k][j])

                if k == 0:

                    step = step + "(" + data1 + "*" + data2 + ")"

                else:

                    step = step + "+(" + data1 + "*" + data2 + ")"

                ans += (float(m1[i][k])*float(m2[k][j]))

            step_temp.append(step + ")")

            temp.append(ans)

        new_matrix.append(temp)

        steps.append(step_temp)

    print("\nThe Setup:")

    print_matrix(steps, row1, col2, False, True)

    return new_matrix

def determinant(matrix, display = None):

    if len(matrix) == 1:

        return float(matrix[0][0])

    det = 0

    for col in range(len(matrix)):

        sub = [row[:col] + row[col+1:] for row in matrix[1:]]

        subDet = determinant(sub, display)

        if display == None:

            display = f'[({(-1)**col})({float(matrix[0][col])})({subDet})]'

        else:

            display = display + f' + [({(-1)**col})({float(matrix[0][col])})({subDet})]'

        det += ((-1)**col)*float(matrix[0][col])*subDet

        print(f'\n{display}')

    return det

def inverse(matrix, row, col):

    if (row == 1) and (col == 1):

        return matrix

    new_matrix = []

    new_col = col * 2

    row_count = 0

    while row_count < row:

        temp = matrix[row_count]

        col_count = 0

        while col_count < col:

            if col_count == row_count:

                temp.append('1')

            else:

                temp.append('0')
                
            col_count += 1

        new_matrix.append(temp)

        row_count += 1

    print('\nThe Setup:')

    print_matrix(new_matrix, row, new_col, False)

    new_matrix = solve(new_matrix, row, new_col)

    return new_matrix

def transpose(matrix, row ,col):

    new_matrix = []

    for i in range(0, col):

        new_matrix.append([])

    for i in range(0, row):

        for j in range(0, col):

            new_matrix[j].append(matrix[i][j])

    return new_matrix

def print_matrix(matrix, row, col, solve = True, steps = False):

    if solve:

        for i in range(0, row):

            num_str = "|"

            for j in range(0, col):

                data = float(matrix[i][j])

                if j == 0:

                    num_str = num_str + str(round(data, 2))

                elif (j == col - 1):

                    num_str = num_str + "\t|" + str(round(data, 2)) 

                else:

                    num_str = num_str + "\t" + str(round(data, 2))

            print(num_str + "\t|")

    elif steps:

        for i in range(0, row):

            num_str = "|"

            for j in range(0, col):

                data = matrix[i][j]

                if j == 0:

                    num_str = num_str + data

                else:

                    num_str = num_str + "\t" + data

            print(num_str + "\t|")

    else:

        for i in range(0, row):

            num_str = "|"

            for j in range(0, col):

                data = float(matrix[i][j])

                if j == 0:

                    num_str = num_str + str(round(data, 2))

                else:

                    num_str = num_str + "\t" + str(round(data, 2))

            print(num_str + "\t|")

def eigval(matrix):

    b = -float(matrix[0][0])-float(matrix[1][1])

    print('\nFinding Determinant of matrix:')

    c = determinant(matrix)

    print('\nSolve for λ:')

    print(f'(λ^2)+({b}λ)+({c})')

    e1 = (-b + ((b**2)-(4*c))**(1/2))/2

    e2 = (-b - ((b**2)-(4*c))**(1/2))/2

    ev = [e1,e2]

    print(f'\nFound eigenvalues {ev[0]} and {ev[1]}')

    return ev

def eigvec(matrix,ev):

    m1 = [[float(matrix[0][0])-ev[0],float(matrix[0][1])],[float(matrix[1][0]),float(matrix[1][1])-ev[0]]]

    m2 = [[float(matrix[0][0])-ev[1],float(matrix[0][1])],[float(matrix[1][0]),float(matrix[1][1])-ev[1]]]

    print(f'\nSolving matrix, plugging in {round(ev[0],2)}:')

    m1 = solve(m1, 2, 2)

    print(f'\nSolving matrix, plugging in {round(ev[1],2)}:')

    m2 = solve(m2, 2, 2)

    evec = [[-m1[0][1],m1[0][0]],[-m2[0][1],m2[0][0]]]

    return evec

def userMatrix(row, col):

    matrix = []

    print("")

    row_count = 0

    while row_count < row:

        new_row = input(f"Enter row {row_count + 1}(Enter numbers comma separated with no spaces): ")

        new_row = new_row.split(",")

        if len(new_row) > col or len(new_row) < col:

            raise IndexError

        matrix.append(new_row)

        row_count += 1

    return matrix

def main():

    print("====Welcome to Chase's Matrix Solver====")

    count = 0

    while count == 0:

        print('\n1) Solve Matrix(RREF)')

        print('2) Add Matrices')

        print('3) Subtract Matrices')

        print('4) Multiply Matrices')

        print('5) Calculate the Determinant')

        print('6) Calculate the Inverse')

        print('7) Find the Transpose')

        print('8) Find Eigenvalues and Eigenvectors(only 2x2 currently)')

        print('9) Exit\n')

        try:

            userChoice = int(input("What would you like to see?: "))

        except:

            userChoice = 0

        if userChoice == 1:

            try:

                row = int(input("Enter amount of rows: "))

                col = int(input("Enter amount of columns: "))

                if row > 1 and col > 1:

                    matrix = userMatrix(row, col)

                    print('\nInputted Matrix:')

                    print_matrix(matrix, row, col)

                    matrix = solve(matrix, row, col)

                    print('\nFinal Answer:')

                    print_matrix(matrix, row, col)

                    zero_count = 0

                    for i in range(0, col - 1):

                        if matrix[row - 1][i] == 0:

                            zero_count += 1

                    if zero_count > col - 2 and (matrix[row-1][col-1] != 0):

                        print("\nHere I found the Matrix to be inconsistent")

                        print('This is also not a Linear Combination due to the inconsistency')

                    elif zero_count == col - 1:

                        print('\nHere I found the Matrix to have infinitely many solutions')

                        print('The value for a varaible could be any real number as 0 = 0 was found')

                else:

                    print("\nMatrices must have columns and rows greater than 1")

            except:

                print("\nYou may have typed something wrong. Please try again")

        elif userChoice == 2:

            try:

                row = int(input('Enter amount of rows: '))

                col = int(input('Enter amount of columns: '))

                if row > 0 and col > 0:

                    m1 = userMatrix(row, col)

                    print('\nInputted Matrix 1:')

                    print_matrix(m1, row, col, False)

                    m2 = userMatrix(row, col)

                    print('\nInputted Matrix 2:')

                    print_matrix(m2, row, col, False)

                    matrix = add(m1, m2, row, col)

                    print('')

                    print('Final Answer:')

                    print_matrix(matrix,row,col,False)

                else:

                    print('\nMatrices must have columns and rows greater than 0')

            except:

                print("\nYou may have typed something wrong. Please try again")

        elif userChoice == 3:

            try:

                row = int(input('Enter amount of rows: '))

                col = int(input('Enter amount of columns: '))

                if row > 0 and col > 0:

                    m1 = userMatrix(row, col)

                    print('\nInputted Matrix 1:')

                    print_matrix(m1, row, col, False)

                    m2 = userMatrix(row, col)

                    print('\nInputted Matrix 2:')

                    print_matrix(m2, row, col, False)

                    matrix = subtract(m1, m2, row, col)

                    print('')

                    print('Final Answer:')

                    print_matrix(matrix,row,col,False)

                else:

                    print('\nMatrices must have columns and rows greater than 0')

            except:

                print("\nYou may have typed something wrong. Please try again")

        elif userChoice == 4:

            try:

                row1 = int(input("Enter amount of rows for Matrix 1: "))

                col1 = int(input("Enter amount of columns for Matrix 1: "))

                row2 = int(input("Enter amount of rows for Matrix 2: "))

                col2 = int(input("Enter amount of columns for Matrix 2: "))

                if (col1 == row2) and (row1 > 0) and (col1 > 0) and (row2 > 0) and (col2 > 0):

                    m1 = userMatrix(row1, col1)

                    print('\nInputted Matrix 1:')

                    print_matrix(m1, row1, col1, False)

                    m2 = userMatrix(row2, col2)

                    print('\nInputted Matrix 2:')

                    print_matrix(m2, row2, col2, False)

                    matrix = multiply(m1, m2, row1, col1, col2)

                    print('')

                    print('Final Answer:')

                    print_matrix(matrix,row1,col2,False)

                else:

                    print('\nMatrices must have columns and rows greater than 0')

                    print("To multiply Matrices, Matrix #1 number of columns must equal Matrix #2 number of rows as well")

            except:

                print("\nYou may have typed something wrong. Please try again")

        elif userChoice == 5:

            try:

                row = int(input("Enter amount of rows: "))

                col = int(input("Enter amount of columns: "))

                if (row == col) and (row > 0) and (col > 0):

                    matrix = userMatrix(row, col)

                    print('\nInputted Matrix:')

                    print_matrix(matrix, row, col, False)

                    print('\nHere is my work:')

                    det = determinant(matrix)

                    print('\nFinal Answer:')

                    print(det)

                else:

                    print('\nThere is no determinant possible as the matrix is not a square matrix')

            except:

                print("\nYou may have typed something wrong. Please try again")

        elif userChoice == 6:

            try:

                row = int(input("Enter amount of rows: "))

                col = int(input("Enter amount of columns: "))

                if (row == col) and (row > 0) and (col > 0):

                    matrix = userMatrix(row, col)

                    print('\nInputted Matrix:')

                    print_matrix(matrix, row, col, False)

                    print('\nChecking determinant:')

                    det = determinant(matrix)

                    print(f'\nHere is the determiannt: {det}')

                    if det == 0:

                        print('\nSince the determinant is 0, there is no possible inverse')

                    else:

                        new_matrix = inverse(matrix, row, col)

                        final = []

                        if (row != 1) and (col != 1):

                            for i in range(0, row):

                                temp = []

                                for j in range(col, col*2):

                                    temp.append(new_matrix[i][j])

                                final.append(temp)

                        else:

                            final.append('1')

                        print('\nFinal Answer:')

                        print_matrix(final,row,col,False)

                else:

                    print('\nThere is no inverse possible as the matrix is not a square matrix')

            except:

                print("\nYou may have typed something wrong. Please try again")

        elif userChoice == 7:

            try:

                row = int(input("Enter amount of rows: "))

                col = int(input("Enter amount of columns: "))

                if (row > 0) and (col > 0):

                    matrix = userMatrix(row, col)

                    print('\nInputted Matrix:')

                    print_matrix(matrix, row, col, False)

                    final = transpose(matrix, row, col)

                    new_row = col

                    new_col = row

                    print('\nFinal Answer:')

                    print_matrix(final,new_row,new_col,False)

                else:

                    print('\nInvalid Row or Column Size')

            except:

                print("\nYou may have typed something wrong. Please try again") 

        elif userChoice == 8:

            try:

                matrix = userMatrix(2,2)

                print('\nInputted Matrix:')

                print_matrix(matrix, 2, 2, False)

                ev = eigval(matrix)

                evec = eigvec(matrix, ev)

                print('\nFinal Answer:')

                print(f'The Eigenvalues are {round(ev[0],2)} and {round(ev[1],2)}\n')

                print('Here are the Eigenvectors respectively:')

                print(f'|{round(evec[0][0],2)}\t|\t|{round(evec[1][0],2)}\t|')

                print(f'|{round(evec[0][1],2)}\t|\t|{round(evec[1][1],2)}\t|')

            except:

                print("\nYou may have typed something wrong. Please try again") 

                print('You may have inputted a matrix that retrieves imaginary numbers')

                print('I am not capable of solving this(yet)')
 

        elif userChoice == 9:

            count = 1

            print('\nExiting...')

        else:

            print("\nYou may have typed something wrong. Please try again")

main()