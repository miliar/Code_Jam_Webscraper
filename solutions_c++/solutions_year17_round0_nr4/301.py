#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <utility>

using namespace std;

struct placement { char k; int r; int c;
placement(char ik, int ir, int ic) : k(ik), r(ir), c(ic) {}
};

void doit() {
    int N, M;
    cin >> N >> M;

    vector<char> rowdat(N, false), coldat(N, false), diag1dat(N*2+1, false), diag2dat(N*2+1, false);
    vector<char> board(N*N, '.');
    vector<placement> result;

    for (int i = 0; i < M; ++i) {
        string ts;
        char t;
        int r, c;
        cin >> ts >> r >> c;
        t = ts[0];
        r--;
        c--;
        board[r*N + c] = t;
        if (t == '+' || t == 'o') {
            if (diag1dat[r+c] == true) {
                cerr << "diagdat1dat[" << r << "+" << c << "] was already true!!!" << endl;
            }
            diag1dat[r+c] = true;
            if (diag2dat[r - c + N - 1] == true) {
                cerr << "diag2dat for " << r << ", " << c << " was already true!!!" << endl;
            }
            diag2dat[r-c+N-1] = true;
        }
        if (t == 'x' || t == 'o') {
            if (rowdat[r] == true) {
                cerr << "rowdat[" << r << "] was already true!!!" << endl;
            }
            if (coldat[c] == true) {
                cerr << "coldat[" << c << "] was already true!!!" << endl;
            }
            rowdat[r] = true;
            coldat[c] = true;
        }
    }

    for (int k = 0; k <= N/2; ++k) {
        for (int i = 0; i < N; ++i) {
            for (int j = 0; j < N; ++j) {
                if (!(i == k || i == N-k-1 || j == k || j == N-k-1)) {
                    continue;
                }
                switch (board[i*N+j]) {
                    case 'o':
                        break;
                    case 'x':
                        if (diag1dat[i+j] == false && diag2dat[i - j + N - 1] == false) {
                            board[i*N+j] = 'o';
                            result.push_back(placement('o', i, j));
                            diag1dat[i+j] = true;
                            diag2dat[i - j + N -1] = true;
                        }
                        break;
                    case '+':
                        if (rowdat[i] == false && coldat[j] == false) {
                            board[i*N+j] = 'o';
                            result.push_back(placement('o', i, j));
                            rowdat[i] = true;
                            coldat[j] = true;
                        }
                        break;
                    case '.':
                        if (diag1dat[i+j] == false && diag2dat[i - j + N - 1] == false && rowdat[i] == false && coldat[j] == false) {
                            board[i*N+j] = 'o';
                            result.push_back(placement('o', i, j));
                            diag1dat[i+j] = true;
                            diag2dat[i - j + N -1] = true;
                            rowdat[i] = true;
                            coldat[j] = true;
                        }
                        else if (diag1dat[i+j] == false && diag2dat[i - j + N - 1] == false) {
                            board[i*N+j] = '+';
                            result.push_back(placement('+', i, j));
                            diag1dat[i+j] = true;
                            diag2dat[i - j + N -1] = true;
                        }
                        else if (rowdat[i] == false && coldat[j] == false) {
                            board[i*N+j] = 'x';
                            result.push_back(placement('x', i, j));
                            rowdat[i] = true;
                            coldat[j] = true;
                        }
                        break;
                }
            }
        }
    }

    int score = 0;
    for (int i = 0; i < N*N; ++i) {
        if (board[i] == 'x' || board[i] == '+') score++;
        else if (board[i] == 'o') score += 2;
    }
    cout << score << ' '  << result.size() << endl;
    for (auto pl : result) {
        cout << pl.k << ' '  << pl.r + 1 << ' ' << pl.c + 1 << endl;
    }
    //cerr << endl;
    //for (int i = 0; i < N; ++i) {
    //    for (int j = 0; j < N; ++j) {
    //        cerr << board[i*N+j];
    //    }
    //    cerr << endl;
    //}
}

int main() {
    int t;
    cin >> t;
    for (int i = 1; i <= t; ++i) {
        cout << "Case #" << i << ": ";
        doit();
    }
    return 0;
}
