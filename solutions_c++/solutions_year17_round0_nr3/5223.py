#define _CRT_SECURE_NO_WARNINGS
#define _USE_MATH_DEFINES

#include "bits/stdc++.h"
#include <random>
using namespace std;
#define rep(i,n) for(int i=0;i<(n);++i)
#define rep2(i,a,b) for(int i=(a);i<(b);++i)
#define rrep(i,n) for(int i=(n)-1;i>=0;--i)
#define rrep2(i,a,b) for(int i=(a)-1;i>=b;--i)
#define range(i,a,b,c) for(int i=a;\
                    c>0?i<b:\
                    i>b;\
                    i+=c)
#define chmax(a, b) (a = (a) < (b) ? (b) : (a))
#define chmin(a, b) (a = (a) > (b) ? (b) : (a))
using ll = long long;
using ull = unsigned long long;
using ld = long double;
#define all(a) begin(a),end(a)
#define ifnot(a) if(not (a))
#define dump(x)  cerr << #x << " = " << (x) << endl
#define int long long
#ifdef _MSC_VER
const bool test = false;
#else 
const bool test = false;
#endif

int dx[] = { 1,0,-1,0 };
int dy[] = { 0,1,0,-1 };
const int INF = 1 << 28;
const ll INFL = (ll)1 << 58;
ll mod = (int)1e9 + 7;
const double eps = 1e-10;
typedef long double Real;
// return -1, 0, 1
int sgn(const Real& r) { return (r > eps) - (r < -eps); }
int sgn(const Real& a, const Real &b) { return sgn(a - b); }

//.....................
const int MAX = (int)2e5 + 5;

int H, W, T;

bool ng(int y, int x) {
	return y < 0 || H <= y || x < 0 || W <= x;
}

vector<string> split(const string &str, char sep) {
	vector<string> v;
	stringstream ss(str);
	string buffer;
	while (getline(ss, buffer, sep)) {
		v.push_back(buffer);
	}
	return v;
}

template<class InputIterator>
int sum(InputIterator begin, InputIterator end) {
	return accumulate(begin, end, 0ll);
}

string reverse_str(string s) {
	reverse(all(s));
	return s;
}

ifstream ifs("C-small-2-attempt0.in");
ofstream ofs("out.txt");

int n, k;

pair<int,int> ans1() {
	if (k == 1) {
		n--;
		int tmp = n / 2;
		return{ n-tmp, tmp };
	}
	priority_queue<int, vector<int>, less<int>> q;
	q.push(n);
	rep(i, k) {
		int cur = q.top(); q.pop();
		// dump(cur);
		cur--;
		int tmp = cur / 2;
		if (i == k - 1) return{ cur-tmp, tmp };
		q.push(tmp);
		q.push(cur - tmp);
	}
	return{ -1, -1 };
}

void solve() {
	ifs >> n >> k;
	dump(n);
	dump(k);
	auto res = ans1();
	cout << res.first << " " << res.second << endl;
	ofs << res.first << " " << res.second << endl;
}

signed main() {
	srand(time(NULL));
	int T = (int)1e15;
	ifs >> T;
	cout << fixed << setprecision(15);
	rep(i, T) {
		char s[MAX];
		int n = strlen(s);
		ofs << "Case #" << i + 1 << ": ";
		solve();
	}
	return 0;
}