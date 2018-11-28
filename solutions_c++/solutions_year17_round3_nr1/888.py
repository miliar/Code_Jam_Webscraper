
#include <algorithm>
#include <iostream>
#include <cstring>
#include <vector>
#include <cstdio>
#include <string>
#include <cmath>
#include <queue>
#include <set>
#include <map>
using namespace std;
typedef long long ll;
typedef unsigned long long ull;
typedef pair<int,int> pii;
typedef pair<ll,ll> pll;
#define mp make_pair
#define pb push_back
#define fi first
#define se second
#define lson l,m,rt<<1
#define rson m+1,r,rt<<1|1
#define de(x) cout << #x << "=" << x << endl

const double pi=acos(-1);
const int N=1005;
double d[N][N],Max[N][N];

struct Node {
    int r,h;
    bool operator < (const Node &tmp) const {
        if(r==tmp.r) return h<tmp.h;
        return r<tmp.r;
    }
}a[N];

int main() {
    freopen("A-large.in","r",stdin);
    freopen("xx.out","w",stdout);
    int T;scanf("%d",&T);
    int ca=0;
    while(T--) {
        printf("Case #%d: ",++ca);
        ///
        int n,k;scanf("%d%d",&n,&k);

        ///read
        for(int i=1;i<=n;++i) scanf("%d%d",&a[i].r,&a[i].h);

        ///init
        memset(Max,0,sizeof(Max));

        ///sort
        sort(a+1,a+1+n);

        ///solve
        for(int i=1;i<=n;++i) {
            for(int j=1;j<=k;++j) {
                d[i][j]=2*pi*a[i].r*a[i].h+Max[i-1][j-1];
                Max[i][j]=fmax(d[i][j],Max[i-1][j]);
            }
        }

        ///get ans
        double ans=0;
        for(int i=1;i<=n;++i) {
            ans=fmax(ans,d[i][k]+pi*a[i].r*a[i].r);
        }

        ///print
        printf("%.9lf\n",ans);
    }
    return 0;
}
