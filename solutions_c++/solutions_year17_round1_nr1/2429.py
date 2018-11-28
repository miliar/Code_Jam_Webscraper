#include<iostream>
#include<string>
#include <queue>
#include <fstream>

using namespace std;

int main() {
    ofstream cop("op1.txt");
    ifstream cinp("in1.txt", ios::binary);
    int T, t=1;
    cinp >> T;
    for(;t <= T;t++){
        fflush(stdin);
        int R, C;
        cinp >> R >> C;
        string grid[R];
        for(int i=0;i<R;i++)
            cinp >> grid[i];
        int last_filled_row = -1, last_filled_col = -1;
        char last_filled_char;
        for(int i=0;i<R;i++) {
            fflush(stdout);
            last_filled_char = 0;
            for(int j=0; j<C;j++) {
                if(grid[i][j] != '?') {
                    int start_col = 0, start_row = 0;
                    if(last_filled_col != -1)
                        start_col = last_filled_col + 1;
                    if(last_filled_row != -1 )
                        start_row = last_filled_row + 1;
                    for(int st_col = start_col; st_col <= j; st_col++) {
                        for(int st_row = start_row; st_row <= i; st_row++) {
                            grid[st_row][st_col] = grid[i][j];
                        }
                    }
                    last_filled_col = j;
                    last_filled_char = grid[i][j];
                }
            }
            if(last_filled_char != 0 && grid[i][C-1] == '?') {
                int start_col = 0, start_row = 0;
                if(last_filled_col != -1)
                    start_col = last_filled_col + 1;
                if(last_filled_row != -1 )
                    start_row = last_filled_row + 1;
                for(int st_col = start_col; st_col < C; st_col++) {
                    for(int st_row = start_row; st_row <= i; st_row++) {
                        grid[st_row][st_col] = last_filled_char;
                    }
                }
            }
            if(grid[i][C-1] != '?') {
                last_filled_col = -1;
                last_filled_row = i;
            }
        }
        if(grid[R-1][C-1] == '?') {
            for(int st_row = last_filled_row + 1; st_row < R; st_row++) {
                for(int st_col = 0; st_col < C; st_col++) {
                    grid[st_row][st_col]  = grid[st_row-1][st_col];
                }
            }
        }
        cop << "Case #" << t << ":" << endl;
        for(int i=0;i<R;i++)
            cop << grid[i] << endl;
    }
}
