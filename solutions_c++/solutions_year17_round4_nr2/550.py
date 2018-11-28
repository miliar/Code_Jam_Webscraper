
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
#define IN freopen("B.in", "r", stdin)
#define OUT freopen("B.out", "w", stdout)
#define scan(x) scanf("%d", &x)
#define mp make_pair
#define pb push_back
#define sqr(x) (x) * (x)
#define pr(x) printf("Case %d: ",x)
#define prn(x) printf("Case %d:\n",x)
#define prr(x) printf("Case #%d: ",x)
#define prrn(x) printf("Case #%d:\n",x)
#define lowbit(x) (x&(-x))

int a[1005],b[1005];
int T,n,c,m;

int check(int v)
{
    int ret=0,ss=0;
    for(int i=1;i<=n;i++)
    {
        ss+=a[i];
        if(ss>i*v)return -1;
        ret+=max(0,a[i]-v);
    }
    return ret;
}

int main()
{
    IN;OUT;
    scanf("%d",&T);
    for(int t=1;t<=T;t++)
    {
        int ma=0;
        scanf("%d%d%d",&n,&c,&m);
        for(int i=0;i<=1000;i++)a[i]=b[i]=0;
        for(int i=1;i<=m;i++)
        {
            int x,y;
            scanf("%d%d",&x,&y);
            a[x]++;b[y]++;
            ma=max(b[y],ma);
        }
        int l=ma,r=m;
        while(r-l>1)
        {
            int mid=(l+r)>>1;
            if(check(mid)>=0)r=mid;else l=mid;
        }
        if(check(l)<0)l++;
        prr(t);
        printf("%d %d\n",l,check(l));
    }
    return 0;
}
