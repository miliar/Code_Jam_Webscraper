

//==========================================================================
//
//                   Bismillahir-Rahmanir-Rahim
//
// ==========================================================================
#include <bits/stdc++.h>
#define        ll                              long long int
#define        FOR(x,y,z)                      for(int x=y;x<z;x++)
#define        pii                             pair<int,int>
#define        pll                             pair<ll,ll>
#define        CLR(a)                          memset(a,0,sizeof(a))
#define        SET(a)                          memset(a,-1,sizeof(a))
#define        N                               100010
#define        M                               1000000007
#define        pi                              acos(-1.0)
#define        ff                              first
#define        ss                              second
#define        pb                              push_back
#define        inf                             (int)1e9
#define        eps                             1e-9
#define        debug(x)                        cerr << #x << " is " << x << endl;
#define        ALL(x)                          x.begin(),x.end()
using namespace std;
int dx[]={0,0,1,-1,-1,-1,1,1};
int dy[]={1,-1,0,0,-1,1,1,-1};
template < class T> inline T biton(T n,T pos){return n |((T)1<<pos);}
template < class T> inline T bitoff(T n,T pos){return n & ~((T)1<<pos);}
template < class T> inline T ison(T n,T pos){return (bool)(n & ((T)1<<pos));}
template < class T> inline T gcd(T a, T b){while(b){a%=b;swap(a,b);}return a;}
template <typename T> string NumberToString ( T Number ) { ostringstream ss; ss << Number; return ss.str(); }
inline int nxt(){int aaa;scanf("%d",&aaa);return aaa;}
inline ll lxt(){ll aaa;scanf("%I64d",&aaa);return aaa;}
inline double dxt(){double aaa;scanf("%lf",&aaa);return aaa;}
template <class T> inline T bigmod(T p,T e,T m){T ret = 1;
for(; e > 0; e >>= 1){
    if(e & 1) ret = (ret * p) % m;p = (p * p) % m;
} return (T)ret;}
///******************************************START******************************************
int ar[N];
int main()
{
#ifdef sayed
    // freopen("in.txt","r",stdin);
    freopen("Alarge.txt","w",stdout);
#endif
    //ios_base::sync_with_stdio(false);
    //cin.tie(0);
      int n=nxt(); int cs=1;
      FOR(i,0,n){
         string s;
         cin>>s; int c=0;
           int k=nxt();
         FOR(i,0,s.length()){
           if(s[i]=='-'&&i+k-1<s.length()){
                FOR(j,0,k){
                    if(s[i+j]=='-') s[i+j]='+';
                    else s[i+j]='-';
                }
                c++;
           }
         }
         bool f=0;
         FOR(i,0,s.length()) if(s[i]=='-') f=1;
         printf("Case #%d: ",cs++);
         if(f) puts("IMPOSSIBLE");
         else printf("%d\n",c);
      }
    return 0;
}
