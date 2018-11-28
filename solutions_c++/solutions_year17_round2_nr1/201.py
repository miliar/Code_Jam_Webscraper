#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
using namespace std;
const int N=1200;
int T_T;
int n;
double dis;
double k[N],s[N];
template <typename T>inline void read(T &x)
{
    x=0;bool f=false;char ch=getchar();
    while (ch<'0'||'9'<ch) {if (ch=='-') f=!f;ch=getchar();}
    while ('0'<=ch&&ch<='9') {x=x*10+ch-'0';ch=getchar();}
    if (f) x=-x;
}
int main()
{
    #ifdef VGel
    freopen("A-large.in","r",stdin);
    freopen("AA.out","w",stdout);
    #endif VGel
    read(T_T);
    for (int T=1;T<=T_T;T++)
    {
        scanf("%lf",&dis);read(n);
        for (int i=1;i<=n;i++) scanf("%lf%lf",&k[i],&s[i]);
        double ans=0.0;
        for (int i=1;i<=n;i++)
            ans=max(ans,(dis-k[i])/s[i]);
        printf("Case #%d: %.12lf\n",T,dis/ans);
    }
    return 0;
}
