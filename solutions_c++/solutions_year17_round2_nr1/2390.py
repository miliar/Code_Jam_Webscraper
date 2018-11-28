#include <bits/stdc++.h>
typedef long long ll;
using namespace std;
#define debug(a) cout<<a<<endl
#define clr(a) memset(a,0,sizeof(a))
#define clrne(a) memset(a,-1,sizeof(a))
#define clrinf(a) memset(a,0x3f,sizeof(a))
#define clrneinf(a) memset(a,0xc0,sizeof(a))
#define pb(a) push_back(a)
#define maxn 100
#define mod 1000000007
#define eps 1e-9
#define inf 0x7fffffff
int main()
{
  freopen("in.txt","r",stdin);
  freopen("out.txt","w",stdout);
    int T;
    scanf("%d",&T);
    int caseno = 0;
    while (T--)
    {
        double ans = 0;
        double d;
        int n;
        scanf("%lf%d",&d,&n);
        while (n--)
        {
            double k,s;
            scanf("%lf%lf",&k,&s);
            k = d-k;
            if (k<=d)
                ans = max(ans,k/s);
        }
        printf("Case #%d: %f\n",++caseno,d/ans);
    }
    return 0;
}
