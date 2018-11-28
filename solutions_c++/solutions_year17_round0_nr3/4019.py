


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
int limit;
struct info{
   int l,r,diff;
   info(int a,int b,int c){
      l=a;
      r=b;
      diff=c;
    }
};
bool operator<(info x,info y){
   if(x.diff<y.diff) return true;
   else if(x.diff==y.diff){
       if(x.l>y.l) return true;
       return false;
   }
   return false;
}
void bfs(int n){

     int c=0;
     priority_queue<info> pq;
     pq.push(info(1,n,0));

     while(!pq.empty()){
         int b=pq.top().l;
         int e=pq.top().r;
          pq.pop();
         int mid=(b+e)/2;
         c++;
           if(c==limit){
            //     debug(b);
          // debug(e);
                cout<<max(mid-b,e-mid)<<" "<<min(mid-b,e-mid)<<endl;
                return;
            }
         int x,y;
         x=mid+1;y=e;
         int t=(x+y)/2;
         if(x<=y) pq.push(info(x,y,y-x+1));
         x=b;y=mid-1;
         t=(x+y)/2;
         if(x<=y) pq.push(info(x,y,(y-x+1)));

     }
     //puts("b");
  }
int main()
{
#ifdef sayed
    // freopen("in.txt","r",stdin);
    freopen("temp.txt","w",stdout);
#endif
    //ios_base::sync_with_stdio(false);
    //cin.tie(0);
   int test=nxt();
   int cs=1;
   while(test--){
       int n=nxt();
       limit=nxt();
       printf("Case #%d: ",cs++);
       bfs(n);

   }
    return 0;
}
