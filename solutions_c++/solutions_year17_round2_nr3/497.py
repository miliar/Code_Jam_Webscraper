#include<bits/stdc++.h>
using namespace std;
/*------- Constants---- */

#define Long                    long long
#define Ulong                   unsigned long long
#define FOR(I,A,B)              for(int I = (A); I < (B) ; ++ I)
#define REP(i,n)                for( int i=0 ; i < n ; i++ )
#define mp                      make_pair
#define pb                      push_back
#define all(x)                  (x).begin(),(x).end()
#define PI                      acos(-1.0)
#define EPS                     1e-9
#define F                       first
#define S                       second
#define lc                      ((n)<<1)
#define rc                      ((n)<<1|1)
#define db(x)                   cout << #x << " -> " << x << endl;
#define Di(x)                   int x;scanf("%d",&x)
#define in(x)                   input(x)
#define in2(x,y)                input(x), input(y)
#define in3(x,y,z)              input(x), input(y),input(z)
#define ins(x)                  scanf("%s",x)
#define ind(x)                  scanf("%lf",&x)
#define ms(ara_name,value)      memset(ara_name,value,sizeof(ara_name))
#define IO                      ios_base::sync_with_stdio(0);cin.tie(0)
#define READ                    freopen("/Users/matrixcode/Desktop/in.txt","r",stdin)
#define WRITE                   freopen("/Users/matrixcode/Desktop/out.txt","w",stdout)

template<class T > void input(T &x){
    char c = getchar();x = 0;
    for(;(c<48 || c>57);c = getchar());
    for(;c>47 && c<58;c = getchar()) {x = (x<<1) + (x<<3) + c - 48;}
}
inline long long bigmod(long long p,long long e,long long M){
    long long ret = 1;
    for(; e > 0; e >>= 1){
        if(e & 1) ret = (ret * p) % M;
        p = (p * p) % M;
    } return ret;
}
template <class T> inline T gcd(T a,T b){if(b==0)return a;return gcd(b,a%b);}
template <class T> inline T modinverse(T a,T M){return bigmod(a,M-2,M);}

/***************************** END OF TEMPLATE *******************************/

const int M = 105;
int E[M], S[M];
int D[M][M];
int N;
int Q;
struct Node{
    int u;
    double d;
    int r,s;
    bool operator<(const Node& rhs) const {
        if(d == rhs.d) {
            if(s== rhs.s ) {
                if(r== rhs.r) return u<rhs.u;
                return r > rhs.r;
            }
            return s > rhs.s;
        }return d < rhs.d;
    }
};
bool vis[M];
double dij(int s,int t)
{
    set<Node> pq;
    memset(vis,0,sizeof vis);
    pq.insert({s,0.0,E[s],S[s]});
    while(!pq.empty()) {
        Node u = *pq.begin(); pq.erase(u);
    
        if(u.u==t) return u.d;
        for(int i= 1; i <= N; i++ ) {
            if(D[u.u][i] == -1) continue;
            double dp = D[u.u][i] *1. / u.s;
            if(u.r >= D[u.u][i]) pq.insert({i,u.d + dp, u.r - D[u.u][i] , u.s});
            if(E[u.u] >= D[u.u][i] && vis[u.u] == 0)pq.insert({i,u.d + D[u.u][i]*1./ S[u.u] , E[u.u] - D[u.u][i] , S[u.u]});
        }
        vis[u.u] = 1;
        
    }
    return -1;
}
int main()
{
    READ;
    WRITE;
    int t,cs=0,u,v;
    cin>>t;
    while(t--){
        cin>>N>>Q;
        for(int i=1;i<=N;i++) cin>>E[i] >> S[i];
        for(int i=1;i<=N;i++){
            for(int j=1;j<=N;j++) cin>>D[i][j];
        }
        
        printf("Case #%d:",++cs);
        for(int i=1;i<=Q;i++) {
            cin>>u>>v;
            printf(" %.9lf", dij(u,v));
        }
        printf("\n");
    }
    return 0;
}
