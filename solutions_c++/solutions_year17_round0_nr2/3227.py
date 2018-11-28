//#pragma comment(linker,"/STACK:16777216") /*16Mb*/
#pragma comment(linker,"/STACK:33554432") /*32Mb*/
#define _CRT_SECURE_NO_DEPRECATE
#include<sstream>
#include<iostream>
#include<numeric>
#include<sstream>
#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<memory>
#include<memory.h>
#include<string>
#include<vector>
#include<cctype>
#include<list>
#include<queue>
#include<deque>
#include<stack>
#include<map>
#include<complex>
#include<set>
#include<algorithm>
#include <iomanip>

using namespace std;

typedef unsigned long long      ui64;
typedef long long               i64;
typedef long long               LL;
typedef vector<int>             VI;
typedef vector<bool>            VB;
typedef vector<VI>              VVI;
typedef vector<string>          VS;
typedef pair<int, int>           PII;
typedef map<string, int>         MSI;
typedef set<int>                SI;
typedef complex<double>         CD;
typedef vector< CD >            VCD;
typedef map<int, int>            MII;
typedef pair<double, double>     PDD;

#define PB                      push_back
#define MP                      make_pair
#define FOR(i, a, b)            for(int i = (a); i < (b); ++i)
#define RFOR(i, a, b)           for(int i = (a) - 1; i >= (b); --i)
#define CLEAR(a, b)             memset(a, b, sizeof(a))
#define SZ(a)                   int((a).size())
#define ALL(a)                  (a).begin(), (a).end()
#define RALL(a)                 (a).rbegin(), (a).rend()
#define INF                     (1000000000)
#define MOD                     (1000000007)

#ifdef _DEBUG
#define eprintf(...) fprintf (stderr, __VA_ARGS__)
#else
#define eprintf(...) assert (true)
#endif

const int SZ = 1000005;
int len;

string changeS(string n, string ans, int pos) {
	char ch = ans[pos];
	if (ch < '9') {
		ch++;
	}
	string s = ans;
	FOR(i, pos, len) {
		s[i] = ch;
	}
	if (s <= n) {
		return s;
	}
	return ans;
}

void solve(int t) {
	cout << "Case #" + std::to_string(t) + ": ";
	long long n;
	cin >> n;
	string ns = std::to_string(n);
	cout << n << " " << ns << endl;
	string ans = "";
	len = ns.length();
	FOR(i, 0, len) {
		ans += "1";
	}
	if (ns < ans) {
		ans = "";
		FOR(i, 0, len -1) {
			ans += "9";
		}
		cout << ans << endl;
		return;
	}

	FOR(i, 0, len) {
		FOR(j, 0, 10) {
			ans = changeS(ns, ans, i);
		}
	}
	cout << ans << endl;
}

int main() {
	freopen("B-large.in", "r", stdin);
	//freopen("B-large.out", "w", stdout);
	int t;
	cin >> t;
	FOR(i, 0, t) {
		solve(i + 1);
	}

	return 0;
}