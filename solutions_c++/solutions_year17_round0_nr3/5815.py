#include <bits/stdc++.h>

using namespace std;

const int MX_SZ = 1000 + 42;
const int INF = 1e+9 + 42;

void solve(int tst)
{
    cout << "Case #" << tst << ": ";
    int n, k;
    cin >> n >> k;
    set<int> ppl;
    ppl.insert(0);
    ppl.insert(n + 1);
    for (int i = 1; i <= k; ++i) {
        int best_mn = -INF, best_mx = -INF;
        int pos = INF;
        for (int j = 1; j <= n; ++j) {
            if (ppl.find(j) == ppl.end()) {
                auto it = ppl.lower_bound(j);
                int r = *it - j - 1;
                int l = j - *(--it) - 1;
                if (best_mn <= min(l, r)) {
                    if (best_mn == min(l, r)) {
                        if (best_mx < max(l, r)) {
                            best_mn = min(l, r);
                            best_mx = max(l, r);
                            pos = j;
                        }
                    } else {
                        best_mn = min(l, r);
                        best_mx = max(l, r);
                        pos = j;
                    }
                }
            }
        }
        ppl.insert(pos);
        if (i == k) {
            cout << best_mx << " " << best_mn << endl;
        }
    }
}

int main()
{
    ios_base::sync_with_stdio(false);
    freopen("C-small-1-attempt0.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    int t;
    cin >> t;
    for (int i = 1; i <= t; i++)
    {
        solve(i);
    }
}
