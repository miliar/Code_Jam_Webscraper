///////////////////////////////
// Template By: Agus Sentosa //
//      15 - 02 - 2017       //
///////////////////////////////
//           Note            //
// * Don't use std::remove   //
// * Special flag: DEBUG     //
///////////////////////////////
 
#include <bits/stdc++.h>
using namespace std;
 
//Data Type
typedef long long LL;
typedef unsigned long long ULL;
typedef pair<int,int> pii;
typedef pair<LL,LL> pll;
typedef pair<double,double> pdd;
typedef vector<int> VI;
typedef vector<VI> VII;
typedef vector<string> VS;
typedef vector<VS> VSS;
typedef vector<LL> VL;
typedef vector<VL> VLL;
typedef vector<double> VD;
typedef vector<VD> VDD;
typedef vector<char> VC;
typedef vector<VC> VCC;
 
//Data Type Properties
#define f first
#define s second
#define mp make_pair
#define pb push_back
#define pf push_front
#define popb pop_back
#define popf pop_front
#define ins insert
#define remove erase
#define p push
 
//Macro
#define all(v) (v).begin(),(v).end()
#define sortv(v) sort(all(v))
#define reversev(v) reverse(all(v))
#define POPCOUNT __builtin_popcount
#define POPCOUNTLL __builtin_popcountll
#define CTZ __builtin_ctz
#define CTZLL __builtin_ctzll
#define THIS (*this)
#define SZ(v) ((int)(v).size())
 
//Output optimization for iostream
#define endl '\n'
 
//Debugging
#ifdef DEBUG
    #define DO_IF_DEBUG_FLAG_IS_ON 1
    #undef DEBUG
    #undef endl
#else
    #define DO_IF_DEBUG_FLAG_IS_ON 0
#endif
#define DEBUG if(DO_IF_DEBUG_FLAG_IS_ON)
#define NDEBUG if(!DO_IF_DEBUG_FLAG_IS_ON)
#define valueOf(x) cout << "Value of \"" << #x << "\" is \"" << x << "\"" << endl << flush;
 
//Some common inline function
template<class T, class U, class V> inline bool inRange(T a, U b, V c){   return b <= a && a <= c; }
template<class T> inline T sqr(T a){ return a * a; }
template<class T> inline void MAX(T &a, T b){ a = max(a,b); }
template<class T> inline void MIN(T &a, T b){ a = min(a,b); }
 
//pair<T,V> function (somehow very helpfull)
template<class T, class V>
pair<T,V> operator+(pair<T,V> a, pair<T,V> b){
    return {a.f + b.f, a.s + b.s};
}
 
template<class T, class V>
pair<T,V> operator-(pair<T,V> a, pair<T,V> b){
    return {a.f - b.f, a.s - b.s};
}
 
//Some I/O options
 
//Only for NON-NEGATIVE INTEGER!
#ifdef _WIN32
#define getchar_unlocked getchar
#endif
#define GETCHAR getchar_unlocked
template<class T = int>
inline bool io(T &res){
    static char c=' ';
    if(c == -1)return 0;
    while(!inRange(c, '0', '9'))c = GETCHAR();
    if(c == -1)return 0;
    res = c - '0';
    while((c=GETCHAR()), inRange(c, '0', '9')){ res = (res << 3) + (res << 1) +  c - '0'; }
    return 1;
}
 
inline string getString(){
    char buff[1000006];
    scanf("%s", buff);
    return buff;
}
 
inline void open(string a){
    freopen((a+".in").c_str(),"r",stdin);
    freopen((a+".out").c_str(),"w",stdout);
}
 
inline void close(){
    fclose(stdin);
    fclose(stdout);
}
 
//Constant
const int MAGIC_MEMSET_CONST = 63;
const int INF = 1061109567;
const LL LINF = 4557430888798830399LL;
const double DINF = numeric_limits<double>::infinity();
const int INV = -1044266559;
const LL LINV = -4485090715960753727LL;
const double DINV = -DINF;
const int MOD = (int)1e9 + 7;
const int dx[] = {1,0,-1,0,1,1,-1,-1};
const int dy[] = {0,1,0,-1,1,-1,1,-1};
///////////////////////////////
//      End of Template      //
///////////////////////////////

int main(){
    NDEBUG {ios_base::sync_with_stdio(false); std::cin.tie(0);}
    
    int t; cin >> t;
    while(t--) {
    	static int tc = 1;
    	cout << "Case #" << tc++ << ": ";

    	string str;
    	cin >> str;

    	int mx = 0;
    	int l = 0;
    	for(char i : str) {
    		MAX(mx, (int)i);
    		if(mx == '1' && i == '0') l ++;
    	}

    	if(l) {
    		for(int i = 0 ; i < SZ(str) - 1 ; i ++)
    			cout << '9';
    		cout << endl;
    	} else {
    		vector<char> res;

    		int s = 0;
    		for(char i : str) {
    			if(!SZ(res)) res.pb(i);
    			else {
    				if(res.back() <= i) res.pb(i);
    				else {
    					int x = res.back();
    					while(SZ(res) && res.back() == x) res.popb();
    					res.pb(x - 1);
    					for(; SZ(res) < SZ(str);) res.pb('9');
    						break;
    				}
    			}
    		}

    		for(char i : res) cout << i;
    		cout << endl;
    	}

    }

    return 0;
}