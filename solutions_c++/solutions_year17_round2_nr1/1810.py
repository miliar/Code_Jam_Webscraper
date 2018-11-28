#include<cstdio>
#include<cstring>
#include<iostream>
using namespace std;

const int N = 2000;
int p[N];
int s[N];
double t[N];

int main(int argc, char *argv[])
{
	if (argc == 1)
	{
		freopen("in", "r", stdin);
		freopen("out","w",stdout);
	}
	else
	{
		if (freopen(argv[1], "r",stdin) == NULL)
		{
			cerr << "open file failed" << endl;
			return 0;
		}
		freopen("ans","w",stdout);
	}
	int T;
	scanf("%d", &T);
	for (int Case = 1;Case <= T;++ Case)
	{
		double max_t = 0;
		int n,d;
		scanf("%d%d", &d, &n);
		for (int i = 0;i < n;++ i)
		{
			scanf("%d%d", &p[i], &s[i]);
			t[i] = (double)(d -p[i]) / s[i];
			max_t = max(max_t, t[i]);
		}
		printf("Case #%d: ", Case);
		printf("%.6lf\n", (double)d/max_t);
	}
	return 0;
}
