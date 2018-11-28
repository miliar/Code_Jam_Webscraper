#include <bits/stdc++.h>
using namespace std;

#define INF        (~(1<<31))
#define INFLL      (~(1ll<<63))
#define pb         push_back
#define mp         make_pair
#define abs(a)     ((a)>0?(a):-(a))
#define lalal      puts("*******");
#define s1(x)      scanf("%d",&x)
#define Rep(a,b,c) for(int a=(b);a<=(c);a++)
#define Per(a,b,c) for(int a=(b);a>=(c);a--)
#define no         puts("NO")

typedef long long int LL ;
typedef unsigned long long int uLL ;

const int    MOD = 1e9+7;
const int    N   = 50000+5;
const double eps = 1e-6;
const double PI  = acos(-1.0);
void fre()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
}
inline int Rint()
{
    int x=0,f=1;
    char ch=getchar();
    while('0'>ch||ch>'9'){if(ch=='-') f=-1;ch=getchar();}
    while('0'<=ch&&ch<='0'){x=x*10+ch-'0'; ch=getchar();}
    return x*f;
}
inline LL RLL()
{
    LL x=0,f=1;
    char ch=getchar();
    while('0'>ch||ch>'9'){if(ch=='-') f=-1;ch=getchar();}
    while('0'<=ch&&ch<='0'){x=x*10+ch-'0'; ch=getchar();}
    return x*f;
}
/***********************************************************************/

int _,n,q;
double d[111],d2[111],s[111],dp[111];
double a[111],sum[111];
int main(){
    freopen("C-small-attempt0.in","r",stdin);
    freopen("C-small-attempt0.txt","w",stdout);

    int kcase = 0;
    scanf("%d",&_);
    while(_--){
        scanf("%d%d",&n,&q);

        for(int i=1;i<=n;i++){
            scanf("%lf%lf",&d[i],&s[i]);
            d2[i]=d[i];
        }
        LL x;
        for(int i=1;i<=n;i++){
            for(int j=1;j<=n;j++){
                scanf("%lld",&x);
                if(i+1==j){
                    a[i]=1.0*x;
                }
            }
        }
        scanf("%lld %lld",&x,&x);

//        for(int i=1;i<n;i++)  printf("%d ",a[i]);puts("---");

        double ans1=0,ans2=0;
        dp[1]=0;
        sum[1]=0;
        for(int i=2;i<=n;i++){
            dp[i]=1e14;
            sum[i]=sum[i-1]+a[i-1];
//            printf("%d ",sum[i]);
            for(int j=1;j<i;j++){
                if(d[j]>=sum[i]-sum[j]){
                    dp[i]=min(dp[i],dp[j]+1.0*max(0.0,(sum[i]-sum[j]))/s[j]);
                }
            }
//            printf("%.6lf ",dp[i]);
        }
//        puts("");

        printf("Case #%d: ",++kcase);
        printf("%.6lf\n",dp[n]);
    }

    return 0;
}
/**
3
3 1
2 3
2 4
4 4
-1 1 -1
-1 -1 1
-1 -1 -1
1 3
4 1
13 10
1 1000
10 8
5 5
-1 1 -1 -1
-1 -1 1 -1
-1 -1 -1 10
-1 -1 -1 -1
1 4
*/
