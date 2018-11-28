#include <iostream>
#include <cstdio>
#include <stdint.h>
#include <vector>
#include <algorithm>
using namespace std;
void A()
{
	size_t T, D, N;
	vector<size_t> p, s, t;
	scanf("%d", &T);
	for (size_t cnt = 1; cnt <= T; cnt++)
	{
		scanf("%d %d", &D, &N);
		p.clear();
		s.clear();
		t.clear();
		p.resize(N);
		s.resize(N);
		t.resize(N);
		double max_s = 0;
		double max_t = 0;
		double res = 1e30;
		double answer = 1e30;
		double k, s;
		for (int i = 1; i <= N; ++i) {
			scanf("%Lf%Lf", &k, &s);
			double x = (D * s) / (D - k);
			answer = std::min(answer, x);
		}
		printf("Case #%d: %.6lf\n", cnt, answer);
	}
}

void C()
{
	size_t T;
	scanf("%d", &T);
	int n, p;
	const int N = 101;
	size_t h_e[N];
	size_t h_s[N];
	size_t dis[N][N];
	double time_dis[N][N];
	for (size_t cnt = 1; cnt <= T; cnt++)
	{
		scanf("%d%d", &n, &p);
		memset(h_e, 0, sizeof(h_e));
		memset(h_s, 0, sizeof(h_s));
		memset(dis, 0, sizeof(dis));
		memset(time_dis, 0, sizeof(time_dis));
		for (int i = 0; i < n; i++)
		{
			scanf("%lld%lld", &h_e[i], &h_s[i]);
		}
		for (int i = 0; i < n; i++)
		{
			for (int j = 0; j < n; j++)
			{
				int dist;
				scanf("%d", &dist);
				dis[i][j] = dist;
				time_dis[i][j] = -1;
			}
		}
		
		for (int k = 0; k < n; k++)
		{
			for (int i = 0; i < n; i++)
			{
				for (int j = 0; j < n; j++)
				{
					if (dis[i][k] != -1 && dis[k][j] != -1)
					{
						if (dis[i][j] == -1)
						{
							dis[i][j] = dis[i][k] + dis[k][j];
						}
						else
						{
							dis[i][j] = min(dis[i][j], dis[i][k] + dis[k][j]);
						}
					}
				}
			}
		}
		for (int i = 0; i < n; i++)
		{
			for (int j = 0; j < n; j++)
			{
				if (i == j)continue;
				if (dis[i][j] <= h_e[i])
				{
					time_dis[i][j] = dis[i][j] * 1.0 / h_s[i];
				}
			}
		}
		double eps = 1e-6;
		for (int k = 0; k < n; k++)
		{
			for (int i = 0; i < n; i++)
			{
				for (int j = 0; j < n; j++)
				{
					if ((abs(time_dis[i][k] - (-1)) > eps) && abs(time_dis[k][j] - (-1))>eps)
					{
						if (abs(time_dis[i][j] - (-1)) <eps)
						{
							time_dis[i][j] = time_dis[i][k] + time_dis[k][j];
						}
						else
						{
							time_dis[i][j] = min(time_dis[i][j], time_dis[i][k] + time_dis[k][j]);
						}
					}
				}
			}
		}

		printf("Case #%d: ", cnt);
		for (int i = 0; i < p; i++)
		{
			int first, second;
			scanf("%d%d", &first, &second);
			printf(" %.7lf", time_dis[first - 1][second - 1]);
		}
		printf("\n");
	}
}
//int main()
//{
//	freopen("in.txt", "r", stdin);
//	freopen("out.txt", "w", stdout);
//	//A();
//	C();
//	return 0;
//}