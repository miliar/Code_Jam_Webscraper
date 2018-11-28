#include<iostream>
using namespace std;
const int BUF = 30;


int row, col;
char b[BUF][BUF];

void read() {
    cin >> row >> col;
    for (int i = 0; i < row; ++i) {
        for (int j = 0; j < col; ++j) {
            cin >> b[i][j];
        }
    }
}


void work(int cases) {
    for (int c = 0; c < col; ++c) {
        int r = 0;
        while (r < row) {
            int nextR = r;
            while (nextR < row && b[nextR][c] == '?') {
                ++nextR;
            }
            
            if (nextR < row) {
                for (int rr = nextR - 1; rr >= 0 && b[rr][c] == '?'; b[rr][c] = b[nextR][c], --rr);
                for (int rr = nextR + 1; rr < row && b[rr][c] == '?'; b[rr][c] = b[nextR][c], ++rr);
            }

            r = nextR + 1;
        }
    }
    
    for (int r = 0; r < row; ++r) {
        int c = 0;
        while (c < col) {
            int nextC = c;
            while (nextC < col && b[r][nextC] == '?') {
                ++nextC;
            }
            
            if (nextC < col) {
                for (int cc = nextC - 1; cc >= 0 && b[r][cc] == '?'; b[r][cc] = b[r][nextC], --cc);
                for (int cc = nextC + 1; cc < col && b[r][cc] == '?'; b[r][cc] = b[r][nextC], ++cc);
            }

            c = nextC + 1;
        }
    }
    

    cout << "Case #" << cases << ":";
    cout << endl;
    for (int i = 0; i < row; ++i) {
        for (int j = 0; j < col; ++j) {
            cout << b[i][j];
        }
        cout << endl;
    }
}


int main() {
    int cases;
    cin >> cases;
    
    for (int i = 0; i < cases; ++i) {
        read();
        work(i + 1);
    }
    return 0;
}
