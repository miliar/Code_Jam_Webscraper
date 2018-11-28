#include<cstdio>

using namespace std;

struct horse
{
	long long int maxD;
	int maxS;
};
	
int n, q;
horse horses[100];
long long int tab[100][100];

long double check(int k)
{
	if(k == n-1)
		return 0;
	long double bestTime = -1;
	int idx = k + 1;
	while(idx < n && tab[k][idx] <= horses[k].maxD)
	{
		long double time = (long double)tab[k][idx] / (long double)horses[k].maxS;
		long double x = check(idx);
		if(x != -1)
		{
			time += x;
			if(bestTime == -1 || bestTime > time)
				bestTime = time;
		}
		idx++;
	}
	//printf("%d %Lf\n", k, bestTime);
	return bestTime;
}
		
int main()
{
	int t;
	scanf("%d", &t);
	for(int tt = 1; tt <= t; tt++)
	{
		scanf("%d %d", &n, &q);
		for(int i = 0; i < n; i++)
		{
			scanf("%lld %d", &horses[i].maxD, &horses[i].maxS);
		}
		for(int i = 0; i < n; i++)
		{
			for(int j = 0; j < n; j++)
				scanf("%lld", &tab[i][j]);
		}
		for(int i = 0; i < n; i++)
			for(int j = i+2; j < n; j++)
				tab[i][j] = tab[i][j-1] + tab[j-1][j];
		
		int u, v;
		for(int i = 0; i < q; i++)
			scanf("%d %d", &u, &v);
		
		printf("Case #%d: ", tt);
		printf("%Lf\n", check(0));
	}
	return 0;
}

