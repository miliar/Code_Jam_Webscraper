
/*****************************************
Author: lizi
Email: lzy960601@outlook.com
****************************************/
  
#include<bits/stdc++.h>
  
using namespace std;
  
const double eps=1e-10;
const double pi=3.1415926535897932384626433832795;
const double eln=2.718281828459045235360287471352;
  
#define LL long long
#define IN freopen("gb.in", "r", stdin)
#define OUT freopen("gb.out", "w", stdout)
#define scan(x) scanf("%d", &x)
#define mp make_pair
#define pb push_back
#define sqr(x) (x) * (x)
#define pr(x) printf("Case %d: ",x)
#define prn(x) printf("Case %d:\n",x)
#define prr(x) printf("Case #%d: ",x)
#define prrn(x) printf("Case #%d:\n",x)
#define lowbit(x) (x&(-x))
 
vector<int> a[55];
int T;
int n,p;
vector<int> nd;
int pos[55];

int main()
{
    IN;OUT;
    scanf("%d",&T);
    for(int _=1;_<=T;_++)
    {
        scanf("%d%d",&n,&p);
        nd.clear();nd.pb(0);
        for(int i=1;i<=n;i++)
        {
            int x;
            scanf("%d",&x);
            nd.pb(x);
        }
        for(int i=1;i<=n;i++)
        {
            a[i].clear();a[i].pb(0);
            for(int j=1;j<=p;j++)
            {
                int x;
                scanf("%d",&x);
                a[i].pb(x);
            }
            sort(a[i].begin(),a[i].end());
        }
        int tot=0;prr(_);
        for(int i=1;i<=n;i++)pos[i]=1;
        for(int num=1;num<=1e6;num++)
        {
            bool f=true;
            for(int i=1;i<=n;i++)
            {
                while(pos[i]<=p && 1ll*a[i][pos[i]]*10<1ll*nd[i]*num*9)pos[i]++;
                if(pos[i]>p){f=false;break;}
            }
            if(!f)break;
            for(int i=1;i<=n;i++)
            {
                if(1ll*a[i][pos[i]]*10>1ll*nd[i]*num*11)
                {f=false;break;}
            }
            if(!f)continue;
            tot++;
            for(int i=1;i<=n;i++)pos[i]++;
            num--;
        }
        printf("%d\n",tot);
    }
    return 0;
}
