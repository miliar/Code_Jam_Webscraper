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
		string S;
		cin >> S;
		
		while (true) {
			bool ok = true;
			
			for (int i = S.size() - 1; i > 0; i--) {
				if (S[i - 1] <= S[i]) continue;
				
				if (i - 1 == 0 && S[i - 1] == '1') {
					S.erase(S.begin());
					REP(i, S.size()) S[i] = '9';
				}
				else {
					int j = i - 1;
					while (S[j] == '0') j--;
					
					S[j]--;
					FOR(k, j + 1, S.size()) S[k] = '9';
				}
				
				ok = false;
				break;
			}
			
			if (ok) break;
		}
				
		printf("Case #%d: %s\n", Case + 1, S.c_str());
	}
	return 0;
}