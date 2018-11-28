

#include<bits/stdc++.h>

using namespace std;
#define xx first
#define yy second
#define pb push_back
#define mp make_pair
typedef long long i64;

#define mod 1000000007LL



template<class T>T Bitcnt(T a){int sum=0;while(a){if(a&1)sum++;a/=2;}return sum;}
template<class T>T Max3(T a,T b,T c){return max(a,max(b,c));}
template<class T>T Lcm(T a,T b){T tmp=__gcd(a,b);return (a/tmp)*b;}
template<class T> T Pow(T a,T b){T ans=1;T base=a;while(b){if(b&1)ans=(ans*base);base=(base*base);b/=2;}return ans;}


i64 Bigmod(i64 a,i64 b)
{

    i64 res=1;
    i64 pw=a%mod;
    while(b>0)
    {
       if(b&1)res=(res*pw)%mod;
       pw=(pw*pw)%mod;
       b/=2;
    }
    return res;
}


#define s1(a) scanf("%d",&a)
#define s2(a,b) scanf("%d %d",&a,&b)
#define s3(a,b,c) scanf("%d %d %d",&a,&b,&c)
#define sl1(a) scanf("%lld",&a)
#define sl2(a,b) scanf("%lld %lld",&a,&b)
#define sl3(a,b,c) scanf("%lld %lld %lld",&a,&b,&c)
#define p1(a) printf("%d",a)
#define p2(a,b) printf("%d %d",&a,&b)
#define NL printf("\n")
#define N 4000000
#define rep(i,a,b)    for(int i=a;i<=b;i++)
#define rrep(i,b,a)   for(int i=b;i>=a;i--)
#define fs(i,a,s)     for(int i=a;s[i];i++)

int a_x[]={1,-1,0,0};
int a_y[]={0,0,1,-1};
i64 X,Y;

void extend_euclid(i64 a,i64 b)
{
    if(b==0)
    {
        X=1;Y=0;return;
    }
    extend_euclid(b,a%b);
    i64 x,y;
    x=Y;
    y=X-(a/b)*Y;
    X=x;
    Y=y;
}



i64 inverse_modulo(i64 a,i64 b)
{
    extend_euclid(a,b);
    return (X+mod)%mod;
}

int mn[]={0,31,28,31,30,31,30,31,31,30,31,30,31};
#define PI acos(-1.0)

pair<i64,i64>lst[1005];
int k,n;

bool cmp(pair<i64,i64>a,pair<i64,i64>b )
{
    return a.xx>b.xx;
}

double dp[1001][1001];
bool visit[1001][1001];


double solve(int pos,int rem)
{
   if(rem==0)
    return 0.0;
    if(pos<0)
    {
        return (-1e16);
    }
    double &ret=dp[pos][rem];
     if(visit[pos][rem])
        return ret;
        visit[pos][rem]=1;
    ret=-1e16;
    double tmp=PI*lst[pos].xx*lst[pos].xx+2*PI*1.0*lst[pos].xx*lst[pos].yy;
    double val=solve(pos-1,rem-1);
    //cout<<val<<endl;
    if(rem!=1)ret=max(ret,tmp+val-PI*lst[pos].xx*1.0*lst[pos].xx);
    else ret=max(ret,tmp+val);
    ret=max(ret,solve(pos-1,rem));
    ret=max(ret,-1e16);
    return ret;

}
int main()
{

   freopen("input.txt","r",stdin);
   freopen("output.txt","w",stdout);

   int test;
   scanf("%d",&test);
    rep(ca,1,test)
    {
         scanf("%d %d",&n,&k);
         for(int i=0;i<n;i++)
            scanf("%lld %lld",&lst[i].xx,&lst[i].yy);
         sort(lst,lst+n,cmp);

        memset(visit,0,sizeof visit);
        double res=solve(n-1,k);

        printf("Case #%d: %.16lf\n",ca,res);
    }



    return 0;
}




