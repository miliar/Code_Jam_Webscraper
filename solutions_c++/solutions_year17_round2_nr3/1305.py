#include <bits/stdc++.h>

using namespace std;

#ifndef ONLINE_JUDGE
#define db(...) printf(__VA_ARGS__);
#else
#define db(...)
#endif

#define mp(x,y) make_pair(x,y)
#define For(i,n) for(int i = 0; i<n; ++i)

typedef long long ll;
typedef unsigned long long ull;
typedef pair<int, int> pii;
typedef vector<int> vi;
typedef vector<ll> vl;

int n,q;
vector< pair<ll, ll> > kone;
vector< vector<ll> > g;

long double ries(int u, int v) {
    vector< vector< pair<int, long double> > > rych(n, vector< pair<int, long double> >());
    For(k, n) {
        vector< pair<long double, int> > r;
        ll vzd = 0;
        for (int z = k-1; z>=0; z--){
            vzd += g[z][z+1];
            if (kone[z].first < vzd) continue;
            long double time = (vzd+0.0L)/kone[z].second;
            r.push_back({time, z});
        }
        sort(r.begin(), r.end());
        int last = n+47;
        For(z, r.size()) {
            if (r[z].second > last) continue;
            rych[k].push_back({r[z].second, r[z].first});
            last = r[z].second;
        }
    }
    set< pair<long double, int> > pq;
    pq.insert({0.0L, v});
    vector<long double> vzd(n, -47);
    vector<bool> mam(n, false);
    mam[v] = true;
    vzd[v] = 0.0L;
    while (!pq.empty()) {
        auto it = pq.begin();
        pair<long double, int> t = *it;
        pq.erase(it);

        int kto = t.second;
        long double time = t.first;
        if (kto == u) break;
        for (pair<int, long double> sused: rych[kto]) {
            long double alt = sused.second + time;
            //db("Bug %d->%d: %f + %f = %f\n", kto, sused.first, sused.second, time, alt);
            if (!mam[sused.first] || alt < vzd[sused.first]) {
                pq.erase({vzd[sused.first], sused.first});
                vzd[sused.first] = alt;
                mam[sused.first] = true;
                pq.insert({alt, sused.first});
            }
        }

    }
    return vzd[u];
}

int main() {
    int T;
    scanf("%d", &T);
    for (int t = 1; t<=T; ++t) {
        printf("Case #%d: ", t);
        scanf("%d %d", &n, &q);
        kone.clear();
        g.clear();
        g.resize(n, vector<ll>(n, -1));
        For(i,n) {
            ll e,s;
            scanf("%lld %lld", &e, &s);
            kone.push_back({e,s});
        }
        For(i, n) {
            For (j, n) {
                ll x;
                scanf("%lld", &x);
                g[i][j] = x;
            }
        }
        For(i,q) {
            int u,v;
            scanf("%d %d", &u, &v);
            u--; v--;
            printf(" %Lf", ries(u, v));
        }
        printf("\n");
    }
    return 0;
}
