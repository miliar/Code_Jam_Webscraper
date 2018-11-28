#include <iostream>
#include <cstdio>
#include <cstring>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <cmath>
#include <ctime>
#include <cstdlib>
#include <queue>

#define LL long long
#define mp(x, y) make_pair(x, y)
#define pb(x) push_back(x)
#define PII pair<int, int>
#define PID pair<int, double>

using namespace std;

const int maxn = 1010;
int n, m, c, T, b, p;
int cnt[maxn];
vector<int> t[maxn];
bool forbid[maxn];

bool cmp(const vector<int> &a, const vector<int> &b) {
    return a.size() > b.size();
}

inline bool put(int x, multiset<int> &S) {
    int i = 0;
    for (auto &y : S) {
        i++;
        if (y >= x && y <= i) return false;
    }
    return true;
}

int main(){
    cin >> T;
    for (int id = 1; id <= T; id++) {
        printf("Case #%d: ", id);
        cin >> n >> c >> m;
        memset(cnt, 0, sizeof(cnt));
        for (int i = 0; i < c; i++) t[i].clear();
        for (int i = 0; i < m; ++i) {
            cin >> p >> b;
            b--;
            cnt[p]++;
            t[b].pb(p);
        }

        for (int i = 0; i < c; i++)
            sort(t[i].begin(), t[i].end());
        sort(t, t + c, cmp);
        
        vector<multiset<int>> S;
        for (int i = 0; i < c; i++) {
            memset(forbid, 0, sizeof(forbid));
            for (auto &x : t[i]) {
                bool done = false;
                for (int k = 0; k < S.size(); k++) {
                    if (forbid[k]) continue;
                    if (put(x, S[k])) {
                        S[k].insert(x);
                        forbid[k] = true;
                        done = true;
                        break;
                    }
                }
                if (!done) {
                    S.emplace_back();
                    int k = S.size() - 1;
                    S[k].insert(x);
                    forbid[k] = true;
                }
            }
        }

        int run = S.size(), ans = 0;
        for (int i = 1; i <= n; i++) {
            ans += max(0, cnt[i] - run);
        }
        printf("%d %d\n", run, ans);
    }
}
