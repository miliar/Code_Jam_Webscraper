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
#define eps 1e-9
#define MAX 100000
#define MAXL 20
#define MAXE 100000
#define inf (1<<30)
//ll mod = 1000000000+7;
//int dx[] = {0,0,1,-1};
//int dy[] = {1,-1,0,0};
//int dx[] = {-1,-1,-1,0,0,1,1,1};
//int dy[] = {-1,0,1,-1,1,-1,0,1};
int k[1005], s[1005];

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("output.out", "w", stdout);
    //ios_base::sync_with_stdio(false);
    int ncase, tcase = 1, d, n, i;
    scanf("%d", &ncase);
    while(ncase--)
    {
        scanf("%d %d", &d, &n);
        double ans = 1e18;
        for(i = 0; i < n; i++)
        {
            scanf("%d %d", &k[i], &s[i]);
            double sp = (1.0*d)/((1.0*(d-k[i]))/s[i]);
            ans = min(ans, sp);
        }
        printf("Case #%d: %.10f\n", tcase++, ans);

    }
    return 0;
}



