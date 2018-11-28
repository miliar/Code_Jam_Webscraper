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

ll toint(const string &s) { stringstream ss; ss << s; ll x; ss >> x; return x; }
string tostring ( int number ){  stringstream ss; ss<< number; return ss.str();}
int bit(ll x, int pos){ return ((1ll<<pos)&x) ? 1 : 0; }

const int INF = 1e9;
const int NMAX = 1e5+5;
const ll MOD = 1000000007;
const lf PI = 2*acos(0);

ll power(ll base, ll exp, ll c = MOD) { if(!exp) return 1; ll r = power(base, exp/2, c); r=(r*r)%c; if(exp&1) r=(r*base)%c; return r; }

ll T;
int a,b,c;
string s1, s2;

void solve() {
	ll N, P;
	cin >> N >> P;
	int ref[53];
	FOI(i, 0, N - 1) cin >> ref[i];
	vvi mat(N, vi(P, 0));
	FOI(i, 0, N - 1) {
		FOI(j, 0, P - 1) {
			cin >> mat[i][j];
		}
		sort(ALL(mat[i]));
	}
	int flag = 0;
	int cn = 0;
	ll kitn = 1;
	FOI(kitn, 1, 1e6) {
		int fail = 0;
		int done = 0;
		vi usin(N);
		FOI(i, 0, N - 1) {
			int gotit = 0;
			while(SZ(mat[i]) && mat[i][0] * ll(10) < 9 * ll(kitn) * ref[i]) {
				mat[i].erase(mat[i].begin());
			}
			if(!SZ(mat[i])) {
				fail = 1;
				done = 1;
				break;
			}
			while(mat[i][0] * ll(10) <= 11 * ll(kitn) * 
				ref[i]) {
				int temp = mat[i][0];
				if(temp * ll(10) >= 9 * ll(kitn) * ref[i]) {
					gotit = 1;
					break;
				}
			}
			if(!gotit)
				fail = 1;
		}
		if(!fail) {
			FOI(i, 0, N - 1) mat[i].erase(mat[i].begin());
			kitn --;
			cn ++;
		}
		if(done)
			break;
	}
	cout << cn << '\n';
}

int main(){
	ios_base::sync_with_stdio(false); cin.tie(0);
	
	cin >> T;

	FOI(test, 1, T) {
		cout << "Case #" << test << ": "; solve(); //cout << '\n';
	}	
	
	return 0;
}

