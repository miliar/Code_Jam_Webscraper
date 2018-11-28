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
int bit(ll x, int pos){ return (x >> pos) & 1; }
ll power(ll base, ll exp, ll c = 1e9 + 7) { if(!exp) return 1; ll r = power(base, exp/2, c); r=(r*r)%c; if(exp&1) r=(r*base)%c; return r; }

const ll INF = 1e9;
const int NMAX = 1e5+5;
const ll MOD = 1000000007;
const lf PI = 2*acos(0);

ll T,N,M;  
int a,b,c;
string s1, s2;

short rec4[103][103][103][4];
short rec3[103][103][5];

int dper4(int c1, int c2, int c3, int curr) {
	if(c1 + c2 + c3 == 0) return 0;
	if(rec4[c1][c2][c3][curr] != -1)
		return rec4[c1][c2][c3][curr];
	short & ret = rec4[c1][c2][c3][curr];
	int temp = 0;
	if(curr == 0) temp = 1;

	if(c1)
		REMAX(ret, temp + dper4(c1 - 1, c2, c3, (curr - 1 + 4) % 4));
	if(c2)
		REMAX(ret, temp + dper4(c1, c2 - 1, c3, (curr - 2 + 4) % 4));
	if(c3)
		REMAX(ret, temp + dper4(c1, c2, c3 - 1, (curr - 3 + 4) % 4));

	return ret;
}

int dper3(int c1, int c2, int curr) {
	if(c1 + c2 == 0) return 0;
	if(rec3[c1][c2][curr] != -1)
		return rec3[c1][c2][curr];
	short & ret = rec3[c1][c2][curr];
	int temp = 0;
	if(curr == 0) temp = 1;

	if(c1)
		REMAX(ret, temp + dper3(c1 - 1, c2, (curr - 1 + 3) % 3));
	if(c2)
		REMAX(ret, temp + dper3(c1, c2 - 1, (curr - 2 + 3) % 3));
	
	return ret;	
}

void solve() {
	cin >> N >> M;
	int cn[5];
	MSET(cn, 0);
	FOI(i, 1, N) {
		cin >> a;
		cn[a % M] ++;
	}
	if(M == 2) {
		int ans = cn[0];
		ans += (cn[1] + 1) / 2;
		cout << ans << '\n';
	} else if(M == 3) {
		int ans = cn[0];
		MSET(rec3, -1);
		ans += dper3(cn[1], cn[2], 0);
		cout << ans << '\n';
	} else {
		int ans = cn[0];
		MSET(rec4, -1);
		ans += dper4(cn[1], cn[2], cn[3], 0);
		cout << ans << '\n';
	}
}

int main(){
	ios_base::sync_with_stdio(false); cin.tie(0);
	
	cin >> T;

	FOI(test, 1, T) {
		cout << "Case #" << test << ": "; solve(); //cout << '\n';
	}	
	
	return 0;
}

