#include <bits/stdc++.h>
using namespace std;
#define F first
#define S second
#define mp make_pair
#define pb push_back
#define CLEAR(a) memset(a,0,sizeof a)
#define REP(i,n) for(int i=0;i<n;i++)
#define FOR(i,a,b) for(int i=a;i<=b;i++)
#define fr freopen("input.txt", "r", stdin);
#define fw freopen("output.txt", "w", stdout);
typedef long long LL;
typedef pair<int,int> pii;
const int MOD = 1e9 + 7;
const int MAX = 1e5 + 5;
int n, k;
double u, a[MAX], ret;

int check(int M){
    double x = a[M];
    double r = 0;
    for(int i=0;i<M;i++){
        r += x - a[i];
    }
    if(r > u) return 0;
    return 1;
}
void doit(int M){
    double r = 0;
    for(int i=0;i<M;i++){
        r += a[M] - a[i];
        a[i] = a[M];
    }

    double add = 0;
    
    u -= r;
    if(u > 0) add = u/(M+1);

    REP(i, M+1){
        a[i] += add;
    }
    ret = 1;
    REP(i, n) ret *= a[i];
}
int main() {
    fr;fw;
    cout << fixed << setprecision(9);
    int T, cases = 1;
    cin >> T;
    while(T--){
        cin >> n >> k >> u;
        REP(i, n) cin >> a[i];
        sort(a,a+n);
        int lo = 0, hi = n-1, pl = -1, ph = -1;
        while(1){
            int mid = (lo+hi+1) >> 1;
            if(pl == lo && ph == hi) break;
            pl = lo; ph = hi;
            if(check(mid)) lo = mid;
            else hi = mid-1;
        }
        doit(lo);
        cout <<"Case #" << cases++<<": "<< ret <<"\n";
    }
    return 0;
}