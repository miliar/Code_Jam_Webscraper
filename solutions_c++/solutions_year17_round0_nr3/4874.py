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

int mx , mn;
int main() {
    freopen("C-small-2-attempt0.in", "r" , stdin);
    freopen("output.txt", "w", stdout);
    int t;
    cin >> t;
    for(int test = 1; test <= t; ++ test) {

        int n , k;
        scanf("%d", &n);
        scanf("%d", &k);
        mx = 1e6 + 1;
        mn = 1e6 + 1;
        priority_queue<int>pq;
        pq.push(n);
        for(int j = 0; j < k; ++ j) {
            int x = pq.top();
            pq.pop();
            int y = x / 2;
            int z = x / 2 - 1 + x % 2;
            if(y + z < mx + mn) {
                mx = y;
                mn = z;
            }
            if(mx + mn == 0) {
                break;
            }
            pq.push(y);
            pq.push(z);
        }
        printf("Case #%d: %d %d\n", test, mx , mn);
    }
}
