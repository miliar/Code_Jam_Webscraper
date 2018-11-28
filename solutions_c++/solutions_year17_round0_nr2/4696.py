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
    freopen("B-large.in", "r" , stdin);
    freopen("output.txt", "w", stdout);
    int t;
    cin >> t;
    for(int test = 1; test <= t; ++ test) {

        string s, ans = "";
        cin >> s;
        int sz = s.size();
        if(sz == 1) ans = s;
        else {
            int ind = -1;
            for(int i = 0; i < sz - 1; ++ i) {
                if(s[i] > s[i + 1]) {
                    ind = i;
                    break;
                }
            }
            if(ind == -1) {
                ans = s;
            }
            else {
                int lim = -1;
                for(int i = ind; i >= 0; -- i) {
                    if(i > 0) {
                        if(s[i] != s[i - 1]) {
                            s[i] --;
                            lim = i;
                            break;
                        }
                    }
                }
                if(lim != -1) {
                        for(int j = 0; j <= lim; ++ j) ans += s[j];
                        for(int j = lim + 1; j < sz; ++ j) ans += '9';
                }
                else {
                    if(s[0] == '1') {
                        for(int j = 0; j < sz - 1; ++ j) ans += '9';
                    }
                    else {
                        s[0] --;
                        ans += s[0];
                        for(int j = 1; j < sz; ++ j) ans += '9';
                    }
                }
            }
        }

        cout << "Case #" << test << ": ";
        cout << ans << endl;
    }
}
