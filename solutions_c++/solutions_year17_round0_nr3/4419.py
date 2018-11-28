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

vector < int > v;

void bfs (int n){
    queue < int > q;
    q.push(n/2);
    if (n & 1) q.push(n/2);
    else q.push(n/2-1);
    while (!q.empty()){
        int p = q.front();
        q.pop();
        if (p == 0) continue;
        v.pb(p);
        q.push((p-1)/2);
        q.push(p/2);
    }
}

int main()
{
    freopen("C_stwo.txt", "r", stdin);
    freopen("C_soutTWO.txt", "w", stdout);
    int t = nxt(), cse = 0;
    while (t--){
        v.clear();
        int n = nxt(), k = nxt();
        bfs(n);
        v.pb(n);
        sort(v.begin(), v.end());
        reverse(v.begin(), v.end());
        //for (int i=0; i<v.size(); i++) cout << v[i] << " "; cout << endl;
        printf("Case #%d: ", ++cse);
        cout << v[k-1]/2 << " " << (v[k-1]-1)/2 << endl;
    }
    return 0;
}
