#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;

#define mp make_pair
#define pb push_back
#define fi first
#define se second
#define forab(i,a,b) for( int i = (a); i < (b); i++ )
#define forn(i,n) forab(i,0,n)
#define pii pair<int,int>
#define pdd pair<double,double>
#define pll pair<ll,ll>

const int MXN = 20;


void solve() {
    int d, n;
    scanf("%d%d", &d, &n);
    double maxt = 0;
    forn(i,n) {
        int k, s;
        scanf("%d%d", &k, &s);
        maxt = max(maxt, 1.0 * (d-k) / s);
    }
    printf("%.15f", d / maxt);
}


int main(){
    freopen("input.txt", "r", stdin);    freopen("output.txt", "w", stdout);
    int T;
    scanf("%d", &T);
    forn(i,T){
        printf("Case #%d: ", i+1);
        solve();
        printf("\n");
    }
}