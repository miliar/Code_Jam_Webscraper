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
		long long N; long long K;
		scanf("%lld%lld", &N, &K);
		map<ll, ll> cnt;
		cnt[N] = 1;
		while (K > 1) {
			auto it = -- cnt.end();
			ll n = min(it->second, K - 1);
			if (it->first >= 3)
				cnt[(it->first - 1) / 2] += n;
			if (it->first >= 2)
				cnt[it->first / 2] += n;
			if((it->second -= n) == 0)
				cnt.erase(it);
			K -= n;
		}
		ll t = cnt.rbegin()->first;
		pair<ll, ll> ans = { t / 2, (t - 1) / 2 };
		printf("Case #%d: ", ii + 1);
		printf("%lld %lld\n", ans.first, ans.second);
	}
	return 0;
}
