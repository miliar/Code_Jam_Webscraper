#include<iostream>
#include<fstream>
#include<string>

using namespace std;

ifstream Inputfile;
ofstream Outputfile;

#define cin Inputfile
#define cout Outputfile

#define FILENAME "A-large"
#define FILENAME_IN FILENAME ".in"
#define FILENAME_OUT FILENAME ".out"

#define forab(i, a, b) for (int i = (int)(a); i <= (int)(b); ++i)
#define forba(i, a, b) for (int i = (int)(b); i >= (int)(a); --i)
#define for0n(i, n) forab (i, 0, n-1)
#define for1n(i, n) forab (i, 1, n)
#define forn0(i, n) forba (i, n-1, 0)
#define forn1(i, n) forba (i, n, 1)

void processT_row(char ipT[26][26], int R, int C, int r) {
    forab (c, 0, (C-1)) {
        if (ipT[r][c] != '?') {
            for (int cc = c - 1; ipT[r][cc] == '?' && cc >= 0; --cc) {
                ipT[r][cc] = ipT[r][c];
            }
            for (int cc = c + 1; ipT[r][cc] == '?' && cc < C; ++cc) {
                ipT[r][cc] = ipT[r][c];
            }
        }
    }
}

void processT_column(char ipT[26][26], int R, int C, int c) {
    forab (r, 0, (R-1)) {
        if (ipT[r][c] != '?') {
            for (int rr = r - 1; ipT[rr][c] == '?' && rr >= 0; --rr) {
                ipT[rr][c] = ipT[r][c];
            }
            for (int rr = r + 1; ipT[rr][c] == '?' && rr < R; ++rr) {
                ipT[rr][c] = ipT[r][c];
            }
        }
    }
}

void processT(char ipT[26][26], int R, int C) {
    forab (r, 0, (R-1)) {
        processT_row(ipT, R, C, r);
    }
    forab (c, 0, (C-1)) {
        processT_column(ipT, R, C, c);
    }
}

int main() {
    int T;
    char ipT[26][26];
    int R;
    int C;

    Inputfile.open(FILENAME_IN);
    Outputfile.open(FILENAME_OUT);
    cin >> T;
    for1n (i, T) {
        cin >> R >> C;
        forab (r, 0, (R-1)) {
            cin >> ipT[r];
        }

        processT(ipT, R, C);

        cout << "Case #" << i << ":" << endl;
        forab (r, 0, (R-1)) {
            cout << ipT[r] << endl;
        }
    }

    return 0;
}
