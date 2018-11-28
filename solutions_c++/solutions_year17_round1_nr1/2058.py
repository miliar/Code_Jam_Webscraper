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

int T;
int h, w;
string str[25], ans[25];

int main() {
	cin >> T;
	
	REP(t, T) {
		printf("Case #%d:\n", t + 1);
		
		scanf("%d %d", &h, &w);
		REP(i, h) {
			cin >> str[i];
			ans[i] = str[i];
		}
		
		bool done[26] = {};
		
		for (int sh = h - 1; sh >= 0; sh--) for (int sw = w - 1; sw >= 0; sw--) {
			REP(i, h - sh) REP(j, w - sw) {
				bool ng = false;
				int cnt = -1;
				REP(k, sh + 1) REP(l, sw + 1) {
					int nx = j + l;
					int ny = i + k;
					
					if (ans[ny][nx] != '?') {
						if (cnt != -1 || done[ans[ny][nx] - 'A']) { ng = true; k=l=INF; break; }
						cnt = ans[ny][nx] - 'A';
					}
				}
				if (cnt == -1) ng = true;
				
				if (!ng) {
					REP(k, sh + 1) REP(l, sw + 1) ans[i + k][j + l] = cnt + 'A';
					done[cnt] = true;
				}
			}
		}
		
		REP(i, h) cout << ans[i] << endl;
	}
	
	return 0;
}
