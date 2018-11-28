#include <bits/stdc++.h>

using namespace std;

int need[55], w[55][55];

bool inrange(long long x, long long y) {
    return x * 9 <= y * 10 && y * 10 <= 11 * x;
}

pair <int, int> cal(long long x, long long y) {
    int l = 1, r = 1000000, retl = 1 << 30, retr = -(1 << 30);
    while(l <= r) {
        int m = (l + r) >> 1;
        long long t = x * m;
        long long ll = t * 9;
        long long rr = t * 11;
        if(y * 10 > rr) {
            l = m + 1;
        } else if(y * 10 < ll) {
            r = m - 1;
        } else {
            retl = m;
            r = m - 1;
        }
    }
    l = 1; r = 1000000;
    while(l <= r) {
        int m = (l + r) >> 1;
        long long t = x * m;
        long long ll = t * 9, rr = t * 11;
        if(y * 10 > rr) {
            l = m + 1;
        } else if(y * 10 < ll) {
            r = m - 1;
        } else {
            retr = m;
            l = m + 1;
        }
    }
    if(retl > retr)
        return make_pair(-1, -1);
    return make_pair(retl, retr);
}

vector < pair <int, int> > G[55];

bool inter(int a, int b) {
    pair <int, int> x = G[a][G[a].size() - 1];
    pair <int, int> y = G[b][G[b].size() - 1];
    if(x.second < y.first || y.second < x.first)
        return false;
    return true;
}

int main() {
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    int T;
    scanf("%d", &T);
    for(int cas = 1; cas <= T; ++ cas) {
        int n, p;
        scanf("%d%d", &n, &p);
        for(int i = 0; i < n; ++ i)
            scanf("%d", need + i);
        for(int i = 0; i < n; ++ i)
            for(int j = 0; j < p; ++ j)
                scanf("%d", w[i] + j);
        printf("Case #%d: ", cas);
        for(int i = 0; i < n; ++ i)
            G[i].clear();
        for(int i = 0; i < n; ++ i)
            for(int j = 0; j < p; ++ j) {
                pair <int, int> t = cal(need[i], w[i][j]);
                if(t.first != -1)
                    G[i].push_back(t);
            }
        for(int i = 0; i < n; ++ i)
            sort(G[i].begin(), G[i].end());
        int ans = 0;
        while(true) {
            bool ep = false;
            for(int i = 0; i < n; ++ i)
                if(G[i].empty())
                    ep = true;
            if(ep)
                break;
            int mx = -1, who = 0;
            for(int i = 0; i < n; ++ i) {
                int x = G[i][G[i].size() - 1].first;
                if(x > mx) {
                    mx = x;
                    who = i;
                }
            }
            bool flag = true;
            for(int i = 0; i < n; ++ i) {
                bool ok = true;
                for(int j = 0; ok && j < n; ++ j)
                    ok &= inter(i, j);
                if(!ok) {
                    flag = false;
                    break;
                }
            }
            if(flag) {
                ++ ans;
                for(int i = 0; i < n; ++ i)
                    G[i].pop_back();
            } else {
                G[who].pop_back();
            }
        }
        printf("%d\n", ans);
    }
    return 0;
}
