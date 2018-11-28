/*************************************************************************
    > In god we trust
    > File Name: B.cpp
************************************************************************/
const bool debug = false;
#include <cstdio>
#include <iostream>
#include <cmath>
#include <stack>
#include <queue>
#include <climits>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <cstring>
#include <algorithm>
#include <stdarg.h>
using namespace std;
#define per(i,a,n) for(int i=n-1;i>=a;--i)
#define rep(i,a,n) for(int i=a;i<n;++i)
#define erep(i,a,n) for(int i=a;i<=n;++i)
#define fi first
#define se second
#define all(x) (x).begin(), (x).end()
#define pb push_back
#define mp make_pair
typedef long long ll;
typedef vector<int> VI;
typedef pair<int, int> PII;
#define lc(o) (o<<1)
#define rc(o) (o<<1|1)
ll powmod(ll a,ll b, ll MOD) {ll res=1;a%=MOD;for(;b;b>>=1){if(b&1)res=res*a%MOD;a=a*a%MOD;}return res;}
void buginfo(const char* f, ...) {if(!debug)return;va_list al; va_start(al, f);vprintf(f, al);va_end(al);}
/*------------------ head-------------------*/
int T;
ll n;
char s[100];
void init() {
    n = 0;
}

inline void dec(int x) {
    if (s[x] == '0') s[x] = '9';
    else --s[x];
}

ll check() {
    int len = strlen(s);
    per(i, 0, len-1) {
        if (s[i] <= s[i+1]) continue;
        dec(i);
        rep(j, i+1, len) s[j] = '9';
    }
    ll ans = 0;
    sscanf(s, "%lld", &ans);
    return ans;
}

int main() {
#ifdef ROACH_ONLINE_JUDGE
    freopen("B.txt", "r", stdin);
#endif
    scanf("%d", &T);
    rep(t, 1, T+1) {
        init();
        scanf("%lld", &n);
        sprintf(s, "%lld", n);
        ll r = check();
        printf("Case #%d: %lld\n", t, r);
    }
}
