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

const int MAXN = 1000 + 50;
int cnt[2][MAXN];

int main() {
	int all_kase;
	scanf("%d", &all_kase);
	for(int num_kase = 1; num_kase <= all_kase; num_kase++) {
		int N, C, M;
		scanf("%d%d%d", &N, &C, &M);
		fill(cnt[0], cnt[0] + N + 1, 0);
		fill(cnt[1], cnt[1] + N + 1, 0);
		int num[2] = {0};
		for(int i = 0; i < M; i++) {
			int P, B;
			scanf("%d%d", &P, &B);
			B--;
			cnt[B][P]++;
			num[B]++;
		}
		int ans = max(num[0], num[1]);
		int ans2 = 0;
		int id = 0;
		for(int i = 0; i <= N; i++)
			if(cnt[0][i] + cnt[1][i] > cnt[0][id] + cnt[1][id])
				id = i;
		if(cnt[0][id] + cnt[1][id] > ans) {
			if(id == 1) ans = cnt[0][id] + cnt[1][id];
			else ans2 = cnt[0][id] + cnt[1][id] - ans;
		}
		printf("Case #%d: %d %d\n", num_kase, ans, ans2);
	}
	return 0;
}
