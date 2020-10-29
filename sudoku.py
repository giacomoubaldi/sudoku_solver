
def check(array):
    """ This function takes an array and compares it with the fixed one a=[1,2,3,4,5,6,7,8,9]
    """
    val = [1,2,3,4,5,6,7,8,9]
    array.sort()
    if val == array:
        res = True
    else:
        res = False
      
    return res



def check_raws(table):
    """This function takes from a 2D array each raw and check if it is a fixed array a=[1,2,3,4,5,6,7,8,9]
    """
    for i in range(9):
        if(check(table[i]) == False):
            return False
    
    return True
        
    
def check_columns(table):
    """This function takes from a 2D array each column and check if it is a fixed array a=[1,2,3,4,5,6,7,8,9]
    """
    
    for i in range(9):
        column = []
        for j in range(9):
            column.append(table[i][j])
        
        if(check(column) == False):
            return False
    
    return True




def check_squares(table):
    """This function takes from a each 3x3 matrix an array and check if it is a fixed array a=[1,2,3,4,5,6,7,8,9]
    """
    val =[0,3,6]
    for m in val:
        
        for n in val:
            square = []
            for i in range(3):
                for k in range (m,m+3):
                    square.append(table[i+n][k])
                    
            if ( check(square)== False):
                 return False
        
    return True




def valid_solution(table):
    """This function asserts if a sudoku is correct or not, according to the rules"""
    if (check_squares(table) and check_columns(table) and check_raws(table)) == True:
        return("Finished!")
    else:
        return("'Try again!'")


es = [[1, 3, 2, 4, 9, 8, 7, 5, 6],
[6, 4, 3, 5, 2, 1, 9, 8, 7],
[2, 1, 4, 3, 6, 5, 8, 7, 9],
[5, 7, 9, 2, 6, 1, 3, 8, 4],
[1, 5, 8, 7, 9, 3, 4, 2, 6],
[9, 3, 5, 8, 1, 7, 6, 4, 2],
[4, 6, 8, 3, 7, 5, 2, 1, 9],
[7, 9, 2, 8, 4, 6, 5, 3, 1],
[6, 8, 7, 9, 2, 4, 1, 3, 5]]

es2= [[1, 3, 2, 5, 7, 9, 4, 6, 8]
     ,[4, 9, 8, 2, 6, 1, 3, 7, 5]
     ,[7, 5, 6, 3, 8, 4, 2, 1, 9]
     ,[6, 4, 3, 1, 5, 8, 7, 9, 2]
     ,[5, 2, 1, 7, 9, 3, 8, 4, 6]
     ,[9, 8, 7, 4, 2, 6, 5, 3, 1]
     ,[2, 1, 4, 9, 3, 5, 6, 8, 7]
     ,[3, 6, 5, 8, 1, 7, 9, 2, 4]
     ,[8, 7, 9, 6, 4, 2, 1, 3, 5]]


valid_solution(es2)
    