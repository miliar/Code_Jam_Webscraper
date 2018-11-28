#include <cstdio>
#include <algorithm>
#include <cstring>
#define int64 long long

using namespace std;

const int Maxn = 110;

double E[Maxn], S[Maxn];
double a[Maxn][Maxn];
double d[Maxn][Maxn];
double f[Maxn];
int q[1000000];
bool visit[Maxn];
int N, Q, T, l1, l2;

int main() {
	freopen("C-large.in.txt", "r",stdin);
	freopen("C-large.out","w",stdout);

	scanf("%d", &T);
	for (int ii=1;ii<=T;++ii) {
		printf("Case #%d:", ii);
		scanf("%d %d", &N, &Q);
		for (int i=1;i<=N;++i)
			scanf("%lf %lf", &E[i], &S[i]);
		for (int i=1;i<=N;++i)
			for (int j=1;j<=N;++j)
				d[i][j] = -1.0;
		for (int i=1;i<=N;++i)
			for (int j=1;j<=N;++j) {
				int x;
				scanf("%d", &x);
				d[i][j] = a[i][j] = x;
			}
		
		for (int k=1;k<=N;++k)
			for (int i=1;i<=N;++i)
				if (d[i][k] > -1e-7)
					for (int j=1;j<=N;++j)
						if (d[k][j] > -1e-7) {
							if (d[i][j] < -1e-7 || d[i][j] > d[i][k] + d[k][j])
								d[i][j] = d[i][k] + d[k][j];
						}
		for (int i=1;i<=N;++i)
			for (int j=1;j<=N;++j) {
				if (d[i][j] < -1e-7) 
					continue;
				if (d[i][j] <= E[i] + 1e-7) {
					d[i][j] /= S[i];
				}
				else d[i][j] = -1.0;
			}

		for (int i=0;i<Q;++i) {
			int s, t;
			scanf("%d %d", &s, &t);
			for (int j=1;j<=N;++j)
				f[j] = -1.0;
			f[s] = 0;
			l1 = 0; l2 = 1;
			memset(visit, false, sizeof(visit));
			visit[s] = true;
			f[s] = 0; q[0] = s;
			for (;l1 < l2;++l1) {
				int now = q[l1];
				visit[now] = false;
				for (int j = 1;j<=N;++j)
					if (d[now][j] > -1e-7) {
						if (f[j] < -1e-7 || f[j] > f[now] + d[now][j]) {
							f[j] = f[now] + d[now][j];
							if (!visit[j]) {
								visit[j] = true;
								q[l2++]= j;
							}
						}
					}
			}
			printf(" %.8lf", f[t]);
		}
		printf("\n");
	}

	return 0;
}