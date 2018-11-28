#include <bits/stdc++.h>

#define __INIT_CC__ ios::sync_with_stdio(false); \
	cin.tie(0);

#ifdef __WIN32__
	char getchar_unlocked() {return getchar();}
#endif

#define FOR(_i,_n,_m) for(int (_i)=(_n),_t=(_m);_i<(_t);++(_i))
#define FORN(_i,_n,_m) for(int (_i)=(_n),_t=(_m);_i<=(_t);++(_i))
#define FORD(_i,_n,_m) for(int (_i)=(_n),_t=(_m);_i>=(_t);--(_i))
#define FORLL(_i,_n,_m) for(long long (_i)=(_n),_t=(_m);_i<(_t);++(_i))
#define FORNLL(_i,_n,_m) for(long long (_i)=(_n),_t=(_m);(_i)<=(_t);++(_i))
#define FORDLL(_i,_n,_m) for(long long (_i)=(_n),_t=(_m);(_i)>=(_t);--(_i))
#define FOREACH(_i,_a) for (__typeof(_a.begin()) _i=_a.begin();_i!=_a.end();++_i)
#define RESET(_a,_value) memset(_a,_value,sizeof(_a))
#define pb push_back
#define ppb pop_back
#define pf push_front
#define ppf pop_front
#define ff first
#define ss second
#define mp make_pair
#define SIZE(_a) (int)_a.size()
#define VSORT(_a) sort(_a.begin(),_a.end())
#define SSORT(_a,_val) sort(_a,_a+(_val))
#define ALL(_a) _a.begin(),_a.end()
#define mt make_tuple
#define _get(_tuple,_i) get<_i>(_tuple)
#define eb emplace_back
 
using namespace std;
 
const int dr[] = { 1, 0,-1, 0, 1, 1,-1,-1};
const int dc[] = { 0, 1, 0,-1, 1,-1,-1, 1};
const double eps = 1e-9;
typedef vector<int> vi;
typedef pair<int,int> ii;
typedef vector<ii> vii;
typedef long long ll;
typedef unsigned long long ull;
typedef pair<ll,ll> pll;
typedef vector<pll> vpll;
typedef vector<ll> vll;
typedef pair<double,double> pdd;
typedef vector<pdd> vpdd;
const int INF = 0x7FFFFFFF;
const ll INFLL = 0x7FFFFFFFFFFFFFFFLL;
const double pi = acos(-1);

template <class T> T take(queue<T> &O) {T tmp=O.front();O.pop();return tmp;}
template <class T> T take(stack<T> &O) {T tmp=O.top();O.pop();return tmp;}
template <class T> T take(priority_queue<T> &O) {T tmp=O.top();O.pop();return tmp;}
template <class T> inline void getint(T &num)
{
	bool neg = 0;
	num = 0;
	char c;
	while ((c = getchar_unlocked()) && (!isdigit(c) && c != '-'));
	if (c == '-')
	{
		neg = 1;
		c = getchar_unlocked();
	}
	do num = num * 10 + c - '0';
	while ((c = getchar_unlocked()) && isdigit(c));
	if (neg) num = -num;
}

template <class T> inline bool inRange(T z, T a, T b){return a <= z && z <= b;}

void OPEN(string in = "input.txt",string out = "output.txt")
{
	freopen(in.c_str(), "r", stdin);
	freopen(out.c_str(), "w", stdout);
	return ;
}

//using sokokaleb's template v3.1

int n, p;
int cnt[5];

int dp3[105][105][3];

int f3(int a, int b, int sisa) {
	sisa %= 3;
	int& res = dp3[a][b][sisa];
	if (res != -1) return res;
	if (a == 0 && b == 0) return res = 0;
	res = 0;
	if (a > 0) {
		if (sisa == 0) {
			res = max(res, f3(a - 1, b, 2) + 1);
		} else {
			int lol = 1 - sisa;
			if (lol < 0) lol += 3;
			res = max(res, f3(a - 1, b, 3 - lol));
		}
	}

	if (b > 0) {
		if (sisa == 0) {
			res = max(res, f3(a, b - 1, 1) + 1);
		} else {
			int lol = 2 - sisa;
			if (lol < 0) lol += 3;
			res = max(res, f3(a, b - 1, 3 - lol));
		}
	}
	return res;
}

int dp4[105][105][105][4];

int f4(int a, int b, int c, int sisa) {
	sisa %= 4;
	int& res = dp4[a][b][c][sisa];
	if (res != -1) return res;
	if (a == 0 && b == 0 && c == 0) return res = 0;
	res = 0;
	if (a > 0) {
		if (sisa == 0) {
			res = max(res, f4(a - 1, b, c, 3) + 1);
		} else {
			int lol = 1 - sisa;
			if (lol < 0) lol += 4;
			res = max(res, f4(a - 1, b, c, 4 - lol));
		}
	}

	if (b > 0) {
		if (sisa == 0) {
			res = max(res, f4(a, b - 1, c, 2) + 1);
		} else {
			int lol = 2 - sisa;
			if (lol < 0) lol += 4;
			res = max(res, f4(a, b - 1, c, 4 - lol));
		}
	}

	if (c > 0) {
		if (sisa == 0) {
			res = max(res, f4(a, b, c - 1, 1) + 1);
		} else {
			int lol = 3 - sisa;
			if (lol < 0) lol += 4;
			res = max(res, f4(a, b, c - 1, 4 - lol));
		}
	}
	return res;
}

int main(int argc, char** argv) {
	__INIT_CC__
	cin >> n;
	FORN (tc, 1, n) {
		cin >> n >> p;
		RESET(cnt, 0);
		FOR (i, 0, n) {
			int a;
			cin >> a;
			++cnt[a % p];
		}

		int ans = 0;
		if (p == 2) {
			ans = cnt[0] + (cnt[1] + 1) / 2;
		} else if (p == 3) {
			RESET(dp3, -1);
			ans = cnt[0] + f3(cnt[1], cnt[2], 0);
		} else {
			RESET(dp4, -1);
			ans = cnt[0] + f4(cnt[1], cnt[2], cnt[3], 0);
		}
		cout << "Case #" << tc << ": " << ans << "\n";
	}
}
