#include <iostream>
#include <string>
#include <vector>
using namespace std;

int main() {
    long T, R, C;
    cin >> T;
    for (long t = 1; t <= T; t++) {
        cin >> R >> C;
        vector<string> G(R);
        for (long i = 0; i < R; i++) cin >> G[i];

        for (long i = 0; i < R; i++) {
            char last = '?';
            for (long j = 0; j < C; j++) {
                if (G[i][j] == '?') {
                    G[i][j] = last;
                } else if (last == '?') {
                    for (long jj = 0; jj < j; jj++) G[i][jj] = G[i][j];
                }
                last = G[i][j];
            }
        }
        string lst = "?";
        for (long i = 0; i < R; i++) {
            if (G[i][0] == '?') {
                G[i] = lst;
            } else if (lst[0] == '?') {
                for (long ii = 0; ii < i; ii++) G[ii] = G[i];
            }
            lst = G[i];
        }

        cout << "Case #" << t << ": " << endl;
        for (long i = 0; i < R; i++) {
            for (long j = 0; j < C; j++) {
                cout << G[i][j];
            }
            cout << endl;
        }
    }
}
