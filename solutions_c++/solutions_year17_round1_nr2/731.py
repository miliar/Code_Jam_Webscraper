#include <stdio.h>
#include <vector>
#include <algorithm>
using namespace std;

#define INF 987654321

struct state {
	int l, r;
};

int cnt;

vector<int> bef_idx;
vector<int> now_idx;
vector<state> crr[100];

int N, P;

bool entire_chk;

void dfs(int i, int left, int right);

int main() {

	int T;
	scanf("%d", &T);

	for (int tt = 1; tt <= T; tt++) {

		scanf("%d %d", &N, &P);

		vector<int> arr(N);

		for (int i = 0; i < N; i++) scanf("%d", &arr[i]);

		vector<int> brr[100];

		for (int i = 0; i < N; i++) {
			brr[i] = vector<int>(P);
			for (int j = 0; j < P; j++) {
				scanf("%d", &brr[i][j]);
			}
			sort(brr[i].begin(), brr[i].end());
		}

		for (int i = 0; i < N; i++) {
			crr[i] = vector<state>(P);
			for (int j = 0; j < P; j++) {
				int upper = 10 * brr[i][j];
				int down1 = 11 * arr[i];
				int down2 = 9 * arr[i];

				crr[i][j].r = upper / down2;
				crr[i][j].l = upper / down1;
				if (upper%down1 != 0) crr[i][j].l++;
				if (crr[i][j].l > crr[i][j].r) {
					crr[i][j].l = -1;
					crr[i][j].r = -1;
				}
			}
		}

		cnt = 0;

		bef_idx = vector<int>(N, -1);
		now_idx = vector<int>(N, 0);

		while (1) {
			entire_chk = false;
//			printf("now idx :\n");
//			for (int i = 0; i < N; i++) printf("%d ", now_idx[i]);
//			printf("\n");
			dfs(0, 0, INF);
			for (int i = 0; i < N; i++) now_idx[i]++;
			if (now_idx[0] >= P) break;
		}
		printf("Case #%d: %d\n", tt, cnt);
	}
}
void dfs(int i, int left, int right) {
//	printf("i : %d, left : %d, right : %d\n", i, left, right);

	if (i == N) {
		cnt++;
		entire_chk = true;
		return;
	}
	bool chk = false;
	for (int k = now_idx[i]; k < P; k++) {
	//	printf("k : %d\n", k);

		if (!(crr[i][k].l > right || left > crr[i][k].r)) {
			dfs(i + 1, max(crr[i][k].l, left), min(right, crr[i][k].r));
			if (entire_chk) {
				now_idx[i] = k;
				chk = true;
				break;
			}
		}
	}
	if (!chk) return;
}