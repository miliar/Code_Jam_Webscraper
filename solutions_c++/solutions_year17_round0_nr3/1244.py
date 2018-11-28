#include <bits/stdc++.h>
using namespace std;
#define pb push_back
#define fi first
#define se second
#define mp make_pair
#define SZ(x) ((int)(x.size()))
#define FOI(i,a,n) for(int (i)=int(a);(i)<=int(n);++(i))
#define FOD(i,a,n) for(int (i)=int(a);(i)>=int(n);--(i))
#define IN(x,y) ((y).find((x))!=(y).end())
#define ALL(t) t.begin(),t.end()
#define MSET(tabl,i) memset(tabl, i, sizeof(tabl))
#define PSET(x,y) fixed<<setprecision(y)<<lf(x)
#define DBG(c) cout << #c << " = " << c << endl;
#define RTIME ((double)clock()/(double)CLOCKS_PER_SEC)

template<typename T,typename S>inline bool REMIN(T&a,const S&b){return a>b?a=b,1:0;}
template<typename T,typename S>inline bool REMAX(T&a,const S&b){return a<b?a=b,1:0;}

typedef long long ll;
typedef long double lf;
typedef pair<int, int> pi;
typedef vector<pi> vpi;
typedef vector<int> vi;
typedef vector<vi> vvi;

int toint(const string &s) { stringstream ss; ss << s; int x; ss >> x; return x; }
string tostring ( int number ){  stringstream ss; ss<< number; return ss.str();}
int bit(ll x, int pos){ return ((1ll<<pos)&x) ? 1 : 0; }

const int INF = 1e9;
const int NMAX = 1e5+5;
const ll MOD = 1000000007;
const lf PI = 2*acos(0);

ll power(ll base, ll exp, ll c = MOD) { if(!exp) return 1; ll r = power(base, exp/2, c); r=(r*r)%c; if(exp&1) r=(r*base)%c; return r; }

ll T,N,M;  
int a,b,c;
string s1, s2;

void nope(int dec = 0){
	if(!dec) cout<<"NO";
	exit(0);
}

int main(){
	ios_base::sync_with_stdio(false); cin.tie(0);
	
	cin >> T;
	FOI(test, 1, T) {

		cout << "Case #" << test << ": ";
		cin >> N >> M;
		
		map<ll, ll> cn;
		set<ll> vis;
		vis.insert(N + 1);
		cn[N + 1] = 1;

		while(1) {
			auto ptr = vis.end(); ptr --;
			ll curr = *ptr;
			vis.erase(ptr);
			ll co = cn[curr];
			M -= co;
			if(M <= 0) {
				curr -= 2;
				ll a2 = curr >> 1;
				ll a1 = curr - a2;
				cout << a1 << ' ' << a2 << '\n';
				break;
			}
			ll a2 = curr >> 1;
			ll a1 = curr - a2;
			cn[a2] += co;
			cn[a1] += co;
			vis.insert(a1); vis.insert(a2);
		}
	}	
	
	return 0;
}

