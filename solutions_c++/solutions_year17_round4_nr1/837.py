#include <bits/stdc++.h>
#define PB push_back
#define MP make_pair
#define F first
#define S second
#define SZ(x) ((int)(x).size())
#define ALL(x) (x).begin(),(x).end()
#ifdef _DEBUG_
	#define debug(...) printf(__VA_ARGS__)
#else
	#define debug(...) (void)0
#endif
using namespace std;
typedef long long ll;
typedef pair<int,int> PII;
typedef vector<int> VI;

int main() {
	int all_kase;
	scanf("%d", &all_kase);
	for(int num_kase = 1; num_kase <= all_kase; num_kase++) {
		int N, P;
		scanf("%d%d", &N, &P);
		int cnt[10] = {0};
		for(int i = 0; i < N; i++) {
			int G;
			scanf("%d", &G);
			G %= P;
			cnt[G]++;
		}
		int ans = cnt[0];
		if(P == 2)
			ans += (cnt[1] + 1) / 2;
		else if(P == 3) {
			int t = min(cnt[1], cnt[2]);
			ans += t;
			cnt[1] -= t;
			cnt[2] -= t;
			ans += (cnt[1] + cnt[2] + 2) / 3;
		}
		else if(P == 4) {
			ans += cnt[2] / 2;
			cnt[2] %= 2;
			int t = min(cnt[1], cnt[3]);
			ans += t;
			cnt[1] -= t;
			cnt[3] -= t;
			int k = cnt[1] + cnt[3] + 2 * cnt[2];
			ans += (k + 3) / 4;
		}
		printf("Case #%d: %d\n", num_kase, ans);
	}
	return 0;
}
