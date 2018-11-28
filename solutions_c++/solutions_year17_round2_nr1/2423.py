#include <bits/stdc++.h>
#define ll long long int
#define pii pair <int,int>
#define ff first
#define ss second
#define pi acos(-1.0)
#define pb push_back
#define INF (ll)1e17
#define N 100002
#define MOD 1000000007
#define BASE 100003
//#define FastRead ios_base::sync_with_stdio(0);cin.tie(0)
using namespace std;

template < class T > inline T gcd(T a, T b) {while(b) {a %= b; swap(a, b);} return a;}
template < class T > inline T lcm(T a, T b) {return a/gcd(a, b)*b;}
inline int nxt() {int wow; scanf("%d", &wow); return wow;}
inline ll lxt() {ll wow; scanf("%lld", &wow); return wow;}
inline double dxt() {double wow; scanf("%lf", &wow); return wow;}

/***************** Fighters Launched *******************/

int main()
{
    freopen("A_large.txt", "r", stdin);
    freopen("A_Lout.txt", "w", stdout);
    int t = nxt(), cse = 0;
    while (t--){
        ll d = lxt();
        int n = nxt();
        double mx = -1.0;
        for (int i=1; i<=n; i++){
            ll k = lxt(), s = lxt();
            double t = (double)(d-k)/(double)s;
            mx = max(mx, t);
        }
        double ans = (double)d/mx;
        printf("Case #%d: %0.8lf\n", ++cse, ans);
    }
    return 0;
}
