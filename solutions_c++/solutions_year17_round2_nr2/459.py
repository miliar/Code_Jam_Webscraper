#include <bits/stdc++.h>

using namespace std;

const string IMPOSSIBLE = "IMPOSSIBLE";

int main() {
//    freopen("sample.in", "r", stdin);
    freopen("B-small-attempt2.in", "r", stdin);
//    freopen("B-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int tc;
    cin >> tc;

    vector<vector<bool>> g(6, vector<bool>(6, true));
    for (int i = 0; i < 6; ++i)
        for (int j = max(0, i-1); j < min(6, i+1); ++j)
            g[i][j] = false;
    g[5][0] = g[0][5] = false;

    for (int ti = 1; ti <= tc; ++ti) {
        printf("Case #%d: ", ti);
        int n;
        vector<int> c(6);
        vector<int> oc(6);
        cin >> n;
        for (int i = 0; i < 6; ++i) {
            cin >> c[i];
            oc[i] = c[i];
        }

        bool gok = false;


        for (int y = 0; y < 6; ++y) {

            if (oc[y] == 0) {
                continue;
            }

            for (int i = 0; i < 6; ++i)
                c[i] = oc[i];

            vector<int> ans(n);
            bool ok = true;
            vector<pair<int, int>> s(6);

            ans[0] = y;
            --c[y];

            for (int i = 1; i < n; ++i) {
                for (int j = 0; j < 6; ++j) {
                    s[j] = {c[j], j};
                }
                sort(s.rbegin(), s.rend());
                bool fnd = false;
                for (int j = 0; j < 6; ++j) {
                    if (s[j].first == 0) {
                        break;
                    }
                    if (g[ans[i-1]][s[j].second]) {
                        ans[i] = s[j].second;
                        --c[s[j].second];
                        fnd = true;
                        break;
                    }
                }
                if (!fnd) {
                    ok = false;
                    break;
                }
            }

            if (ok && g[ans[n-1]][ans[0]]) {
                for (int i = 0; i < n; ++i) {
                    printf("%c", "ROYGBV"[ans[i]]);
                }
                printf("\n");
                gok = true;
                break;
            }
        }

        if (!gok) {
            printf("IMPOSSIBLE\n");
        }
    }
    return 0;
}
