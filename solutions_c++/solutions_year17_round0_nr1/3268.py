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

int d[1 << 12];
int n, k;
queue<int> Q;

//set<string> S;

void addMasks(int mask) {
	FOR(i, 0, n - k + 1) {
		int nmask = mask;
		FOR(j, 0, k) {
			nmask ^= (1 << (i + j));
		}
		if (d[nmask] == INF) {
			Q.push(nmask);
			d[nmask] = d[mask] + 1;
		}
	}
}

string bs(int mask) {
	string r = "";
	while (mask) {
		if (mask % 2 == 1) {
			r += "1";
		}
		else {
			r += "0";
		}
		mask /= 2;
	}

	return r;
}

int brut(string s, int k) {
	FOR(i, 0, 1 << 11) {
		d[i] = INF;
	}

	n = s.size();
	int mask = 0;
	FOR(i, 0, n) {
		if (s[i] == '+') {
			mask += (1 << i);
		}
	}
	//cout << bs(mask) << endl;

	while (!Q.empty()) {
		Q.pop();
	}

	d[mask] = 0;
	Q.push(mask);
	int kk = 0;
	while (!Q.empty()) {
		kk++;
		mask = Q.front();
		//cout << bs(mask) << endl;
		Q.pop();
		addMasks(mask);
		if (d[(1 << n) - 1] < INF) {
			//cout << kk << endl;
			return d[(1 << n) - 1];
		}
	}
	//cout << kk << endl;
	return d[(1 << n) - 1];
}

int main() {
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("A-small.out", "w", stdout);
	int t;
	cin >> t;
	FOR(i, 0, t) {
		string s;
		cout << "Case #" + std::to_string(i+1) + ": ";
		cin >> s >> k;
		int ans = brut(s, k);
		if (ans == INF) {
			cout << "IMPOSSIBLE" << endl;
		}
		else {
			cout << ans << endl;
		}
	}

	return 0;
}