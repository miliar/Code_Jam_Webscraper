import os
import sys

KEY = 0;
PREV = 1;
MAX = 4;
X = 0;
O = 1;
T = -1;


def process_test_case(in_file):
    fi = open(in_file);
    test_case_count = int(fi.readline());
    for i in range(0, test_case_count):
        won_flag = False;
        won_type = "";
        blank_flag = False;
        row_flag = [];
        col_flag = [];
        diag_flag = [];
        for k in [0,1,2,3]:
            row_flag.append([False, False]);
            col_flag.append([False, False]);
        for k in [0, 1]:
            diag_flag.append([False, False]);
        incomplete_flag = False;
        row = 0;
        col = 0;
        for line in fi:
            if line.strip() == "":
                #######This is where we evaluate the test case 
                #If won is True 
                if not won_flag:
                    for col in col_flag:
                        if col[X] != col[O]:
                            if col[X] == True:
                                won_flag = True;
                                won_type = "X";
                                break;
                            else:
                                won_flag = True;
                                won_type = "O";
                                break;
                if not won_flag:
                    for diag in diag_flag:
                        if diag[X] != diag[O]:
                            if diag[X] == True:
                                won_flag = True;
                                won_type = "X";
                                break;
                            else:
                                won_flag = True;
                                won_type = "O";
                                break;
                        
                if won_flag:
                    print "Case #%d: %s won"%(i+1, won_type);
                else:
                    print "Case #%d: %s"%(i+1,("Draw", "Game has not completed")[incomplete_flag]);
                won_flag = False;
                won_type = "";
                blank_flag = False;
                ###resetting ecery thing
                for row in row_flag:
                    row[X] = False;
                    row[O]=  False;
                for col in col_flag:
                    col[X] = False;
                    col[O] = False;
                for diag in diag_flag:
                    diag[O] = False;
                    diag[X] = False;
                incomplete_flag = False;
                row = 0;
                col = 0;
                i += 1;
            
            elif not won_flag:
                ## cehck for row_vic
                col = 0;
                for char in line:
                    if char == "X":
                        row_flag[row][X] = True;
                        col_flag[col][X] = True;
                        if row ==  col or MAX-1-col == row:
                            diag_flag[row==col][X] = True;
                    elif char == "O":
                        row_flag[row][O] = True;
                        col_flag[col][O] = True;
                        if row ==  col or MAX-1-col == row:
                            diag_flag[row==col][O] = True;
                    elif char == ".":
                        incomplete_flag = True;
                        row_flag[row][X] = True;
                        row_flag[row][O] = True;
                        col_flag[col][O] = True;
                        col_flag[col][X] = True;
                        if row ==  col or MAX-1-col == row:
                            diag_flag[row==col] = [True, True];
                    col +=1
                if row_flag[row][X] != row_flag[row][O]:
                    if row_flag[row][X] == True:
                        won_flag = True;
                        won_type = "X";
                    else:
                        won_flag = True;
                        won_type = "O";
                row += 1;
        return

process_test_case(sys.argv[1]);
