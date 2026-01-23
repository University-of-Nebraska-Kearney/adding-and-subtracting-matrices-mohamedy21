# Create your own code here

# Main method to run program
def main():
    matrix1 = get_matrix()
    matrix2 = get_matrix()
    final_matrix = add_matrix(matrix1, matrix2)
    print("\nFinal Matrix: ")
    print(final_matrix)


# Begin by asking the user for the number of rows and collumns wanted in the matrix
# Then ask the user to input the number for each specific row and collumn
# Each time an input is taken it is appended to the list and then returned once completed
def get_matrix(): 
    matrix = []
    num_rows = input("Please enter the number of rows for your matrix: ")
    num_cols = input("Please enter the number of columns for your matrix: ")
    print("Matrix size is: " + str(num_cols) + "x" + str(num_rows))
    for i in range(int(num_rows)):
        matrix.append([])
        for j in range(int(num_cols)):
            input_number = input("\nPlease enter a number for row " + str((i+1)) 
                                       + " column " + str((j+1)) + ": " )
            matrix[i].append(input_number)
    print("\nCompleted Matrix: ")
    print(matrix)
    return matrix


# First check the number of lists within the matrices matchup
# Then check the number of elements within the first list of each matrix are the same 
# Since the number of elements in each list was already predetermined we do not need to check each individual list to ensure that they are the same size
# After confirming, create loops to add a list for each new row and then add the two matrices to its position into the new empty list and return
def add_matrix(matrix1, matrix2):
    added_matrix = []
    if len(matrix1) == len(matrix2) and len(matrix1[0]) == len(matrix2[0]):
        print("Adding Matrix......")
        for i in range(len(matrix1)):
            added_matrix.append([])
            for j in range(len(matrix1[0])):
                added_matrix[i].append(int(matrix1[i][j]) + int(matrix2[i][j]))
    else:
        print("Not able to add")
    return added_matrix



if __name__ == "__main__":
    main()