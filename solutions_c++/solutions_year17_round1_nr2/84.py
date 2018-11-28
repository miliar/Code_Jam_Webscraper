#include <bits/stdc++.h>

using namespace std;

#define pb push_back
#define mp make_pair
#define forn(i, n) for (int i = 0; i < (int)(n); ++i)
typedef long long LL;
typedef pair<int, int> PII;

int test, testCount;

const int INF = int(1e9);

int n, p;
int r[50];
int q[50][50];
int from[50][50], to[50][50], done[50][50];

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    scanf("%d", &testCount);
    for (int test = 1; test <= testCount; ++test) {
        printf("Case #%d: ", test);
        scanf("%d%d", &n, &p);
        forn(i, n) {
            scanf("%d", r + i);
        }
        forn(i, n) forn(j, p) {
            scanf("%d", q[i] + j);
        }
        forn(i, n) forn(j, p) {
            from[i][j] = (q[i][j] * 100 + r[i] * 110 - 1) / (r[i] * 110);
            to[i][j] = (q[i][j] * 100) / (r[i] * 90);
        }
        memset(done, 0, sizeof done);
        int ans = 0;
        while (true) {
            bool bad = false;
            int st = 0;
            forn(i, n) {
                int cur = INF;
                forn(j, p) if (!done[i][j] && from[i][j] < cur) {
                    cur = from[i][j];
                }
                if (cur == INF) {
                    bad = true;
                    break;
                }
                st = max(st, cur);
            }
            if (bad) {
                break;
            }
            bad = true;
            vector<int> v;
            forn(i, n) {
                forn(j, p) if (!done[i][j] && to[i][j] < st) {
                    done[i][j] = true;
                    bad = false;
                }
                int cur = INF;
                int curInd = -1;
                forn(j, p) if (!done[i][j] && from[i][j] <= st && to[i][j] >= st) {
                    if (to[i][j] < cur) {
                        cur = to[i][j];
                        curInd = j;
                    }
                }
                if (curInd != -1) {
                    v.pb(curInd);
                }
            }
            if ((int)v.size() == n) {
                bad = false;
                forn(i, n) done[i][v[i]] = true;
                ++ans;
            }
            if (bad) {
                break;
            }
        }
        cout << ans << endl;
        cerr << "done " << test << endl;
    }
    return 0;
}
