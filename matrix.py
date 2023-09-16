def solve(matrix, row ,col):

    row_count = 0

    step = 1

    while row_count < row:

        col_count = 0

        check = True

        while check:

            if float(matrix[row_count][col_count]) == 0:

                col_count += 1

            else:

                check = False

        if row_count == col_count:

            jumper = 0

            if float(matrix[row_count][col_count]) != 1:

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

def main():

    print("====Welcome to Chase's Matrix Solver====\n")

    count = 0

    while count == 0:

        print('1) Solve Matrix(RREF)')

        print('2) Add Matrices')

        print('3) Subtract Matrices')

        print('4) Multiply Matrices')

        print('5) Exit\n')

        try:

            userChoice = int(input("What would you like to see?: "))

        except:

            userChoice = 0

        if userChoice < 5 and userChoice != 0:

            if userChoice == 1:

                matrix = []

                try:

                    row = int(input("Enter amount of rows: "))

                    col = int(input("Enter amount of columns: "))

                    if row > 1 and col > 1:

                        print("")

                        row_count = 0

                        while row_count < row:

                            new_row = input(f"Enter row {row_count + 1}: ")

                            new_row = new_row.split(",")

                            matrix.append(new_row)

                            row_count += 1

                        matrix = solve(matrix, row, col)

                        print('')

                        print('Final Answer:')

                        print_matrix(matrix, row, col)

                        zero_count = 0

                        for i in range(0, col - 2):

                            if matrix[row - 1][i] == 0:

                                zero_count += 1

                        if zero_count > col - 2:

                            print('\nThis is not a Linear Combination as the Matix is inconsistent')

                        print('')

                    else:

                        print("\nMatrices must have columns and rows greater than 1\n")

                except:

                    print("Try Again\n")

            elif userChoice == 2:

                m1 = []

                m2 = []

                try:

                    row = int(input('Enter amount of rows: '))

                    col = int(input('Enter amount of columns: '))

                    if row > 0 and col > 0:

                        print('')

                        row_count = 0

                        while row_count < row:

                            new_row = input(f"Enter row {row_count + 1} for Matrix 1: ")

                            new_row = new_row.split(",")

                            m1.append(new_row)

                            row_count += 1

                        row_count = 0

                        while row_count < row:

                            new_row = input(f"Enter row {row_count + 1} for Matrix 2: ")

                            new_row = new_row.split(",")

                            m2.append(new_row)

                            row_count += 1

                        matrix = add(m1, m2, row, col)

                        print('')

                        print('Final Answer:')

                        print_matrix(matrix,row,col,False)

                        print('')

                    else:

                        print('\nMatrices must have columns and rows greater than 0\n')

                except:

                    print('Try Again\n')

            elif userChoice == 3:

                m1 = []

                m2 = []

                try:

                    row = int(input('Enter amount of rows: '))

                    col = int(input('Enter amount of columns: '))

                    if row > 0 and col > 0:

                        print('')

                        row_count = 0

                        while row_count < row:

                            new_row = input(f"Enter row {row_count + 1} for Matrix 1: ")

                            new_row = new_row.split(",")

                            m1.append(new_row)

                            row_count += 1

                        row_count = 0

                        while row_count < row:

                            new_row = input(f"Enter row {row_count + 1} for Matrix 2: ")

                            new_row = new_row.split(",")

                            m2.append(new_row)

                            row_count += 1

                        matrix = subtract(m1, m2, row, col)

                        print('')

                        print('Final Answer:')

                        print_matrix(matrix,row,col,False)

                        print('')

                    else:

                        print('\nMatrices must have columns and rows greater than 0\n')

                except:

                    print('Try Again\n')

            else:

                m1 = []

                m2 = []

                try:

                    row1 = int(input("Enter amount of rows for Matrix 1: "))

                    col1 = int(input("Enter amount of columns for Matrix 1: "))

                    row2 = int(input("Enter amount of rows for Matrix 2: "))

                    col2 = int(input("Enter amount of columns for Matrix 2: "))

                    if (col1 == row2) and (row1 > 0) and (col1 > 0) and (row2 > 0) and (col2 > 0):

                        print('')

                        row_count = 0

                        while row_count < row1:

                            new_row = input(f"Enter row {row_count + 1} for Matrix 1: ")

                            new_row = new_row.split(",")

                            m1.append(new_row)

                            row_count += 1

                        row_count = 0

                        while row_count < row2:

                            new_row = input(f"Enter row {row_count + 1} for Matrix 2: ")

                            new_row = new_row.split(",")

                            m2.append(new_row)

                            row_count += 1

                        matrix = multiply(m1, m2, row1, col1, col2)

                        print('')

                        print('Final Answer:')

                        print_matrix(matrix,row1,col2,False)

                        print('')

                    else:

                        print('\nMatrices must have columns and rows greater than 0')

                        print("And to multiply Matrices, Matrix #1 number of columns must equal Matrix #2 number of rows\n")

                except:

                    print('Try Again\n')

        elif userChoice == 5:

            count = 1

            print('\nExiting...')

        else:

            print("Try Again\n")

main()