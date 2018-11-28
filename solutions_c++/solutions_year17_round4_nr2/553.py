#include <cstdio>
#include <algorithm>
#include <cstring>

using namespace std;

int p[1100], b[1100];
int f[1100][1100];
int a[1100];
int cnt[1100];
int sum[1100];
double D, v, x;
int T;

int main() {
	freopen("B-large.in.txt","r",stdin);
	freopen("B-large.out","w",stdout);

	scanf("%d", &T);
	for (int ii=1;ii<=T;++ii) {
		int N, M, C;
		printf("Case #%d: ", ii);
		scanf("%d %d %d", &N, &C, &M);
		memset(a, 0, sizeof(a));
		memset(cnt, 0, sizeof(cnt));
		memset(sum, 0, sizeof(sum));
		for (int i=0;i<M;++i) {
			scanf("%d %d", &p[i], &b[i]);
			a[b[i]] ++;
			cnt[p[i]] ++;
		}
		for (int i=1;i<=N;++i)
			sum[i] = sum[i - 1] + cnt[i];
		int res = 0;
		for (int i=1;i<=C;++i)
			res = max(res, a[i]);
		for (int i=0;i<=N;++i)
			for (int j=0;j<=M;++j)
				f[i][j] = 999999999;
		f[0][0] = 0;
		for (int i=0;i<=N;++i)
			for (int j=0;j<=M;++j) {
				if (f[i][j] >= 9999999) continue;
				f[i][j + 1] = min(f[i][j + 1], f[i][j]);
				for (int k=0;k<=cnt[i + 1];++k) {
					int rest = j * i - sum[i];
					if (rest < k) continue;
					int jj = max(j, cnt[i + 1] - k);
					f[i + 1][jj] = min(f[i + 1][jj], f[i][j] + k);
				}
			}
		int tmp = res;
		res = 999999999;
		int ans = 999999999;
		/*for (int i=0;i<=N;++i)
			for (int j=0;j<=M;++j)
				printf("%d %d : %d\n", i, j, f[i][j]);*/
		for (int j = 0;j <= M;++j) {
			if (f[N][j] < 99999999) {
				int _res = max(tmp, j);
				int _ans = f[N][j];
				if (_res < res || (_res == res && _ans < ans)) {
					res = _res;
					ans = _ans;
				}
			}
		}
		printf("%d %d\n", res, ans);
	}

	return 0;
}