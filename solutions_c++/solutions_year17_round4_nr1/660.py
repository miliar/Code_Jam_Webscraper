#include <bits/stdc++.h>

using namespace std;

#define REP(i,n) for(int (i)=0;(i)<(int)(n);(i)++)
#define one first
#define two second
typedef long long ll;
typedef pair<int, int> pi;
const int INF = 0x3f2f1f0f;

int N, K, Cnt[10];

const int fre = 1;
void PROCESS(int tc) {
	printf("Case #%d: ", tc);
	REP(i, 10) Cnt[i] = 0;
	scanf("%d%d", &N, &K);
	for(int i=0, x; i<N; i++) scanf("%d", &x), Cnt[x%K]++;
	if(K == 2) {
		printf("%d\n", Cnt[0] + (Cnt[1] + 1) / 2);
		return;
	}
	if(K == 3) {
		int mV = min(Cnt[1], Cnt[2]);
		printf("%d\n", Cnt[0] + mV + (Cnt[1] + Cnt[2] - mV - mV + 2) / 3);
		return;
	}
	if(K == 4) {
		int mV = min(Cnt[1], Cnt[3]);
		int left = Cnt[1] + Cnt[3] - mV - mV;
		int plus2 = Cnt[2] / 2; Cnt[2] %= 2;

		int ans = Cnt[0] + mV + plus2 + left / 4; left %= 4;
		if(Cnt[2] >= 1 && left >= 2) ans++, Cnt[2]--, left -= 2;
		if(Cnt[2] >= 1 || left >= 1) ans++;
		printf("%d\n", ans);
	}
}
int main() {
	if(fre) freopen("output.txt", "w", stdout);
	int TC; cin >> TC;
	for(int tc=1; tc<=TC; tc++) PROCESS(tc);
	return 0;
}