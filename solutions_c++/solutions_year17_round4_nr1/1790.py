#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <string.h>
#include <stdio.h>
#include <math.h>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <cassert>

using namespace std;


const double eps = 1e-8;
const double pi = acos(-1.0);

const int N = 1005;

int g[N];
int cnt[10];

int main() {
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);

    int T;
    cin >> T;

    for (int cas = 1; cas <= T; cas++) {
        int n, p;
        cin >> n >> p;
        memset(cnt, 0, sizeof cnt);
        for (int i = 1; i <= n; i++) {
            cin >> g[i];
            g[i] %= p;
            cnt[g[i]]++;
        }
        int ans=n;
        if (p == 2) {
            ans = cnt[1] / 2;
        } else if (p == 3) {
            int mi = min(cnt[1], cnt[2]);
            ans = mi;
            cnt[1] = max(0, cnt[1] - mi);
            cnt[2] = max(0, cnt[2] - mi);
            ans += cnt[1] - (cnt[1]+2) / 3 + cnt[2] - (cnt[2]+2) / 3;
        }

        cout << "Case #" << cas << ": " << n - ans << endl;

    }
    return 0;
}

