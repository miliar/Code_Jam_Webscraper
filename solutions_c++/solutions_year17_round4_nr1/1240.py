#include <bits/stdc++.h>
using namespace std;

#define pb push_back
#define ff first
#define ss second
#define POPCOUNT __builtin_popcountll
#define RIGHTMOST __builtin_ctzll
#define LEFTMOST(x) (63-__builtin_clzll((x)))
#define MP make_pair
#define FOR(i,x,y) for(vlong i = (x) ; i <= (y) ; ++i)
#define ROF(i,x,y) for(vlong i = (y) ; i >= (x) ; --i)
#define CLR(x,y) memset(x,y,sizeof(x))
#define UNIQUE(V) (V).erase(unique((V).begin(),(V).end()),(V).end())
#define NUMDIGIT(x,y) (((vlong)(log10((x))/log10((y))))+1)
#define SQ(x) ((x)*(x))
#define ABS(x) ((x)<0?-(x):(x))
#define FABS(x) ((x)+eps<0?-(x):(x))
#define ALL(x) (x).begin(),(x).end()
#define LCM(x,y) (((x)/gcd((x),(y)))*(y))
#define SZ(x) ((vlong)(x).size())
#define Set(N,cur) N=(N|(1<<cur))
#define Reset(N,cur) N=(N&(~(1<<cur)))
#define Check(N,cur) (!((N&(1<<cur))==0))
#define fast_cin ios_base::sync_with_stdio(false);cin.tie(NULL)
#define nl printf("\n")
#define phl printf ("hello world\n")
#define dbgA(A,i) debug("@At pos: ",i," = ",A[i])
#define dbg(x) debug("@Print: ",x)
#define spc(N) FOR(i,0,N-1) cout<<" "
#define printArray(A,st,ed) cout<<"@Array:";FOR(i,st,ed) cout<<" "<<A[i];cout<<endl
#define LINE printf("\n"); FOR(i,0,50) printf("=");printf("\n\n")

#ifdef forthright48
     #include <ctime>
     clock_t tStart = clock();
     #define debug(args...) {dbg,args; cerr<<endl;}
     #define timeStamp debug ("Execution Time: ", (double)(clock() - tStart)/CLOCKS_PER_SEC)
     #define bug printf("%d\n",__LINE__);

#else
     #define debug(args...)  // Just strip off all debug tokens
     #define timeStamp
#endif

struct debugger{
    template<typename T> debugger& operator , (const T& v){
        cerr<<v<<" ";
        return *this;
    }
}dbg;

#define LL long long
#define LLU long long unsigned int
typedef long long vlong;
typedef unsigned long long uvlong;
typedef pair < int, int > pii;
typedef pair < vlong, vlong > pll;

inline vlong gcd ( vlong a, vlong b ) {
    a = ABS ( a ); b = ABS ( b );
    while ( b ) { a = a % b; swap ( a, b ); } return a;
}

vlong ext_gcd ( vlong A, vlong B, vlong *X, vlong *Y ){
    vlong x2, y2, x1, y1, x, y, r2, r1, q, r;
    x2 = 1; y2 = 0; x1 = 0; y1 = 1;
    for (r2 = A, r1 = B; r1 != 0; r2 = r1, r1 = r, x2 = x1, y2 = y1, x1 = x, y1 = y ) {
        q = r2 / r1; r = r2 % r1;
        x = x2 - (q * x1); y = y2 - (q * y1);
    }
    *X = x2; *Y = y2;
    return r2;
}

inline vlong modInv ( vlong a, vlong m ) {
    vlong x, y;
    ext_gcd( a, m, &x, &y );
    x %= m;
    if ( x < 0 ) x += m;
    return x;
}

inline vlong power ( vlong a, vlong p ) {
    vlong res = 1, x = a;
    while ( p ) {
        if ( p & 1 ) res = ( res * x );
        x = ( x * x ); p >>= 1;
    }
    return res;
}

inline vlong bigmod ( vlong a, vlong p, vlong m ) {
    vlong res = 1 % m, x = a % m;
    while ( p ) {
        if ( p & 1 ) res = ( res * x ) % m;
        x = ( x * x ) % m; p >>= 1;
    }
    return res;
}

inline int STRLEN(char *s){
    int p = 0; while(s[p]) p++; return p;
}

//int knightDir[8][2] = { {-2,1},{-1,2},{1,2},{2,1},{2,-1},{-1,-2},{1,-2},{-2,-1} };
int dir4[4][2] = {{-1,0},{0,1},{1,0},{0,-1}};
//int dir8[8][2] = {{-1,0},{0,1},{1,0},{0,-1},{-1,-1},{1,1},{1,-1},{-1,1}};

const int inf = 214738360;
const LL mod = 1000000007;
const double pi = 2 * acos ( 0.0 );
const double eps = 1e-9;
const int Size = 100005;

///=========================  TEMPLATE ENDS HERE  ========================///
///=======================================================================///

int N,P;
int A[105];
int DP[101][101][101][101][4];
//int vis[101][101][101][101][4];

int call(int r0, int r1, int r2, int r3, int ex){
    if(DP[r0][r1][r2][r3][ex] != -1) return DP[r0][r1][r2][r3][ex];

    int res = 0, ret;
    if(r0>0){
        ret = call(r0-1, r1, r2, r3, (ex+0)%P) + (ex == 0);
        res = max(res, ret);
    }
    if(r1>0){
        ret = call(r0, r1-1, r2, r3, (ex+1)%P) + (ex == 0);
        res = max(res, ret);
    }
    if(r2>0){
        ret = call(r0, r1, r2-1, r3, (ex+2)%P) + (ex == 0);
        res = max(res, ret);
    }
    if(r3>0){
        ret = call(r0, r1, r2, r3-1, (ex+3)%P) + (ex == 0);
        res = max(res, ret);
    }

    return DP[r0][r1][r2][r3][ex] = res;
}

int C[5];

int main() {
    #ifdef forthright48
    freopen ( "A-large.in", "r", stdin );
    freopen ( "output_A_large.txt", "w", stdout );
    #endif // forthright48

    int nCase;
    scanf("%d",&nCase);
    for(int cs = 1;cs<=nCase;cs++){
        scanf("%d %d",&N,&P);
        CLR(DP, -1);
        CLR(C, 0);
        for(int i = 0;i<N;i++){
            int num;
            scanf("%d",&num);
            int r = num%P;
            C[r]++;
        }
        LL res = call(C[0], C[1], C[2], C[3], 0);
        printf("Case #%d: %lld\n",cs,res);
    }
    return 0;
}
