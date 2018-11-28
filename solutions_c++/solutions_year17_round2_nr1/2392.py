#include <bits/stdc++.h>
using namespace std;
#define fi first
#define se second
#define pi 3.14159265359
#define in(x) scanf("%d" ,&x)
#define IN(x) scanf("%I64d" , &x)
#define out(x) printf("%d" , x)
#define OUT(x) printf("%I64d", x)
#define ll long long
#define all(a) memset(a , 0 , sizeof a)
#define ull unsigned long long
#define pii pair<int , int>
const int mod = 1e9+7;
const int MAXN = 2e5 + 10;
ll powmod(ll a,ll b){ll res=1;a%=mod;assert(b>=0);for(;b;b>>=1){if(b&1)res=res*a%mod;a=a*a%mod;}return res;}
int gcd ( int a, int b ){int c;  while ( a != 0 ) { c = a; a = b%a;  b = c;}return b;};
ll lcm ( ll a , ll b) {return a / gcd(a , b) * b;}
int main() {
    freopen("Al.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t, d, n;
    cin >> t;
    for(int test = 1; test <= t; ++ test) {
        cin >> d >> n;
        double mx = 0.;
        for(int i = 0; i < n; ++ i) {
            int p, s;
            cin >> p >> s;
            double time = (double)(d - p) / s;
            mx = max(time, mx);
        }
        cout << fixed;
        cout << setprecision(9);
        cout << "Case #" << test << ": " << d / mx << endl;
    }
}


