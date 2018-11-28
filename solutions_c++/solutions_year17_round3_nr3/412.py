#include <bits/stdc++.h>
using namespace std;
#define D(x) cerr<<#x " = "<<(x)<<endl
#define pb push_back
#define ff first
#define ss second
#define mem(a) memset(a,0,sizeof(a))
#define _set(a) memset(a,-1,sizeof(a))
typedef long long int ll;
typedef unsigned long long ull;
typedef pair<int,int> pii;
typedef pair<ll,ll> pll;
#define eps 1e-9
#define MAX 100000
#define MAXL 20
#define MAXE 100000
#define inf 100000000
#define pi acos(-1.0)
//ll mod = 1000000000+7;
//int dx[] = {0,0,1,-1};
//int dy[] = {1,-1,0,0};
//int dx[] = {-1,-1,-1,0,0,1,1,1};
//int dy[] = {-1,0,1,-1,1,-1,0,1};

double prb[100];
int main() {
    freopen("C-small-1-attempt0.in", "r", stdin);
    freopen("output.out", "w", stdout);
    //ios_base::sync_with_stdio(false);

    int ncase, tcase = 1, i, n, k;
    scanf("%d", &ncase);
    while(ncase--) {
        scanf("%d %d", &n, &k);
        double u;
        scanf("%lf", &u);
        for(i = 0; i < n; i++) scanf("%lf", &prb[i]);
        prb[i] = 1.0;
        n++;
        sort(prb, prb+n);
        double ans = 1.0;
        for(i = 0; i+1 < n; i++)
        {
            double req = (prb[i+1]-prb[i])*(i+1);
            if(req <= u+eps) u -= req;
            else {
                double add = u/(i+1);
                for(int j = 0; j <= i; j++) {
                    ans *= (prb[i]+add);
                }
                break;
            }
            //D(u);
        }
        //D(u);
        for(i++; i < n; i++) ans *= prb[i];
        printf("Case #%d: %0.10lf\n", tcase++, ans);
    }
    return 0;
}


