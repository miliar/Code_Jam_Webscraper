

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
char s[100][100];
 int mark[200];
 int n,m;
void f(int x, int y){
    mark[s[x][y]]=1;
     int r=y;
      r++;
    while(s[x][r]=='?'&&r<m) s[x][r]=s[x][y],r++;
    int l=y;
    l--;
    while(s[x][l]=='?'&&l>=0) s[x][l]=s[x][y],l--;
    for(int i=x+1;i<n;i++){
         bool flag=0;
        FOR(j,l+1,r){
            if(s[i][j]!='?') flag=1;
        }
        if(flag) break;
         FOR(j,l+1,r){
            s[i][j]=s[x][y];
        }
    }
     for(int i=x-1;i>=0;i--){
         bool flag=0;
        FOR(j,l+1,r){
            if(s[i][j]!='?') flag=1;
        }
        if(flag) break;
         FOR(j,l+1,r){
            s[i][j]=s[x][y];
        }
    }
}
int main()
{
#ifdef sayed
    // freopen("in.txt","r",stdin);

#endif
    //ios_base::sync_with_stdio(false);
    //cin.tie(0);
    freopen("out.txt","w",stdout);
   int test=nxt();
   int cs=1;
   while(test--){

        n=nxt();
        m=nxt();
       FOR(i,0,n) scanf("%s",s[i]);
       bool flag=0;
       FOR(i,0,n){
         FOR(j,0,m){
           if(s[i][j]!='?'&&mark[s[i][j]]==0){
             f(i,j);
             flag=1;
           }
         }
       }
       printf("Case #%d:\n",cs++);
       if(!flag){
        FOR(i,0,n) {
        FOR(j,0,m) printf("A");
        printf("\n");
        }

       } else {
          FOR(i,0,n){
           FOR(j,0,m){
            printf("%c",s[i][j]);
           }
           printf("\n");
          }
       }
   CLR(mark);
   }
    return 0;
}
