The program consist of three main functions empty() which finds the location of the empty space and do forward checking to only pass in the domain of each empty spaces.

valid() which checks if the number which is temporary placed already existy in the column, row, or the box, the whole division allows me to determine which small 3*3 matrix the empty space is in. This function is a validation function which the correct answer should not go through the if statements hence why it only returns false in this function.

The algor() is where the logic of the backtracking is located it first checks if there is still empty squares in the sudoku board, if there isn't any left the function will return True and end the backtracking else it would use the valid() function to check if the number in the domain will fit into the board and don't conflict, if it passes the test then it will update the empty value to the number desire and call the algor() function recursivly, if it doesn't find the desirable value it will revert the empty square value back to 0. This is my backtracking method. if all attemps are done and no possible answer is found it will return False.

The sudoku_solver() function runs the algor() and if it's True it will return the new sudoku board, else it will return a fail_board consisiting of -1.