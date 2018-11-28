/*************************************************************************
    > In god we trust
    > File Name: A.cpp
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
const int maxn = 1e3 + 10;
char s[maxn];
int n, T, k;

void init() {
    memset(s, 0, sizeof(s));
    n = 0;
}

void revert(int fst, int lst) {
    rep(i, fst, lst)
        s[i] = (s[i]=='+') ? '-' : '+';
}

int check() {
    int p = 0, ans = 0;
    while(p+k <= n) {
        if (s[p] == '-') { revert(p, p+k); ++ans;}
        ++p;
    }
    rep(i, p, n) if (s[i]=='-') return -1;
    return ans;  
}

int main() {
#ifdef ROACH_ONLINE_JUDGE
    freopen("A.txt", "r", stdin);
#endif
    scanf("%d", &T);
    rep(i, 1, T+1) {
        init();
        scanf("%s%d", s, &k); 
        n = strlen(s);
        int r = check();
        if (r!=-1)
            printf("Case #%d: %d\n", i, r);
        else
            printf("Case #%d: IMPOSSIBLE\n", i);
    }
}
