#include<stdio.h>
#include<algorithm>
#include<queue>
using namespace std;
typedef pair<long long int, int> pli;
typedef pair<double, int> pdi;
int n, m;
int a[109];
double v[109];
int b[102][102];
long long int d[102][102];
void build_d(int si) {
	int i, j, k;
	d[si][si] = 0;
	//d[si][k] = minimum time to go with a[si]
	long long int limit = a[si];
	priority_queue<pli> tq;
	tq.push(pli(0, si));
	while (!tq.empty())
	{
		pli tt = tq.top();
		tq.pop();
		int ti = tt.second;
		long long int tm = -tt.first;
		if (d[si][ti] < tm) continue;
		for (i = 0; i < n; i++) {
			if (b[ti][i] < 0) continue;
			if (d[si][i] < 0 || d[si][i] > tm + (b[ti][i]))
			{
				if (tm + b[ti][i] <= limit)
				{
					d[si][i] = tm + b[ti][i];
					tq.push(pli(-d[si][i], i));
				}
			}
		}
	}
}
double f[102];
void dijk(int si, int ei) {
	int i, j, k;
	for (i = 0; i < n; i++)
		f[i] = -1;
	f[si] = 0;
	priority_queue<pdi> tq;
	tq.push(pdi(0, si));

	while (!tq.empty())
	{
		pdi tt = tq.top();
		tq.pop();
		int ti = tt.second;
		double tm = -tt.first;
		if (f[ti] + 1e-9 < tm) continue;
		for (i = 0; i < n; i++) {
			if (d[ti][i] < 0) continue;
			double dk = d[ti][i] / v[ti];
			if (f[i] < 0 || f[i] > tm + dk)
			{
				f[i] = tm + dk;
				tq.push(pdi(-f[i], i));
			}
		}
	}
	printf(" %.9lf", f[ei]);
}
int main() {
//	freopen("C-small-attempt0.in", "rt", stdin);
//	freopen("C-small-attempt0.out", "wt", stdout);
	freopen("C-large.in", "rt", stdin);
	freopen("C-large.out", "wt", stdout);
	int t=1, tv = 0;
	int i, j, k, l;
	scanf("%d", &t);
	while (t--)
	{
		scanf("%d %d", &n, &m);
		printf("Case #%d:", ++tv);
		for (i = 0; i < n; i++) {
			scanf("%d %lf", &a[i], &v[i]);
		}
		for (i = 0; i < n; i++) {
			for (j = 0; j < n; j++) {
				scanf("%d", &b[i][j]);
				d[i][j] = -1;
			}
		}
		for (i = 0; i < n; i++)
		{
			build_d(i);
		}
		while (m--) {
			scanf("%d %d", &i, &j);
			i--; j--;
			dijk(i, j);
		}
		printf("\n");
	}
}