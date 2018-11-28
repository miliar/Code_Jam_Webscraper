
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

const int N=55;
const double eps=1e-7;
double a[N];
int n,uu;
int aa[N];

bool check(int m) {
    int tt=uu;
    for(int i=1;i<=n;++i) {
        if(aa[i]<m) tt=tt-(m-aa[i]);
    }
    return tt>=0;
}

int main() {
    freopen("C-small-1-attempt1.in","r",stdin);
    freopen("xx.out","w",stdout);
    int T;scanf("%d",&T);
    int ca=0;
    while(T--) {
        printf("Case #%d: ",++ca);
        ///
        int k;scanf("%d%d",&n,&k);

        ///read
        double u;scanf("%lf",&u);
        uu=(u+eps)*10000;uu=uu*1000;
        for(int i=1;i<=n;++i) {
            scanf("%lf",a+i);
            aa[i]=(a[i]+eps)*10000;aa[i]=aa[i]*1000;
        }

        ///solve
        int l=0,r=10000000,ans=-1;
        while(l<=r) {
            int m=(l+r)>>1;
            if(check(m)) {
                ans=m;
                l=m+1;
            } else {
                r=m-1;
            }
        }

        for(int i=1;i<=n;++i) {
            if(aa[i]<ans) {
                uu=uu-(ans-aa[i]);
                aa[i]=ans;
            }
        }
        sort(aa+1,aa+1+n);
        for(int i=n;i>=1&&uu>0;--i) {
            ++aa[i];
            --uu;
        }

        double res=1;
        for(int i=1;i<=n;++i) {
            res=res*aa[i]/10000000;
        }

        ///print
        printf("%.6lf\n",res);

    }
    return 0;
}
