#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef unsigned long long int llu;
#define pb push_back
#define mp make_pair
#define X first
#define Y second
#define mem(a, v) memset(a, v, sizeof(a))
#define PI acos(-1)
#define S(a) scanf("%d",&a)
#define SL(a) scanf("%lld",&a)
#define S2(a, b) scanf("%d%d",&a,&b)
#define nl printf("\n")
#define deb(x) cout<<#x<<" : "<<x<<endl;
#define deb2(x, y) cout<<#x<<" : "<<x<<" | "<<#y<<" : "<<y<<endl;
#define deb3(x, y, z) cout<<#x<<" : "<<x<<" | "<<#y<<" : "<<y<<" | "<<#z<<" : "<<z<<endl;
#define debv(x) {cout<<#x<<" : "<<endl; for(int ii =0; ii < x.size(); ii++) cout<<x[ii]<<" "; cout<<endl; }
#define debarr(x, xs) {cout<<#x<<" : "<<endl; for(int ii =0; ii < xs; ii++) cout<<x[ii]<<" "; cout<<endl; }
//auto T=clock(); 
//cout<<double(clock()-T)/CLOCKS_PER_SEC<<'\n';
//cout << fixed << setprecision(10) << f(0, 0, 0) << "\n";
const ll mod = 1000000007LL;
const int lmt = 1000005;
 

ll dp[20][2][2][11];
 
char y[100];
int n;

ll solve(int i, int st, int lo, int last) {
    if(i == n) {
        if(st)
            return 1LL;
        return 0LL;
    }
    if(dp[i][st][lo][last] != -1)
        return dp[i][st][lo][last];
    ll ans = 0;
    int upto, dig = y[i] - '0';
    if(lo) upto = 9;
    else upto = dig;

    for(int d = last; d <= upto; d++){
        ans += solve(i+1, st||(d > 0), lo||(d < dig), d);
    }
    return dp[i][st][lo][last] = ans;
}

int main(){
    freopen("B-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    int t;
    S(t);
    for(int tst = 1; tst <= t; tst++) {
        ll a;
        SL(a);
        sprintf(y,"%lld",a);
        n = strlen(y);
        mem(dp, -1);
        ll tot = solve(0, 0, 0, 0);

        ll lo = 1, hi = a;

        while(lo < hi) {
            ll mid = (lo + hi)/2;
            sprintf(y,"%lld",mid);
            n = strlen(y);
            mem(dp, -1);
            ll cur = solve(0, 0, 0, 0);

            if(tot > cur)
                lo = mid+1;
            else
                hi = mid;
             
        }
        printf("Case #%d: %lld\n",tst, lo);
    }
    return 0;
}