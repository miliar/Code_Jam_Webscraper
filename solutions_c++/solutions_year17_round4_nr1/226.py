#include <bits/stdc++.h>

#define FO(i,a,b) for (int i = (a); i < (b); i++)
#define sz(v) int(v.size())

using namespace std;

map<vector<int>, int> cache[10];

int f(vector<int> v, int cm, int tot) {
    if (tot == 0) return 0;
    else if (cache[cm].count(v)) return cache[cm][v];
    else {
        int res = 0;
        int p = sz(v)+1;
        FO(i,0,sz(v)) if (v[i]) {
            v[i]--;
            int o = f(v, (cm+i+1)%p, tot-1);
            res = max(res, o + (cm == 0));
            v[i]++;
        }
        return cache[cm][v] = res;
    }
}

int main() {
    int T; scanf("%d", &T);
    FO(Z,1,T+1) {
        int p, n;
        scanf("%d %d", &n, &p);
        vector<int> v(p-1);
        int res = 0;
        FO(i,0,n) {
            int g; scanf("%d", &g);
            if (g % p == 0) {
                res++;
            } else v[(g%p)-1]++;
        }
        res += f(v, 0, n-res);
        printf("Case #%d: %d\n", Z, res);
    }
}

