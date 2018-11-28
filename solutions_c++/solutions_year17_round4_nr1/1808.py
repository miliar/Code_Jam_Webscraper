/********************************
*MAHBUBCSEJU                    *
*CSE 22                         *
*JAHANGIRNAGAR UNIVERSITY       *
*TIMUS:164273FU                 *
*UVA>>LIGHTOJ>>HUST:mahbubcseju */
#include<bits/stdc++.h>
#define ll long long int
#define ull unsigned long long int
#define I(a) scanf("%d",&a)
#define I2(a,b) scanf("%d%d",&a,&b)
#define I3(a,b,c) scanf("%d%d%d",&a,&b,&c)
#define L(a) scanf("%lld",&a)
#define L2(a,b) scanf("%lld%lld",&a,&b)
#define L3(a,b,c) scanf("%lld%lld%lld",&a,&b,&c)
#define PI(a) printf("%d",a)
#define PL(a) printf("%lld",a)
#define PT(t) printf("Case %d: ",t)
#define PB push_back
#define x first
#define y second
#define xx first.first
#define xy first.second
#define yx second.first
#define yy second.second
#define SC scanf
#define PC printf
#define NL printf("\n")
#define SET(a) memset(a,0,sizeof a)
#define SETR(a) memset(a,-1,sizeof a)
#define SZ(a) ((int)a.size())-1
#define f(i,a,b) for(int i=a;i<=b; i++)
#define fr(i,a,b) for(int i=a;i<=b; i++)
#define frr(i,a,b) for(int i=a;i>=b; i--)
#define frv(i,a)  for(int i=0;i<a.size();i++)
//#define pi 2.0*acos(0.0)
#define R(a) freopen(a, "r", stdin);
#define W(a) freopen(a, "w", stdout);
#define CB(x) __builtin_popcount(x)
#define STN(a) stringtonumber<ll>(a)
#define lol printf("BUG\n")
#define Endl "\n"
#define mk make_pair
using namespace std;
template <class T> inline T BM(T p, T e, T M)
{
    ll ret = 1;
    for (; e > 0; e >>= 1)
    {
        if (e & 1) ret = (ret * p) % M;
        p = (p * p) % M;
    }
    return (T)ret;
}
template <class T> inline T gcd(T a, T b)
{
    if (b == 0)return a;
    return gcd(b, a % b);
}
template <class T> inline T mdINV(T a, T M)
{
    return BM(a, M - 2, M);
}
template <class T> inline T PW(T p, T e)
{
    ll ret = 1;
    for (; e > 0; e >>= 1)
    {
        if (e & 1) ret = (ret * p);
        p = (p * p);
    }
    return (T)ret;
}
template <class T>string NTS ( T Number )
{
    stringstream ss;
    ss << Number;
    return ss.str();
}
template <class T>T stringtonumber ( const string &Text )
{
    istringstream ss(Text);
    T result;
    return ss >> result ? result : 0;
}
template <class T>bool ISLEFT ( T a, T b, T c)
{
    if (((a.xx - b.xx) * (b.yy - c.yy) - (b.xx - c.xx) * (a.yy - b.yy)) < 0.0)return 1; //Uporer dike //A,b,c, x okkher ordera sorted
    else return 0;
}
#define mx 300000ll
#define md 23377788ll
#define md1 1000000007ll
#define maxp 2050180000
#define LO(X) X[p][k]
#define base 29

typedef pair<int,int >P;
//////////////////////////
/////////////////////////

int dp[102][102][102][4];

int go(int i,int j,int k,int op)
{
    if(i+j+k==0)return 0;


    int &ret=dp[i][j][k][op];
    if(ret!=-1)return ret;
    ret=0;
    int x=0;
    if(op==0)x=1;

    if(i>0)
    ret=max(ret,x+go(i-1,j,k,op));

    if(j>0)
    ret=max(ret,x+go(i,j-1,k,(op+1)%2));

    if(k>0)
    ret=max(ret,x+go(i,j,k-1,(op+2)%2));

    return ret;

}
int dp1[102][102][102][4];

int go1(int i,int j,int k,int op)
{
    if(i+j+k==0)return 0;


    int &ret=dp1[i][j][k][op];
    if(ret!=-1)return ret;
    ret=0;
    int x=0;
    if(op==0)x=1;

    if(i>0)
    ret=max(ret,x+go1(i-1,j,k,op));

    if(j>0)
    ret=max(ret,x+go1(i,j-1,k,(op+1)%3));

    if(k>0)
    ret=max(ret,x+go1(i,j,k-1,(op+2)%3));

    return ret;

}


int main()
{

    R("in.txt");
    W("out.txt");
    SETR(dp);
    SETR(dp1);

    int tc,cs=0;
    I(tc);
    while(tc--)
    {
        int ar[5];
        SET(ar);
        int n,m;
        I2(n,m);
        for(int i=1;i<=n;i++)
        {
            int x;
            I(x);
            ar[x%m]++;
        }
        int ans=0;

        if(m==2)
           ans=go(ar[0],ar[1],ar[2],0);
            if(m==3)
          ans=go1(ar[0],ar[1],ar[2],0);

        PC("Case #%d: %d\n",++cs,ans);
    }

    return 0;
}
