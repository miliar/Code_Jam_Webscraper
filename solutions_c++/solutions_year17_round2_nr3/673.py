#include <iostream>
#include <vector>
#include <string>
#include <set>
#include <algorithm>
#include <cmath>
#include <map>
#include <queue>
#include <ctime>
#include <unordered_map>
using namespace std;

clock_t begin_time, end_time;
void printtime() {
    end_time = clock();
    double elapsed_secs = double(end_time - begin_time) / CLOCKS_PER_SEC;
    cerr << "\nTime elapsed: " << elapsed_secs << endl;
}

const int MAXN = 100 + 7;
long long d[MAXN][MAXN];
const long long INF = 1000000000000L; // 10 ^ 12

void solve() {
    int n, Q;
    cin >> n >> Q;
    vector<int> e(n), s(n);
    for(int i=0;i<n;i++) {
        scanf("%d%d", &e[i], &s[i]);
    }
    for(int i=0;i<n;i++) {
        for(int j=0;j<n;j++) {
            scanf("%lld", &d[i][j]);
            if(d[i][j] == -1)
                d[i][j] = INF;
        }
    }
    for(int i=0;i<n;i++)
        d[i][i] = 0;
    // Calculate distance
    for(int k=0;k<n;k++) {
        for(int i=0;i<n;i++) {
            for(int j=0;j<n;j++) {
                d[i][j] = min(d[i][j], d[i][k] + d[k][j]);
            }
        }
    }
    // cout << endl;
    // for(int i=0;i<n;i++) {
    //     for(int j=0;j<n;j++) {
    //         cout << d[i][j] << " ";
    //     }
    //     cout << endl;
    // }
    for(int test_=0;test_<Q;test_++) {
        int u, v;
        cin >> u >> v;
        u--;v--;
        // Solution
        vector<double> t(n, INF);
        t[u] = 0;
        set< pair<double, int> > q;
        q.insert({0, u});
        while(!q.empty()) {
            auto tmp = *q.begin();
            q.erase(q.begin());
            int f = tmp.second;
            for(int i=0;i<n;i++) {
                if(d[f][i] <= e[f]) {
                    double tt = t[f] + (0. + d[f][i]) / s[f];
                    if(tt < t[i]) {
                        t[i] = tt;
                        q.insert({tt, i});
                    }
                }
            }
        }
        if(test_ != 0)
            printf(" ");
        printf("%.7f", t[v]);
    }
    printf("\n");
}

int main() {
    begin_time = clock();

    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);

    int tests;
    scanf("%d", &tests);
    for(int i=0;i<tests;i++) {
        printf("Case #%d: ", i + 1);
        solve();
    }

    printtime();
    return 0;
}