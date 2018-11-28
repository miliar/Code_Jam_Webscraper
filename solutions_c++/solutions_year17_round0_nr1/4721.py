#include <bits/stdc++.h>
using namespace std;
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
ll gcd ( ll a, ll b ){ll c;  while ( a != 0 ) { c = a; a = b%a;  b = c;}return b;};
ll lcm ( ll a , ll b) {return a / gcd(a , b) * b;}
int main() {
    freopen("A-large.in", "r" , stdin);
    freopen("output.txt", "w", stdout);
    int t;
    cin >> t;
    for(int test = 1; test <= t; ++ test) {
        string s;
        cin >> s;
        int k , ans = 0;
        cin >> k;
        int sz = s.size();
        for(int i = 0; i < sz - k + 1; i ++) {
            if(s[i] == '+') continue;
            ans ++;
            for(int j = i; j < i + k; j ++) {
                if(s[j] == '-') s[j] = '+';
                else s[j] = '-';
            }
        }
        int ok = 1;
        for(int i = 0; i < s.size(); ++ i) {
            if(s[i] == '-') ok = 0;
        }
        cout << "Case #" << test << ": ";
        if(!ok) cout << "IMPOSSIBLE" << endl;
        else cout << ans << endl;
    }
}
