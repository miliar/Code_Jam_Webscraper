#include<bits/stdc++.h>
using namespace std;

int T, R, C;
char maps[30][30];

int main() {
    cin >> T;
    for (int cases = 1; cases <= T; cases++) {
        cin >> R >> C;
        for (int j = 1; j <= R; j++) {
            for (int i = 1; i <= C; i++) {
                cin >> maps[i][j];
            }
        }

        //fill row
        for (int j = 1; j <= R; j++) {
            for (int i = 1; i <= C; i++) {
                if (maps[i][j] != '?') {
                    int ptr;

                    ptr = i - 1;
                    while (ptr > 0 && maps[ptr][j] == '?') {
                        maps[ptr][j] = maps[i][j];
                        ptr--;
                    }

                    ptr = i + 1;
                    while (ptr <= C && maps[ptr][j] == '?') {
                        maps[ptr][j] = maps[i][j];
                        ptr++;
                    }
                }
            }
        }

        //fill column
        for (int i = 1; i <= C; i++) {
            for (int j = 1; j <= R; j++) {
                if (maps[i][j] != '?') {
                    int ptr;

                    ptr = j - 1;
                    while (ptr > 0 && maps[i][ptr] == '?') {
                        maps[i][ptr] = maps[i][j];
                        ptr--;
                    }

                    ptr = j + 1;
                    while (ptr <= R && maps[i][ptr] == '?') {
                        maps[i][ptr] = maps[i][j];
                        ptr++;
                    }
                }
            }
        }

        cout << "Case #" << cases << ":\n";
        for (int j =1; j <= R; j++) {
            for (int i = 1; i <= C; i++)
                cout << maps[i][j];
            cout << endl;
        }
    }
}
