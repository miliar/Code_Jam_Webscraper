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

int _,d,n;

int k[10000],s[10000];

bool check(double x){
    double t = 1.0*d/x;
    for(int i=1;i<=n;i++){
        if(t*s[i]+k[i] + 1e-8 <=d*1.0) return false;
    }
    return true;
}

int main(){
    freopen("A-large (1).in","r",stdin);
    freopen("A-large (1).txt","w",stdout);
    int kcase = 0;
    scanf("%d",&_);
    while(_--){
        scanf("%d%d",&d,&n);
        for(int i=1;i<=n;i++)       scanf("%d%d",&k[i],&s[i]);

        double l=0,r=1e15,mid;
        for(int i=0;i<300;i++){
            mid = (r+l)/2;
            if(check(mid))l=mid;
            else  r=mid;
        }
        printf("Case #%d: ",++kcase);
        printf("%.6lf\n",l);
    }

    return 0;
}
