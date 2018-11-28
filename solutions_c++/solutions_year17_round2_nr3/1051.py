#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <iostream>
#include <algorithm>

using namespace std;

const double INF = 1e100;

int N, Q;
int E[105], S[105];
long long Map[105][105];
double Dist[105], Used[105];

void Work()
{
	scanf("%d%d", &N, &Q);
	for (int i = 0; i < N; i ++)
		scanf("%d%d", &E[i], &S[i]);
	for (int i = 0; i < N; i ++)
		for (int j = 0; j < N; j ++)
		{
			int tmp;
			scanf("%d", &tmp);
			Map[i][j] = tmp;
		}

	for (int i = 0; i < N; i ++)
		Map[i][i] = 0;
	
	for (int k = 0; k < N; k ++)
		for (int i = 0; i < N; i ++)
			for (int j = 0; j < N; j ++)
				if (Map[i][k] != -1 && Map[k][j] != -1)
					if (Map[i][j] == -1 || Map[i][j] > Map[i][k] + Map[k][j])
						Map[i][j] = Map[i][k] + Map[k][j];

	while (Q --)
	{
		int Start, Target;
		scanf("%d%d", &Start, &Target);
		Start --;
		Target --;
		for (int i = 0; i < N; i ++)
		{
			Dist[i] = INF;
			Used[i] = 0;
		}
		Dist[Start] = 0;
		for (int i = 0; i < N; i ++)
		{
			int Min = -1;
			for (int j = 0; j < N; j ++)
				if (Dist[j] != INF && ! Used[j])
					if (Min == -1 || Dist[j] < Dist[Min])
						Min = j;
			if (Min == -1)
				break;
			Used[Min] = 1;
			for (int j = 0; j < N; j ++)
			{
				if (Map[Min][j] <= E[Min])
				{
					double t = (double) Map[Min][j] / (double) S[Min];
					if (Dist[j] > Dist[Min] + t)
						Dist[j] = Dist[Min] + t;
				}
			}
		}
		printf(" %.8lf", Dist[Target]);
	}
	printf("\n");
}

int main()
{
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("C-small.out", "w", stdout);
	int Cases;
	scanf("%d", &Cases);
	for (int Case = 1; Case <= Cases; Case ++)
	{
		printf("Case #%d:", Case);
		fprintf(stderr, "Case #%d: \n", Case);
		Work();
		fflush(stdout);
	}
	return 0;
}