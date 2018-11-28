#include <iostream>
#include <string.h>
#include <cstdio>
#include <set>
#include <vector>
#include <map>
#include <cmath>
using namespace std;
const int INF = 1<<30;
int Ac, Aj;
int C[1000], D[1000];
int J[1000], K[1000];

int dp[1500][1500][2][2];

int H[2000];

int rec(int l0, int l1, int h, int f) {
    int k = l0 + l1;
    //cout << k << " " << l0 << " " << l1 << endl;
    if (k == 1440) {
        return h == f ? 0 : 1;
    }
    if (dp[l0][l1][h][f] != -1) {
        return dp[l0][l1][h][f];
    }
    int c = H[k];
    // 0
    int r1 = INF;
    if (l0 + 1 <= 720 && c != 0) {
        r1 = rec(l0 + 1, l1, 0, f);
        if (r1 != INF) {
            r1 += (h == 0 ? 0 : 1);
        }
    }
    // 1
    int r2 = INF;
    if (l1 + 1 <= 720 && c != 1) {
        r2 = rec(l0, l1 + 1, 1, f);
        if (r2 != INF) {
            r2 += (h == 1 ? 0 : 1);
        }
    }
    return dp[l0][l1][h][f] = min(r1, r2);
}


void solve(int tst) {
    cin >> Ac >> Aj;
    for (int i = 0; i < Ac; ++i) {
        cin >> C[i] >> D[i];
    }
    for (int i = 0; i < Aj; ++i) {
        cin >> J[i] >> K[i];
    }
    memset(dp, -1, sizeof(dp));
    memset(H, -1, sizeof(H));
    for (int t = 0; t < 1440; ++t) {
        for (int i = 0; i < Ac; ++i) {
            if (C[i] <= t && t < D[i]) {
                H[t] = 0;
            }
        }
        for (int i = 0; i < Aj; ++i) {
            if (J[i] <= t && t < K[i]) {
                H[t] = 1;
            }
        }
    }
    int ans1 = rec(0, 0, 0, 0);
    int ans2 = rec(0, 0, 1, 1);
    int ans = min(ans1, ans2);
	printf("Case #%d: %d\n", tst, ans);
}

int main() {
	freopen("/Users/ryuzmukhametov/gcj/input.txt", "r", stdin);
	freopen("/Users/ryuzmukhametov/gcj/output.txt", "w", stdout);
	int tst;
	cin >> tst;
	for (int i = 1; i <= tst; ++i) {
		solve(i);
	}
	return 0;
}
