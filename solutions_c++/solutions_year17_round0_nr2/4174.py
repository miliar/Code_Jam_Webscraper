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

int str2int(string s) {
	stringstream ss(s);
	int x;
	ss >> x;
	return x;
}

string int2str(int a) {
	stringstream ss;
	ss << a;
	string str = ss.str();
	return str;
}

int N;
string s;

string solve(){
    int idx = 1,cnt = 1;
    while(idx<N){
        if(s[idx]<s[idx-1]) break;
        if(s[idx] == s[idx-1]){
            cnt++;
        }else{
            cnt = 1;
        }
        idx++;
    }
    if(idx == N) return s;
    string ns = "";
    if(s[idx-1] == '1' && idx - cnt == 0){
        for(int i = 0;i<N-1;i++) ns = ns + "9";
        return ns;
    }
    ns = s;
    ns[idx-cnt]--;
    for(int i = idx-cnt+1;i<N;i++) ns[i] = '9';
    return ns;
}

bool asc(string s){
    for(int i = 1;i<s.size();i++){
        if(s[i]<s[i-1]) return false;
    }
    return true;
}

string brt(string N){
    int L = str2int(N);
    for(int i = L;i>=1;i--){
        if(asc(int2str(i))){
            return int2str(i);
        }
    }
    return "-1";
}

int main() {
    #ifdef forthright48
    freopen ( "B-large.in", "r", stdin );
    freopen ( "outputBlarge.txt", "w", stdout );
    #endif // forthright48

    fast_cin;

    int nCase;
    cin >> nCase;
    for(int cs = 1;cs<=nCase;cs++){
        cin >> s;
        N = s.size();
        //string bres = brt(s);
        string res = solve();
        //if(res != bres){
        //    cout << "MisMatch For: " << s << endl;
        //    cout << "     Found: " << res << " Should Be: " << bres << endl;
        //}
        //cout << res << endl << endl;
        cout << "Case #" << cs << ": " << res << endl;
    }
    return 0;
}
