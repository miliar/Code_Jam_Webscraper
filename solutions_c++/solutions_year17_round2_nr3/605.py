#include <bits/stdc++.h>
#define forn(i, n) for(int i = 0; i < (int)(n); i++)
typedef long long ll;
typedef long double ld;
using namespace std;

const int MAXN = 100, EPS = 1e-8;
int e[MAXN + 1], s[MAXN + 1], f[MAXN + 1][MAXN + 1];

struct point {
    ll first;
    int second;
    point() : first(0), second(0) {}
    point(ld cur, int idx) : first(cur), second(idx) {}
};

bool operator<(const point& a, const point& b) {
    if(a.first == b.first)
        return a.second < b.second;
    else
        return a.first < b.first;
}

int main() {
    //ios_base::sync_with_stdio(false);
    freopen("C.in", "r", stdin);
    freopen("output.txt", "w", stdout);

    int T;
    cin >> T;
    for(int t = 1; t <= T; t++) {
        int n, q;
        scanf("%d%d", &n, &q);
        for(int i = 1; i <= n; i++) {
            scanf("%d%d", &e[i], &s[i]);
        }
        for(int i = 1; i <= n; i++) {
            for(int j = 1; j <= n; j++) {
                scanf("%d", &f[i][j]);
            }
        }
        cout << "Case #" << t << ": ";
        for(int i = 0; i < q; i++) {
            int v, u;
            scanf("%d%d", &v, &u);
            vector<ld> bestDist(n + 1, 1e18), bestBest(n + 1, 1e18);
            bestDist[v] = 0;
            vector<int> used(n + 1, 0);
            for(int i = 1; i <= n; i++) {
                int temp = -1;
                for(int j = 1; j <= n; j++) {
                    if(!used[j]) {
                        if(temp == -1)
                            temp = j;
                        else if(bestDist[temp] > bestDist[j])
                            temp = j;
                    }
                }
                bestBest[temp] = bestDist[temp];
                used[temp] = 1;
                vector<ll> bestKm(n + 1, 1e18);
                bestKm[temp] = 0;
                set<point> ans;
                for(int i = 1; i <= n; i++) {
                    ans.insert({ bestKm[i], i });
                }
                while (!ans.empty()) {
                    auto it = ans.begin();
                    int st = it->second;
                    ans.erase(it);
                    for (int i = 1; i <= n; i++) {
                        if (f[st][i] != -1) {
                            //cout << i << " " << st << " " << bestDist[i] << " " << bestDist[st] + f[st][i] / (ld)x.second << "\n";
                            if (bestKm[st] + f[st][i] <= e[temp]  && bestKm[i] > bestKm[st] + f[st][i]) {
                                ans.erase({ bestKm[i], i });
                                bestKm[i] = bestKm[st] + f[st][i];
                                ans.insert({bestKm[i], i});
                            }
                        }
                    }
                }
                for(int i = 1; i <= n; i++) {
                    if(!used[i]) {
                        bestDist[i] = min(bestDist[i], bestDist[temp] + bestKm[i] / (ld)s[temp]);
                    }
                }
            }
            cout << fixed << setprecision(15) << bestBest[u] << " ";
        }
        cout << "\n";
    }
    return 0;
}