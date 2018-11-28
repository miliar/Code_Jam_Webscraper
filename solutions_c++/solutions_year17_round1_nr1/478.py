#include <iostream>
#include <fstream>

using namespace std;

int main(){
    ifstream fin("A-large.in");
    ofstream fout("A-large.out");
    int T; fin >> T;
    for(int t = 1; t <= T; t++){
        fout << "Case #" << t << ":\n";
        int R, C; fin >> R >> C;
        char grid[R][C];
        for(int r = 0; r < R; r++){
            for(int c = 0; c < C; c++){
                fin >> grid[r][c];
            }
        }
        for(int r = 0; r < R; r++){
            char cur = '?';
            for(int c = 0; c < C; c++){
                if(grid[r][c] == '?'){
                    if(cur != '?'){
                        grid[r][c] = cur;
                    }
                }else{
                    if(cur == '?'){
                        for(int dc = 0; dc < c; dc++){
                            grid[r][dc] = grid[r][c];
                        }
                    }
                    cur = grid[r][c];
                }
            }
        }
        for(int r = 0; r < R; r++){
            for(int c = 0; c < C; c++){
                if(grid[r][c] == '?'){
                    if(r == 0){
                        grid[r][c] = grid[r+1][c];
                    }else{
                        grid[r][c] = grid[r-1][c];
                    }
                }
            }
        }
        for(int r = R-2; r >= 0; r--){
            for(int c = 0; c < C; c++){
                if(grid[r][c] == '?'){
                    grid[r][c] = grid[r+1][c];
                }
            }
        }
        for(int r = 0; r < R; r++){
            for(int c = 0; c < C; c++){
                fout << grid[r][c];
            }
            fout << "\n";
        }

    }
    fin.close();
    fout.close();
    return 0;
}
