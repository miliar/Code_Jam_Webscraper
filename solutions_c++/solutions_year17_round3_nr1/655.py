#include<cstdio>
#include<algorithm>
#define Pi (double)3.1415926535
#define N 1010
using namespace std;

struct Data
{
	int r, h;
	void read(){scanf("%d%d", &r, &h);}
}A[N];
bool operator < (Data a, Data b){return (a.r < b.r);}
int T, n, k;
double ans, B[N];

void Calc()
{
	ans = 0;
	for (int i = k; i <= n; i++)
	{
		double temp = (double)A[i].r * A[i].r * Pi + (double)A[i].r * A[i].h * 2 * Pi;
		int tot = 0;
		for (int j = 1; j < i; j++) B[++tot] = (double)A[j].r * A[j].h;
		sort(B + 1, B + 1 + tot); 
		for (int j = tot; j > tot - k + 1; j--) temp += B[j] * 2.0 * Pi;
		if (temp > ans) ans = temp;
	}
}

int main()
{
//	freopen("A.in", "r", stdin);
//	freopen("A.out", "w", stdout);
	scanf("%d", &T);
	for (int I = 1; I <= T; I++)
	{
		scanf("%d%d", &n, &k);
		for (int i = 1; i <= n; i++) A[i].read();
		sort(A + 1, A + 1 + n);
		Calc();
		printf("Case #%d: %lf\n", I, ans);
	}
	return 0;
}
