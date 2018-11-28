//#include <bits/stdc++.h>

#include<cstdio>
#include<cstring>
#include<cctype>
#include<cmath>
#include<cstdlib>

#include<iostream>
#include<string>
#include<algorithm>
#include<vector>
#include<stack>
#include<queue>
#include<set>
#include<map>
#include<bitset>
using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef pair<int,int> pii;
typedef pair<ll,ll> pll;


//4-side
//int xx[] = {0,0,-1,1};
//int yy[] = {-1,1,0,0};
//6-side hexagonal
//int xx[] = {2,-2,1,1,-1,-1};
//int yy[] = {0,0,1,-1,1,-1};

#define popc(a) (__builtin_popcount(a))
//ll bigmod(ll a,ll b,ll m){if(b == 0) return 1%m;ll x = bigmod(a,b/2,m);x = (x * x) % m;if(b % 2 == 1) x = (x * a) % m;return x;}
//ll BigMod(ll B,ll P,ll M){ ll R=1%M; while(P>0) {if(P%2==1){R=(R*B)%M;}P/=2;B=(B*B)%M;} return R;} /// (B^P)%M

#define MX 105
#define inf 100000000

const ll mod = 10000000000007ll;

ll dis[MX][MX];
ll hmxdis[MX];
ll hspped[MX];

double res[MX][MX];

void calc(int n) {
    for(int k = 1; k <= n; k++)
        for(int i = 1; i <= n; i++)
            for(int j = 1; j <= n; j++) {
                dis[i][j] = min(dis[i][j],dis[i][k]+dis[k][j]);
            }
    for(int i = 1; i <= n; i++) {
        for(int j = 1; j <= n; j++) {
            if(dis[i][j] <= hmxdis[i]) {
                res[i][j] = (double) dis[i][j]/hspped[i];
            } else {
                res[i][j] = mod;
            }
        }
    }

    for(int k = 1; k <= n; k++)
        for(int i = 1; i <= n; i++)
            for(int j = 1; j <= n; j++) {
                res[i][j] = min(res[i][j],res[i][k]+res[k][j]);
            }
}

int main() {
    freopen("C-large.in", "r", stdin);
    freopen("C-large.in.out", "w", stdout);
    int te, ti;
    scanf("%d", &ti);
    for(te = 1; te <= ti; te++) {
        int n, q;
        scanf("%d %d", &n, &q);
        for(int i = 1; i <= n; i++) {
            scanf("%lld %lld", &hmxdis[i], &hspped[i]);
        }
        for(int i = 1; i <= n; i++)
            for(int j = 1; j <= n; j++) {
                scanf("%lld", &dis[i][j]);
                if(dis[i][j] == -1) dis[i][j] = mod;
                if(i == j) dis[i][j] = 0ll;
            }
        calc(n);
        printf("Case #%d:", te);
        for(int i = 1; i <= q; i++) {
            int u, v;
            scanf("%d %d", &u, &v);
            printf(" %.10lf", res[u][v]);
        }
        puts("");
    }
    return 0;
}

