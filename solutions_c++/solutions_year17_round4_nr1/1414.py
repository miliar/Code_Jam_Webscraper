#include<iostream>
#include<cstdio>
#include<string>
#include<cmath>
#include<bitset>
#include<vector>
#include<map>
#include<set>
#include<algorithm>
#include<utility>
using namespace std;

#define FOR(I,A,B) for(int I=(A);I<=(B);I++)
#define REP(I,N) for(int I=0;I<(N);I++)
#define ALL(X) (X).begin(),(X).end()
#define PB push_back
#define MP make_pair
#define f first
#define s second

typedef vector<int> VI;
typedef pair<int,int> PII;
typedef long long ll;
typedef vector<string> VS;

int memo[101][101][101][4];

int go(int a1, int a2, int a3, int r, int MOD) {
	if(a1 + a2 + a3 == 0) {
		return 0;
	}
	if(memo[a1][a2][a3][r] != -1) {
		return memo[a1][a2][a3][r];
	}
	
	int res = 0;
	if(a1 >= 1) res = max(res, go(a1 - 1, a2, a3, (MOD - 1 + r) % MOD, MOD));
	if(a2 >= 1) res = max(res, go(a1, a2 - 1, a3, (MOD - 2 + r) % MOD, MOD));
	if(a3 >= 1) res = max(res, go(a1, a2, a3 - 1, (MOD - 3 + r) % MOD, MOD));	
	
	res += (r == 0);
	memo[a1][a2][a3][r] = res;
	return res;
}

void testcase() {
	int n, p;
	cin >> n >> p;

	int g[4];
	REP(i, 4) g[i] = 0;
	
	REP(i, n) {
		int a;
		cin >> a;
		g[a % p]++;
	}

	FOR(a1, 0, 100) FOR(a2, 0, 100) FOR(a3, 0, 100) REP(r, 4) {
		memo[a1][a2][a3][r] = -1;
	}

	cout << go(g[1], g[2], g[3], 0, p) + g[0] << '\n';
}

int main() {
	int t;
	cin >> t;

	FOR(i, 1, t) {
		cout << "Case #" << i << ": ";
		testcase();
	}

	return 0;
}
