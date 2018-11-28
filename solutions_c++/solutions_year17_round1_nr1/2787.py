#include <iostream>
#include <cmath>
#include <algorithm>
#include <cstring>

using namespace std;

int T, R, C;
char mat[12][12];
string str;

char checkAbove(int r, int c) {
    for (int j = r; j >= 0; j--) {
        if (mat[j][c] != '?') {
            return mat[j][c];
        }
    }
    return '.';
}

char checkBelow(int r, int c) {
    for (int j = r; j < R; j++) {
        if (mat[j][c] != '?') {
            return mat[j][c];
        }
    }
    return '.';
}

char checkRight(int r, int c) {
    for (int j = c; j < C; j++) {
        if (mat[r][j] != '?') {
            return mat[r][j];
        }
    }
    return '.';
}

void fillRight(int r, int c, char ch) {
    int j = c+1;
    while (mat[r][j] == '?') {
        mat[r][j] = ch;
        j++;
    }
}

int main() {
    cin >> T;
    for (int ca = 1; ca <= T; ca++) {
        cout << "Case #" << ca << ":" << endl;
        cin >> R >> C;
        int lowest = R;
        for (int i = 0; i < R; i++) {
            cin >> str;
            for (int j = 0; j < C; j++) {
                if (str.at(j) != '?') {
                    if (i < lowest) lowest = i;
                }
                mat[i][j] = str.at(j);
            }
        }
        for (int i = lowest; i < R; i++) {
            for (int j = 0; j < C; j++) {
                if (mat[i][j] != '?') {
                    fillRight(i, j, mat[i][j]);
                    continue;
                }
                char c = checkRight(i, j);
                if (c != '.') {
                    mat[i][j] = c;
                    fillRight(i, j, c);
                    continue;
                }
                char d = checkAbove(i, j);
                if (d != '.') {
                    mat[i][j] = d;
                    continue;
                }
                // char e = checkBelow(i, j);
                // if (e != '.') {
                //     mat[i][j] = e;
                //     continue;
                // }
            }
        }
        for (int i = 0; i < lowest; i++) {
            for (int j = 0; j < C; j++) {
                char e = checkBelow(i, j);
                if (e != '.') {
                    mat[i][j] = e;
                    continue;
                }
            }
        }
        for (int i = 0; i < R; i++) {
            for (int j = 0; j < C; j++) {
                cout << mat[i][j];
            }
            cout << endl;
        }


    }   

}