#include <cstdlib>
#include <iostream>

using namespace std;

const int R_MAX = 25;
const int C_MAX = 25;

char matrix[R_MAX][C_MAX];

bool search(char matrix[][C_MAX], int R, int C, int &r, int &c) {
    for(; r < R; ++r) {
        for(; c < C; ++c) {
            if(matrix[r][c] != '?') {
                return true;
            }
        }
        
        c = 0;
    }
    
    return false;
}

long solve(char matrix[][C_MAX], int R, int C) {
    int r = 0;
    int c = 0;
    int ch;
    while(search(matrix, R, C, r, c)) {
        if(c >= C) {
            break;
        }
        
        ch = matrix[r][c];
        for(int j = c - 1; j >= 0 && matrix[r][j] == '?'; --j) {
            matrix[r][j] = ch;
        }
        for(c += 1; c < C && matrix[r][c] == '?'; ++c) {
            matrix[r][c] = ch;
        }
        
        if(c >= C) {
            ++r;
            c = 0;
        }
    }
    
    r = c = 0;
    while(search(matrix, R, C, r, c)) {
        if(c >= C) {
            break;
        }
        
        ch = matrix[r][c];
        for(int i = r - 1; i >= 0 && matrix[i][c] == '?'; --i) {
            matrix[i][c] = ch;
        }
        for(int i = r + 1; i < R && matrix[i][c] == '?'; ++i) {
            matrix[i][c] = ch;
        }
        
        ++c;
        if(c >= C) {
            ++r;
            c = 0;
        }
    }
}

int main(int argc, char** argv) {
    int T;
    cin >> T;
    
    int R, C;
    bool already_solved = true;
    char ch;
    for(int i = 1; i <= T; ++i) {
        cin >> R >> C;
        for(int r = 0; r < R; ++r) {
            for(int c = 0; c < C; ++c) {
                cin >> ch;
                if(ch == '?') {
                    already_solved = false;
                }
                else if(ch == '\n') {
                    cin >> ch;
                }
                
                matrix[r][c] = ch;
            }
        }
        
        cout << "Case #" << i << ":\n";
        if(!already_solved) {
            solve(matrix, R, C);
        }
        for(int r = 0; r < R; ++r) {
            for(int c = 0; c < C; ++c) {
                cout << matrix[r][c];
            }
            cout << "\n";
        }
    }
    
    return 0;
}
