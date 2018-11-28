//Bismillahir Rahmanir Rahim

#include<bits/stdc++.h>
using namespace std;

#define i64 long long int
#define u64 unsigned long long int
#define fin(a) freopen(a,"r",stdin)
#define fout(a) freopen(a,"w",stdout)
#define repc(i,a,b) for(__typeof(b) i=(a); i<=(b); i++)
#define repr(i,a,b) for(__typeof(b) i=(a); i>=(b); i--)
#define clr(a) a.clear()
#define sz(a) (int)a.size()
#define mem(a,b) memset(a,b,sizeof a)
#define ERASE(a) a.erase(a.begin(),a.end())

#define sc scanf
#define S(z) scanf("%d",&z)
#define SL(z) scanf("%I64d",&z)
#define S2(xx,zz) scanf("%d %d",&xx,&zz)
#define SL2(xx,zz) scanf("%I64d %I64d",&xx,&zz)
#define SC(z) scanf("%s",&z)

#define pf printf
#define pfn printf("\n")
#define pfs printf(" ")
#define PF(z) printf("%d",z)
#define PFL(z) printf("%I64d",z)
#define PF2(x,y) printf("%d %d",x,y)
#define PFS(z) printf("%s",z)
#define ff first
#define ss second
#define mp make_pair
#define pb push_back
#define inf 2000000007
#define pi  acos(-1.0)
#define MAX 200007
#define MOD 1000000007LL
#define eps 1e-11

template <class T>T sqr(T x) {return x*x;}
template< class T > T gcd(T a, T b) { return (b != 0 ? gcd<T>(b, a%b) : a); }
template< class T > T lcm(T a, T b) { return (a / gcd<T>(a, b) * b); }
template <class T> inline T bigmod(T p,T e,T M)
{
    if(e==0) return 1;
    if(e%2==0){i64 t=bigmod(p,e/2,M);return (T)((t*t)%M);}
    return (T)((i64)bigmod(p,e-1,M)*(i64)p)%M;
}
template <class T> inline T bigexp(T p,T e)
{
    if(e==0)return 1;
    if(e%2==0){i64 t=bigexp(p,e/2);return (T)((t*t));}
    return (T)((i64)bigexp(p,e-1)*(i64)p);
}
template <class T> inline T modinverse(T a,T M){return bigmod(a,M-2,M);}

int dx4[]={1,0,-1,0};int dy4[]={0,1,0,-1}; //4 Direction
int dx8[]={1,1,0,-1,-1,-1,0,1};int dy8[]={0,1,1,1,0,-1,-1,-1};//8 direction
int nx8[]={1,1,-1,-1,2,2,-2,-2};int ny8[]={2,-2,2,-2,1,-1,1,-1};//8 direction
int month[]={31,28,31,30,31,30,31,31,30,31,30,31};
/*
struct Graph
{
    int u,v,w;
    bool operator<(const Graph& p)
    const {return w<p.w;} // oporerta chotor jnne
}edge[10];
struct compare
{
    bool operator()(const int&l,const int&r)
    {
        return l>r;
    }
};
priority_queue<int,vector<int>,compare>pq;

i64 ncr[1005][1005];
void nCr()
{
    repc(i,0,1002) ncr[i][0]=1LL;
    repc(i,1,1002)
    repc(j,1,i)
    ncr[i][j]=(ncr[i-1][j-1]+ncr[i-1][j])%MOD;
}



/******************* Code Starts here *******************/

int t,n,r,o,y,g,b,v,f,co;

void call(int r, int y, int b, int id)
{
    if(r==0 && y==0 && b==0) return;
    if(id==2)
    {
       if(r>b)
       {
          pf("R"); r--; id=1;

       }
       else if(r<b)
       {
            pf("B"); b--; id=3;
       }
       else if(r==b)
       {
          if(f==3)
          {
              pf("B"); b--; id=3;
          }
          else
          {
            pf("R"); r--; id=1;
          }
       }
    }
    else if(id==1)
    {
        if(y>b)
       {
          pf("Y"); y--; id=2;

       }
       else if(y<b)
       {
            pf("B"); b--; id=3;
       }
       else if(y==b)
       {
          if(f==3)
          {
              pf("B"); b--; id=3;
          }
          else
          {
            pf("Y"); y--; id=2;
          }
       }
    }
    else if(id==3)
    {
        if(y>r)
       {
          pf("Y"); y--; id=2;

       }
       else if(y<r)
       {
            pf("R"); r--; id=1;
       }
       else if(y==r)
       {
          if(f==1)
          {
              pf("R"); r--; id=1;
          }
          else
          {
            pf("Y"); y--; id=2;
          }
       }
    }
    call(r,y,b,id);
    return ;
}
int main()
{
    fin("B-small-attempt0.in");
    fout("B_small.txt");
     S(t);

     while(t--)
     {
         S(n);
         S(r);
         S(o);
         S(y);S(g);S(b);S(v);
         int mx=0;
         mx=max(r,mx);
         mx=max(y,mx);
         mx=max(b,mx);
         pf("Case #%d: ",++co);
         if(r+y<b || r+b<y || y+b<r)
         {
            pf("IMPOSSIBLE");
         }
         else
         {
             int id=0;
             if(mx==r) id=1;
             if(mx==y) id=2;
             if(mx==b) id=3;
             if(id==1) {pf("R"); r--;f=1;}
             else if(id==2){ pf("Y"); y--;f=2;}
             else if(id==3){ pf("B"); b--;f=3;}
             call(r,y,b,id);
         }

         pfn;
     }
    return 0;
}

