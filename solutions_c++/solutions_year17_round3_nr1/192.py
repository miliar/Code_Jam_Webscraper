#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <algorithm>
using namespace std;

const int MaxN = 1007;
const double PI = acos(-1.0);

struct nodetype
{
	int R, H;
};

int T, N, M;
long long tmp[MaxN];
nodetype pan[MaxN];
double ans, res;

bool Comp(const nodetype A, const nodetype B)
{
	return (A.R < B.R);
}

inline double Calc(int L)
{
	double sum = 0.0;
	sort(tmp+1, tmp+L+1);
	for (int i=0; i<M-1; i++)
		sum += 2 * PI * tmp[L - i];
	return sum;
}

int main()
{
	freopen("A.in", "r", stdin);
	freopen("A.out", "w", stdout);

	scanf("%d", &T);
	for (int id = 1; id <= T; id++)
	{
		scanf("%d%d", &N, &M);
		for (int i=1; i<=N; i++)
		{
			scanf("%d%d", &pan[i].R, &pan[i].H);
		}
		sort(pan+1, pan+N+1, Comp);
		for (int i=1; i<M; i++)
			tmp[i] = (long long) pan[i].R * pan[i].H;
		ans = 0.0;
		for (int i=M; i<=N; i++)
		{
			res = PI * pan[i].R * pan[i].R + 2.0 * PI * pan[i].R * pan[i].H;
			res += Calc(i-1);
			if (ans < res) ans = res;
			//cout << i << ' ' << res << endl;
			tmp[i] = (long long) pan[i].R * pan[i].H;
		}
		printf("Case #%d: %.10lf\n", id, ans);
	}
	return 0;
}
