#include <bits/stdc++.h>

using namespace std;

int main() {
//    freopen("sample.in", "r", stdin);
//    freopen("B-small-attempt0.in", "r", stdin);
    freopen("B-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int tc;
    cin >> tc;
    for (int ti = 1; ti <= tc; ++ti) {
        printf("Case #%d: ", ti);
        int n, c, m; cin >> n >> c >> m; 

        vector<map<int, int>> buyers(c); 

        for (int i = 0; i < m; ++i) {
            int p, b; cin >> p >> b; --p; --b;
            ++buyers[b][p];
        }


        vector<int> s(n);

        int ma = 0;
        for (int i = 0; i < c; ++i) {
            int r = 0;
            for (auto &x: buyers[i]) {
                r += x.second;
            }
            ma = max(r, ma);
        }

        int le = ma, ri = 1111, z; 
        do {
            int mid = (le+ri)>>1;

            vector<map<int, int>> o = buyers;

            s.assign(n, mid);
            bool ok = true;

            z = 0;
            for (int i = 0; i < c; ++i) {

                for (auto &x: buyers[i]) {
                    int t = min(x.second, s[x.first]);
                    if (t) {
                        s[x.first] -= t;
                        o[i][x.first] -= t;
                    }
                    z += x.second-t;
                }
            }

            for (int i = 0; ok && i < c; ++i) {

                for (auto &x: o[i]) {
                    if (x.second == 0) {
                        continue;
                    }

                    int r = x.second;
                    for (int p = x.first-1; p >= 0; --p) {
                        if (s[p]) {
                            int t = min(s[p], r);
                            r -= t;
                            s[p] -= t;
                            if (r == 0) {
                                break;
                            }
                        }
                    }
                    if (r) {
                        ok = false;
                        break;
                    }
                }
            }
                    
            if (le == ri)
                break;

            if (ok) {
                ri = mid;
            }
            else {
                le = mid+1;
            }
        }
        while (true);

        printf("%d %d\n", le, z);
    }
    return 0;
}
