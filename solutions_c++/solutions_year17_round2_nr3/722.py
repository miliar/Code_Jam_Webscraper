#include <bits/stdc++.h>

using namespace std;
typedef long long li;

template <class T>
vector<vector<T>> wf(vector<vector<T>> d) {
    auto ans = d;
    const int n = d.size();

    for (int k = 0; k < n; ++k) {
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                if (ans[i][k] != -1 and ans[k][j] != -1) {
                    if (ans[i][j] == -1) {
                        ans[i][j] = ans[i][k] + ans[k][j];
                    } else {
                        ans[i][j] = min(ans[i][j], ans[i][k] + ans[k][j]);
                    }
                }
            }
        }
    }
    return ans;
}

void solve() {
    static int casenum = 1;
    li n, q;
    cin >> n >> q;

    vector<li> es(n), ss(n);
    for (int i = 0; i < n; ++i) {
        cin >> es[i] >> ss[i];
    }

    vector<vector<li>> graph(n, vector<li>(n));
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            cin >> graph[i][j];
        }
    }

    vector<li> fr(q), to(q);
    for (int i = 0; i < q; ++i) {
        cin >> fr[i] >> to[i];
        fr[i]--; to[i]--;
    }

    auto distance = wf(graph);

    vector<vector<double>> timegraph(n, vector<double>(n));
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            if (distance[i][j] != -1 and distance[i][j] <= es[i]) {
                timegraph[i][j] = (double) distance[i][j] / ss[i];
            } else {
                timegraph[i][j] = -1;
            }
        }
    }

    auto timedistance = wf(timegraph);

    cout.precision(16);
    cout << "Case #" << casenum << ":";
    casenum += 1;

    for (int i = 0; i < q; ++i) {
        auto ans = timedistance[fr[i]][to[i]];
        cout << " " << fixed << ans;
    }
    cout << endl;
}

int main() {
    li t;
    cin >> t;
    while (t--) {
        solve();
    }
    return 0;
}