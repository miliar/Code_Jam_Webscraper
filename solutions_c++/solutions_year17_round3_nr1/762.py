#include<cstdio>
#include<cstdlib>
#include<iostream>
#include<cmath>
#include<algorithm>
using namespace std;

const int N = 2000;

const double pi = atan(1.)*4;
int n,k;

struct cake
{
	double r, h;
}f[N];

double x[N][N];


bool cmp1(const cake &A, const cake &B)
{
	return (A.r > B.r)||(A.r == B.r && A.h > B.h);
}

bool cmp2(const cake &A, const cake &B)
{
	return (A.h > B.h);
}

double get(int p)
{
	double ans = 0;
	ans = f[p].r * f[p].r * pi + f[p].h * f[p].r * pi * 2.;
	sort(f+p+1, f+n, cmp2);
	for (int i = p+1;i < p+k;++ i)
		ans += f[i].h * f[i].r * pi * 2.;
	return ans;
}

int main(int argc, char *argv[])
{
	if (argc == 1)
	{
		freopen("in","r",stdin);
		freopen("out","w",stdout);
	}
	else
	{
		freopen(argv[1], "r", stdin);
		freopen("ans", "w",stdout);
	}

	int T;
	cin >> T;
	for (int Case = 1;Case <= T;++ Case)
	{
		scanf("%d%d", &n,&k);
		for (int i = 0;i < n;++ i)
			scanf("%lf%lf", &f[i].r, &f[i].h);
		double ans = 0;
		sort(f, f+n, cmp1);
		for (int i = 0;i <= n;++ i)
			for (int j = 0;j <= k;++ j)
				x[j][i] = 0;
		for (int i = 1;i <= k;++ i)
			for (int j = n-i;j >= 0;-- j)
				x[i][j] = max(x[i][j+1], x[i-1][j+1] + f[j].r * f[j].h * pi * 2.);
		for (int i = 0;i < n;++ i)
			ans = max(ans, f[i].r * f[i].r * pi + f[i].r * f[i].h * pi * 2. + x[k-1][i+1]);

		printf("Case #%d:", Case);
		printf(" %.8f", ans);
		puts("");
	}
	return 0;
}
