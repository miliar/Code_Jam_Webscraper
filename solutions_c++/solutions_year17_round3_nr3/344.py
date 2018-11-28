// VSCF.cpp : Defines the entry point for the console application.
//
#include <bits/stdc++.h>
#include "gurobi_c++.h"
using namespace std;
#define int long long
#define M_PI 3.14159265358979323846
typedef long long LL;
typedef pair<int, int> PII;
#define MP make_pair
#define FOR(v,p,k) for(int v=p;v<=k;++v)
#define FORD(v,p,k) for(int v=p;v>=k;--v)
#define REP(i,n) for(int i=0;i<(n);++i)
#define VAR(v,i)  decltype(i) v=(i)
#define FOREACH(i,c) for(VAR(i,(c).begin());i!=(c).end();++i)
#define PB push_back
#define ST first
#define ND second
#define SZ(x) (int)x.size()
#define SIZE(x) SZ(x)
#define ALL(c) c.begin(),c.end()
#define MAXN 1000010
typedef long double LD;
typedef vector<int> VI;

int32_t main() {
	ios_base::sync_with_stdio(0);
	cout << setprecision(9) << fixed;
	int t;
	cin >> t;
	REP(_, t) {
		int n, k;
		cin >> n >> k;
		LD u;
		cin >> u;
		vector<LD> inp(n);
		for (LD & i : inp) {
			cin >> i;
		}
		sort(ALL(inp));
		LD sum = 0;
		int broke = inp.size();
		REP(i, n) {
			sum += inp[i];
			if (inp[i] * (i + 1) - sum > u) {
				sum -= inp[i];
				broke = i;
				break;
			}
		}
		int count = broke;
		u -= inp[broke - 1] * count - sum;
		LD result = powl(inp[broke - 1] + u / count, count);
		FOR(i, broke, inp.size() - 1) {
			result *= inp[i];
		}
		cout << setprecision(9) << fixed;
		cout << "Case #" << _ + 1 << ": " << result<<"\n";
	}
	return 0;
}
