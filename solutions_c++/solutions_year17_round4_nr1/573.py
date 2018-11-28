
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
#define IN freopen("A.in", "r", stdin)
#define OUT freopen("A.out", "w", stdout)
#define scan(x) scanf("%d", &x)
#define mp make_pair
#define pb push_back
#define sqr(x) (x) * (x)
#define pr(x) printf("Case %d: ",x)
#define prn(x) printf("Case %d:\n",x)
#define prr(x) printf("Case #%d: ",x)
#define prrn(x) printf("Case #%d:\n",x)
#define lowbit(x) (x&(-x))

int T,n,p;
int a[5];

int main()
{
    IN;OUT;
    scanf("%d",&T);
    for(int t=1;t<=T;t++)
    {
        scanf("%d%d",&n,&p);
        a[0]=a[1]=a[2]=a[3]=0;
        for(int i=1;i<=n;i++)
        {
            int x;
            scanf("%d",&x);
            a[x%p]++;
        }
        int ans=a[0],sum=0;
        if(p==2)
        {
            sum=(a[1]+1)>>1;
        }
        if(p==3)
        {
            int v=min(a[1],a[2]),u=a[1]+a[2];
            sum=v;
            u-=2*v;
            sum+=(u+2)/3;
        }
        if(p==4)
        {
            sum=(a[2]+1)>>1;
            int v=min(a[1],a[3]);
            sum+=v;
            a[1]-=v;a[3]-=v;
            int u=a[1]+a[3];
            if((a[2]&1)==0)
            {
                sum+=(u+3)>>2;
            }else
            {
                if(u>2)u-=2;
                sum+=(u+3)>>2;
            }
        }
        prr(t);
        printf("%d\n",ans+sum);
    }
    return 0;
}
