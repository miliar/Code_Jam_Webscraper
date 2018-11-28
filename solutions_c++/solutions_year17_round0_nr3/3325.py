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

map<LL, LL> M;

pair<LL, LL> f(LL n, LL k) {
	M.clear();
	vector<LL> v;
	v.push_back(n);
	M[n] = 1;
	int l = 0;
	LL last = n;
	while (k>0) {
		int r = v.size();
		sort(ALL(v));
		reverse(ALL(v));
		FOR(i,0,2)
			if (k>0 && l < r) {
				n = v[l];
				//cout << n << " " << M[n] << " " << k << endl;
				k -= M[n];
				last = n;
				l++;
				n--;
				if (M[n / 2] == 0) {
					v.push_back(n / 2);
				}
				M[n / 2] += M[n+1];
				if (M[n-n / 2] == 0) {
					v.push_back(n - n / 2);
				}
				M[n - n / 2] += M[n+1];
			}
	}
	FOR(i, 0, v.size()) {
		//cout << v[i] << " " << M[v[i]] << endl;
	}
	last--;
	return MP(max(last/2, last-last/2), min(last / 2, last - last / 2));
}

void fast(int t) {
	cout << "Case #" + std::to_string(t) + ": ";
	LL n, k;
	cin >> n >> k;
	auto r = f(n, k);
	cout << r.first << " " << r.second << endl;
}

int main() {
	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);
	int t;
	cin >> t;
	FOR(i, 0, t) {
		fast(i + 1);
	}

	return 0;
}