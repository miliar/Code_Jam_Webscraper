#include<iostream>

using namespace std;

const int N = 33;
char g[N][N];
int seen[256];

int check(int x0, int y0, int x1, int y1, int target) {
    int count = 0;
    for (int i = x0; i <= x1; i++) {
        for (int j = y0; j <= y1; j++) {
            if (g[i][j] != '?') count++;
            if (count > target) break;
        }
    }

    return count == target;
}

void fill(int x0, int y0, int x1, int y1, char c) {
    for (int i = x0; i <= x1; i++) {
        for (int j = y0; j <= y1; j++) {
            g[i][j] = c;
        }
    }
}

int main() {
    int T; cin >> T;
    for (int tt = 1; tt <= T; tt++) {
        cout << "Case #" << tt << ":\n";
    
    int R, C; cin >> R >> C;

    // cout << R << ' ' << C << endl;

    for (int i = 0; i < R; i++) {
        for (int j = 0; j < C; j++) {
            cin >> g[i][j];
        }
    }
    // for (int i = 0; i < R; i++) {
    //     for (int j = 0; j < C; j++) {
    //         cout << g[i][j];
    //     }
    //     cout << endl;
    // }
    for (int i = 0; i < 256; i++) seen[i] = 0;

    for (int i = 0; i < R; i++) {
        for (int j = 0; j < C; j++) {
            char c = g[i][j];
            if (c != '?' && !seen[c]) {
                seen[c] = 1;

                // find topleft
                int RMin = 0, CMin = 0;
                int found = 0;
                for (; RMin <= i;) {
                    // cout << RMin << ' ' << CMin << ' ' << i << ' ' << j << endl;

                    for (CMin = 0; CMin <= j; CMin++) {
                        // check ?
                        if (check(RMin, CMin, i, j, 1)) {
                            fill(RMin, CMin, i, j, c);
                            found = 1;
                            break;
                        }
                    }
                    if (found) break;

                    if (RMin < i) RMin++;
                }
                if (CMin > j) CMin = j;
                if (RMin > i) RMin = i;
                // cout << c << ' ' << RMin << ' ' << CMin << endl;

                // cout << c << " RC " << RMin << " " << CMin << endl;

                int CMax = j;
                while (1) {
                    if (CMax == C - 1) break;

                    // try CMax + 1
                    if (check(RMin, CMax + 1, i, CMax + 1, 0)) {
                        fill(RMin, CMax + 1, i, CMax + 1, c);
                        CMax++;
                        // cout << "CMax " << CMax << endl;

                    } else {
                        break;
                    }
                }

                // check below
                int RMax = i;
                while (1) {
                    if (RMax == R - 1) break;
                    if (check(RMax + 1, CMin, RMax + 1, CMax, 0)) {
                        fill(RMax + 1, CMin, RMax + 1, CMax, c);
                        RMax++;
                        // cout << "RMax " << RMax << endl;

                    } else {
                        break;
                    }
                }                

            }

            // cout << "ij " << i << ' ' << j << endl;
        }
    }



    for (int i = 0; i < R; i++) {
        for (int j = 0; j < C; j++) {
            cout << g[i][j];
        }
        cout << endl;
    }
}

}