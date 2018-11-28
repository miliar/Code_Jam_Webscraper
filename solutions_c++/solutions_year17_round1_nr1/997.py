#include <bits/stdc++.h>

using namespace std;

int n, m;

const int inf = 1 << 30;

char s[30][30];

int ll[30], rr[30], uu[30], dd[30];

int has() {
    for(int i = 0; i < n; ++ i)
        for(int j = 0; j < m; ++ j)
            if(s[i][j] == '?')
                return i * m + j;
    return -1;
}

void up(int c) {
    int l = ll[c], r = rr[c];
    int x = uu[c];
    for(int i = x - 1; i >= 0; -- i) {
        bool ok = true;
        for(int j = l; j <= r; ++ j) {
            if(s[i][j] != '?') {
                ok = false;
                break;
            }
        }
        if(!ok)
            break;
        for(int j = l; j <= r; ++ j)
            s[i][j] = 'A' + c;
        -- uu[c];
    }
}

void down(int c) {
    int l = ll[c], r = rr[c];
    int x = dd[c];
    for(int i = x + 1; i < n; ++ i) {
        bool ok = true;
        for(int j = l; j <= r; ++ j) {
            if(s[i][j] != '?') {
                ok = false;
                break;
            }
        }
        if(!ok)
            break;
        for(int j = l; j <= r; ++ j)
            s[i][j] = 'A' + c;
        ++ dd[c];
    }
}

void lef(int c) {
    int u = uu[c], d = dd[c];
    for(int j = ll[c] - 1; j >= 0; -- j) {
        bool ok = true;
        for(int i = u; i <= d; ++ i) {
            if(s[i][j] != '?') {
                ok = false;
                break;
            }
        }
        if(!ok)
            break;
        for(int i = u; i <= d; ++ i)
            s[i][j] = 'A' + c;
        -- ll[c];
    }
}

void rig(int c) {
    int u = uu[c], d = dd[c];
    for(int j = rr[c] + 1; j < m; ++ j) {
        bool ok = true;
        for(int i = u; i <= d; ++ i) {
            if(s[i][j] != '?') {
                ok = false;
                break;
            }
        }
        if(!ok)
            break;
        for(int i = u; i <= d; ++ i)
            s[i][j] = 'A' + c;
        ++ rr[c];
    }
}

void extend(int c) {
    lef(c);
    up(c);
    down(c);
    rig(c);
}

int use[30];

bool cmp(int a, int b) {
    if(uu[a] != uu[b])
        return uu[a] < uu[b];
    return ll[a] < ll[b];
}

void solve() {
    int tot = 0;
    for(int i = 0; i < 26; ++ i) {
        if(ll[i] == inf)
            continue;
        use[tot ++] = i;
    }
    random_shuffle(use, use + tot);
    for(int i = 0; i < tot; ++ i)
        extend(use[i]);
}

int main() {
    srand(time(0));
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("A-small-attempt0.out", "w", stdout);
    int T;
    scanf("%d", &T);
    for(int cas = 1; cas <= T; ++ cas) {
        scanf("%d%d", &n, &m);
        for(int i = 0; i < n; ++ i)
            scanf("%s", s[i]);
        for(int i = 0; i < 26; ++ i) {
            ll[i] = inf;
            rr[i] = -inf;
            uu[i] = inf;
            dd[i] = -inf;
        }
        for(int i = 0; i < n; ++ i)
            for(int j = 0; j < m; ++ j) {
                if(s[i][j] == '?')
                    continue;
                int k = s[i][j] - 'A';
                ll[k] = min(ll[k], j);
                rr[k] = max(rr[k], j);
                uu[k] = min(uu[k], i);
                dd[k] = max(dd[k], i);
            }
        for(int i = 0; i < 26; ++ i) {
            if(ll[i] == inf)
                continue;
            for(int a = ll[i]; a <= rr[i]; ++ a)
                for(int b = uu[i]; b <= dd[i]; ++ b)
                    s[b][a] = 'A' + i;
        }
        int tot = 0;
        while(true) {
            int t = has();
            if(t == -1)
                break;
            solve();
        }
        printf("Case #%d:\n", cas);
        for(int i = 0; i < n; ++ i)
            printf("%s\n", s[i]);
    }
    return 0;
}
