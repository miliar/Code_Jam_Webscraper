#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <iostream>
#include <cassert>
#include <cmath>
#include <string>
#include <queue>
#include <set>
#include <map>
#include <cstdlib>

using namespace std;

#define INF 1e+9
#define mp make_pair
#define pb push_back
#define fi first
#define fs first
#define se second
#define i64 long long
#define li long long
#define lint long long
#define pii pair<int, int>
#define vi vector<int>

#define forn(i, n) for (int i = 0; i < (int)n; i++)
#define fore(i, b, e) for (int i = (int)b; i <= (int)e; i++)

const int maxn = 1e6 + 5;

typedef int myarray[maxn];
myarray L, R, minn, maxx;
bool mark[maxn];
set <int> order[maxn];

inline void upd(int k, bool flag=false) {
    int was = minn[k];
    minn[k] = min(k - L[k], R[k] - k);
    if (minn[k] != was) {
        order[was].erase(k);
    }
    maxx[k] = max(k - L[k], R[k] - k);
    if (minn[k] != was || flag) {
        order[minn[k]].insert(k);
    }
}

inline void make(int best_pos) {
    mark[best_pos] = true;
    int cur = best_pos + 1;
    while(!mark[cur]) {
        L[cur] = best_pos;
        upd(cur);
        cur++;
    }
    cur = best_pos - 1;
    while(!mark[cur]) {
        R[cur] = best_pos;
        upd(cur);
        cur--;
    }
}

int main() {
    int tests;
    scanf("%d", &tests);
    fore(test, 1, tests) {
        cerr << "test " << test << endl;
        int n, k;
        scanf("%d%d", &n, &k);
        //cerr << "n = " << n << " k = " << k << endl;
        n += 2;
        forn(j, n)
            mark[j] = false;
        mark[0] = mark[n - 1] = true;
        forn(j, n + 1)
            order[j].clear();
        fore(k, 1, n - 2) {
            L[k] = 0;
            R[k] = n - 1;
            upd(k, true);
        }
        for (int part = n; part >= 0; part--) {
            if (order[part].empty())
                continue;
            if (part == 1) {
                vi max0, max1;
                for (int x : order[1]) {
                    if (maxx[x] == 1)
                        max0.pb(x);
                    else max1.pb(x);
                }
                sort(max1.begin(), max1.end());
                for (int x : max1) {
                    if (maxx[x] == 1) {
                        max0.pb(x);
                        continue;
                    }
                    k--;
                    if (k == 0) {
                        printf("Case #%d: %d %d\n", test, maxx[x] - 1, minn[x] - 1);
                        break;
                    }
                    make(x);
                }
                sort(max0.begin(), max0.end());
                for (int x : max0) {
                    k--;
                    if (k == 0) {
                        printf("Case #%d: %d %d\n", test, maxx[x] - 1, minn[x] - 1);
                        break;
                    }
                    make(x);
                }

                continue;
            }
            vector <pii> vec;
            for (int x : order[part])
                vec.pb(mp(-maxx[x], x));
            sort(vec.begin(), vec.end());
            bool done = false;
            for (pii elem : vec) {
                auto best_pos = elem.second;
                if (order[part].find(best_pos) == order[part].end())
                    continue;
                //printf("pos: %d\n", best_pos);
                k--;
                if (k == 0) {
                    printf("Case #%d: %d %d\n", test, maxx[best_pos] - 1, minn[best_pos] - 1);
                    done = true;
                    break;
                }
                make(best_pos);
            }
            if (done)
                break;
        }
    }
}
