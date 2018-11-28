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
typedef pair<int, pii> P;

const ll INF = 1ll<<29;
const ll MOD = 1000000007;
const double EPS  = 1e-10;

int main() {
	int T;
	cin >> T;
	REP(Case, T) {
		ll N, K;
		scanf("%lld %lld", &N, &K);
		
		priority_queue<pll> pq;
		pq.push(pll(N, 1));
		
		pll ans;
		
		while (K) {
			ll l = pq.top().first;
			ll cnt = 0;
			
			while (!pq.empty() && pq.top().first == l) {
				cnt += pq.top().second;
				pq.pop();
			}
			
			if (K <= cnt) {
				if (l & 1) ans = pll(l / 2, l / 2);
				else ans = pll(l / 2, l / 2 - 1);
				
				K = 0;
			}
			else {
				K -= cnt;
				
				if (l & 1) pq.push(pll(l / 2, cnt * 2));
				else {
					pq.push(pll(l / 2 - 1, cnt));
					pq.push(pll(l / 2, cnt));
				}
			}
		}
		
		printf("Case #%d: %lld %lld\n", Case + 1, ans.first, ans.second);
	}
	return 0;
}