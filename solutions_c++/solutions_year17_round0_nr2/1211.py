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
typedef unsigned long long ull;
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

int T,N,M;  
int a,b,c;
string s1, s2;

void nope(int dec = 0){
	if(!dec) cout<<"NO";
	exit(0);
}

string conv(string giv, int pos) {
	giv[pos]--;
	FOI(i, pos + 1, giv.length() - 1)
		giv[i] = '9';
	return giv;
}

string lookfor(string inp) {
	FOI(i, 1, inp.length() - 1) {
		if(inp[i] < inp[i - 1]) {
			return lookfor(conv(inp, i - 1));
		}
	}
	return inp;
}

int main(){
	ios_base::sync_with_stdio(false); cin.tie(0);
	
	cin >> T;

	FOI(test, 1, T) {
		string inp;
		cin >> inp;
		string res = lookfor(inp);
		int z = 0;
		while(res[z] == '0') z++;
		res = res.substr(z);
		cout << "Case #" << test << ": " << res << '\n';
	}
	
	return 0;
}

