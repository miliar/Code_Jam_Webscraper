#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <set>
#include <unordered_set>
#include <map>
#include <string>
#include <unordered_map>
#include <string>
#include <vector>
#include <queue>
#include <string.h>
#include <algorithm>

using namespace std;

int dp[2][1000][2];
typedef pair<int, int> pp;
vector<pp> p[2];
void update(int& a, const int &b) {
    if (b >= 0) {
        if (a < 0 || a > b) {
            a = b;
        }
    }
}
int inc(int v) {
    if (v >= 0) {
        ++v;
    }
    return v;
}
int getans(int a, int b) {
    if (a > 0) {
        if (b > 0) {
            return min(a, b);
        }
        return a;
    } else if (b > 0) {
        return b;
    }
    return 1e9;
}
int cal(int s) {
    int f = 0, t = 1;
    memset(dp[f], -1, sizeof(dp[f]));
    dp[f][0][s] = 0;
    int ia[2] = {0};
    for (int j = 0; j < 24 * 60; ++j) {
        memset(dp[t], -1, sizeof(dp[t]));
        for (int ll = 0; ll < 2; ++ll) {
            int l = 1 - ll;
            for (; ia[l] < p[l].size() && j >= p[l][ia[l]].second; ++ia[l]) {}
            if (ia[l] < p[l].size() && j < p[l][ia[l]].second &&
                j >= p[l][ia[l]].first) {
                continue;
            }
            for (int k = 0; k <= j && k <= 12 * 60; ++k) {
                update(dp[t][k + (ll == 0 ? 1 : 0)][ll], dp[f][k][ll]);
                update(dp[t][k + (ll == 0 ? 1 : 0)][ll], inc(dp[f][k][1 - ll]));
            }
        }
        swap(f, t);
    }
    return f;
}

int main() {
    int test;
    scanf("%d", &test);
    for (int i = 0; i < test; ++i) {
        int n[2];
        scanf("%d%d", &n[0], &n[1]);
        for (int j = 0; j < 2; ++j) {
            p[j].clear();
            for (int k = 0; k < n[j]; ++k) {
                int s, t;
                scanf("%d%d", &s, &t);
                p[j].push_back(make_pair(s, t));
            }
            sort(p[j].begin(), p[j].end());
        }
        int f = cal(0);
        int ans = getans(dp[f][12 * 60][0], inc(dp[f][12 * 60][1]));
        f = cal(1);
        ans = getans(ans, getans(inc(dp[f][12 * 60][0]), dp[f][12 * 60][1]));
        printf("Case #%d: %d", (i + 1), ans);
        if (i + 1 < test) {
            printf("\n");
        }
    }
    return 0;
}
