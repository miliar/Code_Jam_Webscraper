#include "bits/stdc++.h"
using namespace std;
#define rep(i,n) for(int (i)=0;(i)<(int)(n);++(i))
#define rer(i,l,u) for(int (i)=(int)(l);(i)<=(int)(u);++(i))
#define reu(i,l,u) for(int (i)=(int)(l);(i)<(int)(u);++(i))
static const int INF = 0x3f3f3f3f; static const long long INFL = 0x3f3f3f3f3f3f3f3fLL;
typedef vector<int> vi; typedef pair<int, int> pii; typedef vector<pair<int, int> > vpii; typedef long long ll;
template<typename T, typename U> static void amin(T &x, U y) { if (y < x) x = y; }
template<typename T, typename U> static void amax(T &x, U y) { if (x < y) x = y; }

int main() {
	int T;
	scanf("%d", &T);
	for (int ii = 0; ii < T; ++ ii) {
		long long N;
		scanf("%lld", &N);
		if (N == 1000000000000000000)
			-- N;
		vector<int> digits;
		for (ll x = N; x > 0; x /= 10)
			digits.push_back(x % 10);
		reverse(digits.begin(), digits.end());
		ll ans = 0;
		int lastd = 0;
		rep(i, digits.size()) {
			ll ones = 0, ten = 1;
			rep(j, (int)digits.size() - i) {
				ones = ones * 10 + 1;
				ten *= 10;
			}
			for (int d = 9; d >= lastd; -- d) {
				if (ans * ten + ones * d <= N) {
					ans = ans * 10 + d;
					lastd = d;
					break;
				}
			}
		}
		printf("Case #%d: ", ii + 1);
		printf("%lld\n", ans);
	}
	return 0;
}
