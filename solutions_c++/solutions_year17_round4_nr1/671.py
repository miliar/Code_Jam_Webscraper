#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

int buf[101][101][101][4];

int dp(int P, int a1, int a2, int a3, int r) {
    if (buf[a1][a2][a3][r] >= 0) {
        return buf[a1][a2][a3][r];
    }
    int best = 0;
    if (a1 > 0) {
        best = max(best, dp(P, a1 - 1, a2, a3, (r + 1) % P));
    }
    if (a2 > 0) {
        best = max(best, dp(P, a1, a2 - 1, a3, (r + 2) % P));
    }
    if (a3 > 0) {
        best = max(best, dp(P, a1, a2, a3 - 1, (r + 3) % P));
    }
    if (r > 0) {
        buf[a1][a2][a3][r] = best;
    } else {
        buf[a1][a2][a3][r] = 1 + best;
    }
    return buf[a1][a2][a3][r];
}

int doit() {
    int N, P;
    cin >> N >> P;
    int k[4];
    for (int i = 0; i < 4; i++) {
        k[i] = 0;
    }
    vector <int> G;
    for (int i = 0; i < N; i++) {
        int g;
        cin >> g;
        k[g % P]++;
    }
    for (int i = 0; i < 101; i++) {
        for (int j = 0; j < 101; j++) {
            for (int k = 0; k < 101; k++) {
                for (int r = 0; r < 4; r++) {
                    buf[i][j][k][r] = -1;
                }
            }
        }
    }
    buf[0][0][0][0] = 0;
    buf[0][0][0][1] = 0;
    buf[0][0][0][2] = 0;
    buf[0][0][0][3] = 0;
    return dp(P, k[1], k[2], k[3], 0) + k[0];
}

int main(int argc, char *argv[]) {
    int C;
    cin >> C;
    for (int i = 1; i <= C; i++) {
        int res = doit();
        cout << "Case #" << i << ": " << res << endl;
    }
    return 0;
}
