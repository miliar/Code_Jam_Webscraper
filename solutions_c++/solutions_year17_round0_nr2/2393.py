#include <cstdio>
#include <iostream>
#include <vector>
#include <map>
#include <unordered_map>
#include <set>
#include <unordered_set>
#include <string>
#include <cstring>
#include <sstream>
#include <algorithm>
#include <functional>
#include <queue>
#include <stack>
#include <cmath>
#include <iomanip>
#include <list>
#include <tuple>
#include <bitset>
#include <ciso646>
#include <cassert>

using namespace std;

#define int long long
#define double long double

typedef pair<int, int> P;
typedef tuple<int, int, int> T;

template<class T> string tostr(T x) { stringstream o; o << x; return o.str(); }
template<class T> T sqr(T x) { return x*x; }
template<class T> T mypow(T x, int n) { T r = 1; while (n > 0) { if (n & 1)r = r*x; x = x*x; n >>= 1; }return r; }

int toint(string s) { int v; stringstream i(s); i >> v; return v; }
bool check(int x, int y, int w, int h) { return x >= 0 && y >= 0 && w > x && h > y; }
int gcd(int a, int b) { return b ? gcd(b, a%b) : a; }
int lcm(int a, int b) { return a / gcd(a, b) * b; }

#define REP(i,a,b)	for(int (i) = (a);i < (b);(i)++)
#define rep(i,n)	REP(i,0,n)
#define PER(i,a,b)	for(int (i) = (a-1);i >= (b);(i)--)
#define per(i,n)	PER(i,n,0)
#define each(i,n)	for(auto &i : n)
#define clr(a)		memset((a), 0 ,sizeof(a))
#define mclr(a)		memset((a), -1 ,sizeof(a))
#define all(a)		(a).begin(),(a).end()
#define dump(val) 	cerr << #val " = " << val << endl;
#define dum(val)	cerr << #val " = " << val;
#define FILL(a,v)	fill(a,a+sizeof(a)/sizeof(*a),v)

const int dx[8] = { +1,+0,-1,+0,+1,+1,-1,-1 };
const int dy[8] = { +0,-1,+0,+1,-1,+1,-1,+1 };
const int mod = 1e9 + 7;
const int INF = 1e17 + 9;

bool ok(string s) {
	rep(i, s.size() - 1) {
		if (s[i] > s[i + 1]) {
			return false;
		}
	}
	return true;
}

string fix(string s) {
	rep(i, s.size()) {
		if (s[i] != '0') {
			return s.substr(i);
		}
	}
	return "0";
}

signed main() {
	cin.tie(0);
	ios_base::sync_with_stdio(false);

	int T;
	cin >> T;

	rep(_, T) {
		cout << "Case #" << _ + 1 << ": ";
		string s;
		cin >> s;

		if (ok(s)) {
			cout << s << endl;
			continue;
		}

		int ans = 0;
		int n = s.size();
		REP(i, 1, n) {
			string t = s;
			int j = i - 1;
			t[j]--;
			REP(k, i, n) t[k] = '9';
			if (ok(t)) {
				ans = max(ans, toint(fix(t)));
			}
		}
		cout << ans << endl;
	}

	return 0;
}