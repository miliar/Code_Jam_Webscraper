#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cassert>

using namespace std;

int P[1111], B[1111];
int cnt[1111];
int cnt1[1111];
int N,C,M; 
bool check(int x){
	int left = 0;
	for (int i = 1; i <= N; i++){
		if (cnt[i] >= x) {
			int move = cnt[i] - x;
			if (move > left)
				return false;
			else 
				left -= move;
		} else {
			left += x - cnt[i];
		}
	}
	return true;
}

void work(){
	scanf("%d%d%d", &N, &C, &M);
	memset(cnt,0,sizeof(cnt));
	memset(cnt1,0,sizeof(cnt1));
	int ans1 = 0;
	for (int i = 0; i < M; i++) {
		scanf("%d%d", P + i, B + i);
		cnt[P[i]]++;
		cnt1[B[i]]++;
	}

	for (int i = 1; i <= C; i++)
		if (cnt1[i] >= ans1)
			ans1 = cnt1[i];

	int L = 1, R = M; // [L,R]
	for (int mid = (L + R)/2; L != R; check(mid) ? R = mid : L = mid + 1)
		mid = (L+R)/2;

	int ans2 = L;

	int ans = max(ans1, ans2);
	printf("%d ", ans);

	int need_place = 0;
	int result = 0;
	for (int i = N; i >= 1; i--){
		if (cnt[i] >= ans){
			need_place += cnt[i]-ans;
		} else {
			result += min(need_place, ans - cnt[i]);
			need_place -= min(need_place, ans - cnt[i]);
		}
	}
	printf("%d\n", result);
	assert(need_place == 0);
}
// 1 2 3
// 1 1 3
// 1 2 3

int main(){
	freopen("B.in", "r", stdin);
	int Tc; scanf("%d", &Tc);
	for (int T = 1; T <= Tc; T++){
		printf("Case #%d: ", T);
		work();
	}
}