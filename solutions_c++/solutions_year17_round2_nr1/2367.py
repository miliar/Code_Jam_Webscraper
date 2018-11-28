#include <iostream>
#include <cstdio>
#include <algorithm>
#include <string>
#include <vector>
#include <queue>
#include <map>
#include <set>
#include <functional>
#include <cmath>
#include <complex>
#include <cctype>
#include <cassert>
#include <sstream>
#include <ctime>

using namespace std;

#define FOR(i,a,b) for(int i=(a);i<(b);i++)
#define REP(i,n) FOR(i,0,n)
#define ALL(v) (v).begin(),(v).end()

template<typename A, typename B> inline bool chmax(A &a, B b) { if (a<b) { a=b; return 1; } return 0; }
template<typename A, typename B> inline bool chmin(A &a, B b) { if (a>b) { a=b; return 1; } return 0; }

typedef unsigned long long ull;
typedef long long ll;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;

const ll INF = 1ll<<29;
const ll MOD = 1000000007;
const double EPS  = 1e-10;


int main() {
	int T;
	cin >> T;
	
	REP(tc, T) {
		int D, N;
		scanf("%d %d", &D, &N);
		
		int K[1000], S[1000];
		
		REP(i, N) scanf("%d %d", K + i, S + i);
		
		double ma = 0;
		
		REP(i, N) {
			if (K[i] >= D) continue;
			
			double t = (double)(D - K[i]) / S[i];
			chmax(ma, t);
		}
		
		double ans = D / ma;
		
		printf("Case #%d: ", tc + 1);
		printf("%.15lf\n", ans);
	}
	return 0;
}
