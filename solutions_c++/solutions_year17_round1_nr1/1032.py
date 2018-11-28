#include <bits/stdc++.h>

using namespace std;

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    int t;
    cin >> t;
    int r, c;
    char x[30][30];
    for (int i = 1; i <= t; i++) {
        cin >> r >> c;
        for (int j = 1; j <= r; j++) {
            for (int h = 1; h <= c; h++) cin >> x[j][h];
        }
        int count2 = 0;
        for (int j = 1; j <= r; j++) {
            int count = 0;
            for (int h = 1; h <= c; h++) {
                if (h > 1 && x[j][h - 1] != '?' && x[j][h] == '?') x[j][h] = x[j][h - 1];
                else if (x[j][h] == '?') count++;
                if (count == c) count2++;
            }
            for (int h = c; h >= 1; h--) {
                if (h < c && x[j][h + 1] != '?' && x[j][h] == '?') x[j][h] = x[j][h + 1];
            }
            if (count2 > 0 && x[j][1] != '?') {
                for(int p = 1; p <= count2; p++) {
                    for (int d = 1; d <= c; d++) x[j - p][d] = x[j][d];
                }
                count2 = 0;
            }
        }
        if (count2 > 0) {
            for (int q = 0; q < count2; q++) {
                for (int m = 1; m <= c; m++) x[r - q][m] = x[r - count2][m];
            }
        }
        cout << "Case #" << i << ":\n";
        for (int j = 1; j <= r; j++) {
            for (int h = 1; h <= c; h++) cout << x[j][h];
            cout << '\n';
        }
    }
    return 0;
}
