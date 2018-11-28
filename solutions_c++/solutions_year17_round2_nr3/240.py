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

const int MXN = 110;
const double dinf = 1e18;
const ll linf = 1e18;

int s [MXN];
int e [MXN];

ll d [MXN][MXN];
double dd [MXN][MXN];

void solve() {
    int n,q;
    scanf("%d%d", &n, &q);
    forn(i,n) {
        scanf("%d%d", &e[i], &s[i]);
    }
    forn(i,n) {
        forn(j,n) {
            scanf("%lld", &d[i][j]);
            if (d[i][j] == -1) {
                d[i][j] = linf;
            }
        }
    }

    forn(k,n) {
        forn(i,n) {
            forn(j,n) {
                d[i][j] = min(d[i][j], d[i][k] + d[k][j]);
            }
        }
    }
    forn(i,n) { 
        forn(j,n) {
            dd[i][j] = d[i][j] > e[i] ? dinf : 1.0 * d[i][j] / s[i];
        }
    }
    forn(k,n) {
        forn(i,n) {
            forn(j,n) {
                dd[i][j] = min(dd[i][j], dd[i][k] + dd[k][j]);
            }
        }
    }
    forn(i,q) {
        if (i) printf(" ");
        int a, b;
        scanf("%d%d", &a, &b);
        printf("%.15f", dd[a-1][b-1]);
    }
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