#include <bits/stdc++.h>

using namespace std;

int DP[5][200][200][200];

int main() {

    for (int p = 2; p <= 4; ++p)
    for (int i = 0; i <= 100; ++i)
    for (int j = 0; j <= 100; ++j)
    for (int k = 0; k <= 100; ++k) {
        if (p < 4 && k > 0) continue;
        if (p < 3 && j > 0) continue;

        int val = DP[p][i][j][k];
        int tot = (i * 1 + j * 2 + k * 3) % p;
        if (tot == 0) val += 1;

        DP[p][i + 1][j][k] = max(DP[p][i + 1][j][k], val);
        DP[p][i][j + 1][k] = max(DP[p][i][j + 1][k], val);
        DP[p][i][j][k + 1] = max(DP[p][i][j][k + 1], val);
    }

    cerr << "Done precomp\n";

    int t; cin >> t;
    for (int tt = 1; tt <= t; ++tt) {
        vector<int> have(4, 0);
        int p, n; cin >> n >> p;

        while (n--) {
            int x; cin >> x;
            have[x % p] += 1;
        }

        cerr << have[0] << " " << have[1] << " " << have[2] << " " << have[3] << endl;
        cout << "Case #" << tt << ": " << have[0] + DP[p][have[1]][have[2]][have[3]] << endl;
        cerr << "Done case #" << tt << endl;
    }

    

    return 0;
}