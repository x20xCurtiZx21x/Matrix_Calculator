def solve(matrix, row, col):

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

                print(f'\nStep {step}: R{row_count+1}/{divider}')

                step += 1

                for i in range(0, row):

                    num_str = "|"

                    for j in range(0, col):

                        data = float(matrix[i][j])

                        if j == 0:

                            num_str = num_str + str(round(data, 2))

                        elif j == col - 1:

                            num_str = num_str + "\t|" + str(round(data, 2)) + "\t|"

                        else:

                            num_str = num_str + "\t" + str(round(data, 2))

                    print(num_str)

        next_row = 0

        while next_row < row:

            if next_row != row_count:
            
                if float(matrix[next_row][col_count]) != 0:

                    multiplier = float(matrix[next_row][col_count])

                    jumper = col_count

                    while jumper < col:

                        matrix[next_row][jumper] = float(matrix[next_row][jumper]) - (multiplier * float(matrix[row_count][jumper]))

                        jumper += 1

                    print(f'\nStep {step}: R{next_row+1}-({multiplier}R{row_count+1})')

                    step += 1

                    for i in range(0, row):

                        num_str = "|"

                        for j in range(0, col):

                            data = float(matrix[i][j])

                            if j == 0:

                                num_str = num_str + str(round(data, 2))

                            elif j == col - 1:

                                num_str = num_str + "\t|" + str(round(data, 2)) + "\t|"

                            else:

                                num_str = num_str + "\t" + str(round(data, 2))

                        print(num_str)

            next_row += 1

        row_count += 1

    new_matrix = []

    for i in range(0, row):

        temp = []

        for j in range(0, col):

            data = float(matrix[i][j])

            if data == -0:

                dat = 0

            temp.append(data)

        new_matrix.append(temp)

    return new_matrix

def main():

    print("====Welcome to Chase's Matrix Solver====\n")

    count = 0

    while count == 0:

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

                for i in range(0, row):

                    num_str = "|"

                    for j in range(0, col):

                        data = float(matrix[i][j])

                        if j == 0:

                            num_str = num_str + str(round(data, 2))

                        elif j == col - 1:

                            num_str = num_str + "\t|" + str(round(data, 2)) + "\t|"

                        else:

                            num_str = num_str + "\t" + str(round(data, 2))

                    print(num_str)

                zero_count = 0

                for i in range(0, col - 2):

                    if matrix[row - 1][i] == 0:

                        zero_count += 1

                if zero_count > col - 2:

                    print('\nThis is not a Linear Combination as the Matix is inconsistent')

                print('')

                choice = input("Solve another matrix?(Y/N): ")

                if choice.lower() == 'n':

                    count = 1

            else:

                print("Try Again\n")

        except:

            print("Try Again\n")

main()