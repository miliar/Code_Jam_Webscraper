/*
Author :: MD. Musfiqur Rahman Sanim
Aust cse 28th Batch
ID:11.02.04.097
*/


//{ Template
using namespace std;
//{ headers
#include<bits/stdc++.h>
//}
//{ Loops
#define forab(i,a,b) for (__typeof(b) i = (a); i <= (b); ++i)
#define rep(i,n) forab (i, 0, (n) - 1)
#define For(i,n) forab (i, 1, n)
#define rofba(i,a,b) for (__typeof(b) i = (b); i >= (a); --i)
#define per(i,n) rofba (i, 0, (n) - 1)
#define rof(i,n) rofba (i, 1, n)
#define forstl(i,s) for (__typeof ((s).end ()) i = (s).begin (); i != (s).end (); ++i)
//}
//{ Floating-points
#define EPS 1e-7
#define abs(x) (((x) < 0) ? - (x) : (x))
#define zero(x) (abs (x) < EPS)
#define equal(a,b) (zero ((a) - (b)))
#define PI 2*acos (0.0)
//}
typedef long long int64;
typedef unsigned long long int64u;
#define memo(a,v) memset(a,v,sizeof(a))
#define all(a) a.begin(),a.end()
#define db double
#define pb push_back
#define pii pair<int ,int >
#define NL puts("")
#define ff first
#define ss second
//{
//Intput_Output
#define gc getchar
template<class T>inline bool read(T &x){int c=gc();int sgn=1;while(~c&&c<'0'|c>'9'){if(c=='-')sgn=-1;c=gc();}for(x=0;~c&&'0'<=c&&c<='9';c=gc())x=x*10+c-'0';x*=sgn;return ~c;}
#define II ({ int a; read(a); a;})
#define IL ({ int64 a; read(a);  a;})
#define ID ({ db a; scanf("%lf",&a);  a;})
#define IC ({ char a; scanf("%c",&a);  a;})
#define IS ({ string a; cin >> a;  a;})
#define OC printf("Case #%d:",cs);
//}
//}
#define __(args...) {dbg,args; cerr<<endl;}
struct debugger{template<typename T> debugger& operator , (const T& v){cerr<<v<<"    "; return *this; }}dbg;
template <class T, class U> inline T max (T &a, U &b)
{
    return a > b ? a : b;
}
template <class T, class U> inline T min (T &a, U &b)
{
    return a < b ? a : b;
}
template <class T, class U> inline T swap (T &a, U &b)
{
    T tmp = a;
    a = b;
    b = tmp;
}
//int dx[]={1,0,-1,0};int dy[]={0,1,0,-1}; //4 Direction
//int dx[]={1,1,0,-1,-1,-1,0,1};int dy[]={0,1,1,1,0,-1,-1,-1};//8 Direction
//int dx[]={2,1,-1,-2,-2,-1,1,2};int dy[]={1,2,2,1,-1,-2,-2,-1};//Knight Direction
//int dx[6]={2,1,-1,-2,-1,1};int dy[6]={0,1,1,0,-1,-1}; //Hexagonal Direction


const int mx = 1e5 + 7;
const int mod = 1000000007 ;
const db pi = PI;
int EQ(double d) {
    if ( fabs(d) < EPS ) return 0;
    return d > EPS ? 1 : -1 ;
}

int64 val[55];
int64 arr[55][55];

const int MX = 1e5 + 7  ;
const int INF = 1e8 + 7;

const int  MAXE = 100007 ;

int src, snk, nNode, nEdge;
int Q[MX], fin[MX], pro[MX], dist[MX];
int flow[MAXE], cap[MAXE], Next[MAXE], to[MAXE];

inline void init(int _n) {
    nNode = _n, nEdge = 0;
    memo(fin,-1);
}
// bidirectional edge **
inline void add(int u, int v, int c) {
    to[nEdge] = v, cap[nEdge] = c, flow[nEdge] = 0, Next[nEdge] = fin[u], fin[u] = nEdge++;
    to[nEdge] = u, cap[nEdge] = c, flow[nEdge] = 0, Next[nEdge] = fin[v], fin[v] = nEdge++;
}

bool bfs() {
    int st, en, i, u, v;
    memo(dist,-1);
    dist[src] = st = en = 0;
    Q[en++] = src;
    while(st < en) {
        u = Q[st++];
        for(i=fin[u]; i>=0; i=Next[i]) {
            v = to[i];
            if(flow[i] < cap[i] && dist[v]==-1) {
                dist[v] = dist[u]+1;
                Q[en++] = v;
            }
        }
    }
    return dist[snk]!=-1;
}

int dfs(int u, int fl) {
    if(u==snk) return fl;
    for(int &e=pro[u], v, df; e>=0; e=Next[e]) {
        v = to[e];
        if(flow[e] < cap[e] && dist[v]==dist[u]+1) {
            df = dfs(v, min(cap[e]-flow[e], fl));
            if(df>0) {
                flow[e] += df;
                flow[e^1] -= df;
                return df;
            }
        }
    }
    return 0;
}

int dinitz() {
    int ret = 0;
    int df;
    while(bfs()) {
        for(int i=0; i<=nNode; i++) pro[i] = fin[i]; // use temporary source node 0 and main graph 1 to n
        while(true) {
            df = dfs(src, INF);
            if(df) ret += df;
            else break;
        }
    }
    return ret;
}

pii call(int x,int v){
    int tt = x / v;

    int a = -1, b = -1;

    forab(i,(int)max(0,tt-1000),(int)min(1000000, tt+1000)){
        double Min = i*v*.9;
        double Max = i*v*1.1;
        if(x >= Min && x <= Max){
            if(a  == -1) a = b = i;
            else b = i;
        }
    }
    return pii(a,b);
}

bool inside(pii a, pii b) {
    if(a.ff >= b.ff && a.ff <= b.ss) return true;
    if(a.ss >= b.ff && a.ss <= b.ss) return true;
    if(b.ff >= a.ff && b.ff <= a.ss) return true;
    if(b.ss >= a.ff && b.ss <= a.ss) return true;
    return false;
}

bool isMatch(int a, int b, int k){
    int x = arr[a-1][k];
    int y = arr[a][b];
    pii t1 = call(x, val[a-1]);
    pii t2 = call(y, val[a]);
    if(t1.ff == -1 || t2.ff == -1) return false;


    return inside(t1,t2);
}

int main() {
#ifdef Sanim
    freopen ("in.txt", "r", stdin);
     freopen ("output.txt", "w", stdout);
#endif
    int t = II;
    For(cs,t) {
        int n = II, p = II;
        init(n*p+1);
        rep(i,n) {
            val[i] = II;
        }
        src = 0;
        snk = n*p + 1;
        rep(i,n){
            rep(j,p) {
                arr[i][j] = II;
                if(i) {
                    rep(k,p) {
                        if(isMatch(i,j,k)){
                            int u = (i-1)*p + k + 1;
                            int v = i*p + j + 1;
                            add(u,v,1);
                        }
                    }
                } else {
                    if(call(arr[i][j], val[i]).ff != -1) add(0, j+1, 1);
                }

                if(i == n-1){
                    if(call(arr[i][j], val[i]).ff != -1) add((i*p) + j+1, snk, 1);
                }
            }
        }
        OC;
        printf(" %d\n",dinitz());

    }
}
