#include <iostream>
#include <cstdio>
#include <vector>
#include <cmath>
using namespace std;

const int maxs = int(1e6)+5, maxn = 55, maxp = 55;

int W[maxn], Q[maxn][maxp], ptr[maxn];

void solve()
{
	int n, p;
	scanf("%d%d", &n, &p);
	for(int i = 0;i < n;i++) ptr[i] = 0;

	for(int i = 0;i < n;i++) scanf("%d", &W[i]);

	for(int i = 0;i < n;i++)
	{
		for(int j = 0;j < p;j++) scanf("%d", &Q[i][j]);
		sort(Q[i], Q[i]+p);
	}

	int res = 0;
	for(int serv = 0;serv <= maxs;serv++)
	{
		bool cando = 1;
		for(int i = 0;i < n;i++)
		{
			pair<int, int> r = {ceil(0.9*double(serv*W[i])), floor(1.1*double(serv*W[i]))};

			if(ptr[i] == p)
			{
				cando = 0;
				break;
			}
			while(Q[i][ptr[i]] < r.first && ptr[i] < p)
			{
				ptr[i]++;
				if(ptr[i] == p) break;
			}
			if(ptr[i] == p)
			{
				cando = 0;
				break;
			}
			if(Q[i][ptr[i]] > r.second) cando = 0;
		}

		if(cando)
		{
			res++, serv--;
			for(int i = 0;i < n;i++) ptr[i]++;
		}
	}
	printf("%d\n", res);
}

int main(void)
{
	int t;
	scanf("%d", &t);
	for(int i = 1;i <= t;i++)
	{
		printf("Case #%d: ", i);
		solve();
	}
}