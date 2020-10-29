
def check(array):
    val = [1,2,3,4,5,6,7,8,9]
    array.sort()
    if val == array:
        res = True
    else:
        res = False
      
    return res


def check_raws(table):
    for i in range(9):
        if(check(table[i]) == False):
            return False
    
    return True
        
    
def check_columns(table):
    
    for i in range(9):
        column = []
        for j in range(9):
            column.append(table[i][j])
        
        if(check(column) == False):
            return False
    
    return True




def check_squares(table):
    val =[0,3,6]
    for m in val:
        
        for n in val:
            square = []
            for i in range(3):
                for k in range (m,m+3):
                    square.append(table[i+n][k])
            print(square)        
            if ( check(square)== False):
                 return False
        
    return True


table= [
  [5, 3, 4, 6, 7, 8, 9, 1, 2],
  [6, 7, 2, 1, 9, 5, 3, 4, 8],
  [1, 9, 8, 3, 4, 2, 5, 6, 7],
  [8, 5, 9, 7, 6, 1, 4, 2, 3],
  [4, 2, 6, 8, 5, 3, 7, 9, 1],
  [7, 1, 3, 9, 2, 4, 8, 5, 6],
  [9, 6, 1, 5, 3, 7, 2, 8, 4],
  [2, 8, 7, 4, 1, 9, 6, 3, 5],
  [3, 4, 5, 2, 8, 6, 1, 7, 9]
]
    
check_squares(table)


def valid_solution(table):
    return(check_squares(table) and check_columns(table) and check_raws(table))


"""
    validSolution([
  [5, 3, 4, 6, 7, 8, 9, 1, 2],
  [6, 7, 2, 1, 9, 5, 3, 4, 8],
  [1, 9, 8, 3, 4, 2, 5, 6, 7],
  [8, 5, 9, 7, 6, 1, 4, 2, 3],
  [4, 2, 6, 8, 5, 3, 7, 9, 1],
  [7, 1, 3, 9, 2, 4, 8, 5, 6],
  [9, 6, 1, 5, 3, 7, 2, 8, 4],
  [2, 8, 7, 4, 1, 9, 6, 3, 5],
  [3, 4, 5, 2, 8, 6, 1, 7, 9]
]); // => true
    """
    