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

int N;
int R,O,Y,G,B,V;
char ans[1005];
string RGR,BOB,YVY;

int RR,BB,YY;
int total = 0;
bool found = false;
/// R = 0, B = 1, Y = 2;

vector< vector< vector< vector< vector<int> > > > > DP;
map<vector<int>,int> MAP;

void init(){
    DP.resize(RR+1);
    for(int i = 0;i<=RR;i++){
        DP[i].resize(BB+1);
        for(int j = 0;j<=BB;j++){
            DP[i][j].resize(YY+1);
            for(int m = 0;m<=YY;m++){
                DP[i][j][m].resize(4);
                for(int n = 0;n<=3;n++){
                    DP[i][j][m][n].resize(4);
                    for(int p = 0;p<=3;p++){
                        DP[i][j][m][n][p] = -1;
                    }
                }
            }
        }
    }
}

int cc = 0;

void call(int rr, int bb, int yy, int st, int ed, int idx){
    //debug("DDD: ",rr,bb,yy);
    if(rr+bb+yy == 0){
        if(st != ed){
            found = true;
        }
        return;
    }

    if(rr>bb+yy+2) return;
    if(bb>rr+yy+2) return;
    if(yy>rr+bb+2) return;

    //if(DP[rr][bb][yy][st][ed] != -1) return;
    vector<int> state;
    state.pb(rr);
    state.pb(bb);
    state.pb(yy);
    state.pb(st);
    state.pb(ed);

    if(MAP[state] == 1) return;

    if(rr>0){
        if(ed != 0){
            ans[idx] = 'R';
            call(rr-1, bb, yy, st, 0, idx+1);
        }
    }
    if(found == true) return;

    if(bb>0){
        if(ed != 1){
            ans[idx] = 'B';
            call(rr, bb-1, yy, st, 1, idx+1);
        }
    }
    if(found == true) return;

    if(yy>0){
        if(ed != 2){
            ans[idx] = 'Y';
            call(rr, bb, yy-1, st, 2, idx+1);
        }
    }

    //DP[rr][bb][yy][st][ed] = 1;
    MAP[state] = 1;
}

bool solve(){
    found = false;
    RGR = "",BOB = "",YVY = "";

    //debug("Here 1");
    if(N == 1){
        if(R == 1) ans[0] = 'R';
        else if(B == 1) ans[0] = 'B';
        else if(G == 1) ans[0] = 'G';
        else if(Y == 1) ans[0] = 'Y';
        else if(O == 1) ans[0] = 'O';
        else if(V == 1) ans[0] = 'V';
        return true;
    }

    //debug("Here 12");
    if(R+G == N){
        //debug("RGG");
        if(abs(R-G)>1) return false;
        int idx = 0;
        if(R>G){
            ans[idx++] = 'R';
            R--;
            while(R>0){
                ans[idx++] = 'G';
                ans[idx++] = 'R';
                R--;G--;
            }
        }else if(G>R){
            ans[idx++] = 'G';
            G--;
            while(R>0){
                ans[idx++] = 'R';
                ans[idx++] = 'G';
                R--;G--;
            }
        }else{
            while(R>0){
                ans[idx++] = 'R';
                ans[idx++] = 'G';
                R--;G--;
            }
        }
        return true;
    }
    if(G>=R && G>0) return false;

    //debug("Here 22");

    if(B+O == N){
        if(abs(B-O)>1) return false;
        int idx = 0;
        if(B>O){
            ans[idx++] = 'B';
            B--;
            while(B>0){
                ans[idx++] = 'O';
                ans[idx++] = 'B';
                B--;O--;
            }
        }else if(O>B){
            ans[idx++] = 'O';
            O--;
            while(B>0){
                ans[idx++] = 'B';
                ans[idx++] = 'O';
                B--;O--;
            }
        }else{
            while(B>0){
                ans[idx++] = 'B';
                ans[idx++] = 'O';
                B--;O--;
            }
        }
        return true;
    }
    if(O>=B && O>0) return false;

    //debug("Here 3");

    if(Y+V == N){
        if(abs(Y-V)>1) return false;
        int idx = 0;
        if(Y>V){
            ans[idx++] = 'Y';
            Y--;
            while(Y>0){
                ans[idx++] = 'V';
                ans[idx++] = 'Y';
                Y--;V--;
            }
        }else if(V>Y){
            ans[idx++] = 'V';
            V--;
            while(Y>0){
                ans[idx++] = 'Y';
                ans[idx++] = 'V';
                Y--;V--;
            }
        }else{
            while(Y>0){
                ans[idx++] = 'Y';
                ans[idx++] = 'V';
                Y--;V--;
            }
            //debug("HMM ",idx);
        }
        return true;
    }
    if(V>=Y && V>0) return false;

    /// Base case finish.

    if(G>0){
        RGR = "R";
        R--;
    }
    while(G > 0){
        RGR = RGR + "GR";
        G--; R--;
    }
    if(O>0){
        BOB = "B";
        B--;
    }
    while(O > 0){
        BOB = BOB + "OB";
        O--; B--;
    }
    if(V>0){
        YVY = "Y";
        Y--;
    }
    while(V > 0){
        YVY = YVY + "VY";
        V--; Y--;
    }
    if(R<0 || B<0 || Y<0) return false;

    RR = R, BB = B, YY = Y;
    if(RGR.size()>0) RR++;
    if(BOB.size()>0) BB++;
    if(YVY.size()>0) YY++;
    total = RR+BB+YY;
    N = total;

    //debug(RR,BB,YY);

    found = false;

    //init();
    MAP.clear();
    ans[0] = 'R';
    if(RR>0) call(RR-1, BB, YY, 0, 0, 1);
    if(found == true) return true;

    //debug("123");

    //init();
    MAP.clear();
    ans[0] = 'B';
    if(BB>0) call(RR, BB-1, YY, 1, 1, 1);
    if(found == true) return true;

    //debug("12345");
    //init();
    MAP.clear();
    ans[0] = 'Y';
    if(YY>0) call(RR, BB, YY-1, 2, 2, 1);
    if(found == true) return true;

    //debug("123678");
    return false;
}

void printPart(){
    //debug(RGR, BOB, YVY);
    for(int i = 0;i<N;i++){
        if(ans[i] == 'R'){
            if(RGR.size()>0){
                printf("RGR");
                RGR = "";
            }else{
                printf("R");
            }
        }else if(ans[i] == 'B'){
            if(BOB.size()>0){
                printf("BOB");
                BOB = "";
            }else{
                printf("B");
            }
        }else if(ans[i] == 'Y'){
            if(YVY.size()>0){
                printf("YVY");
                YVY = "";
            }else{
                printf("Y");
            }
        }else{
            printf("%c",ans[i]);
        }
    }
    printf("\n");
}

int main() {
    #ifdef forthright48
    freopen ( "B-small-attempt1.in", "r", stdin );
    //freopen ( "input.txt", "r", stdin );
    freopen ( "B_output_small.txt", "w", stdout );
    #endif // forthright48

    int nCase;
    scanf("%d",&nCase);
    for(int cs = 1;cs<=nCase;cs++){
        scanf("%d %d %d %d %d %d %d",&N, &R,&O,&Y,&G,&B,&V);
        bool res = solve();
        if(res == true){
            printf("Case #%d: ",cs);
            printPart();
        }else{
            printf("Case #%d: IMPOSSIBLE\n",cs);
        }
    }
    return 0;
}
