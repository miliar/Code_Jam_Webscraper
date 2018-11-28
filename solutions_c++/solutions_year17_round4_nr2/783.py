// 3rd party library - CPLEX is used for solving the integer programming

#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <iostream>
#include <sstream>
#include <algorithm>
#include <string>
#include <map>
#include <vector>

using namespace std;

int nseat, ncustomer, nticket;
int P[10000], B[10000];
vector <int> seatcust[1005];

int N, M;
int Map[1005][1005];
int UsedY[1005], Link[1005];

int AugPath(int i)
{
	for (int j = 0; j < M; j ++)
		if (Map[i][j] && ! UsedY[j])
		{
			UsedY[j] = 1;
			if (Link[j] == -1 || AugPath(Link[j]))
			{
				Link[j] = i;
				return 1;
			}
		}
	return 0;
}

void Work()
{
	scanf("%d%d%d", &nseat, &ncustomer, &nticket);
	for (int i = 0; i < nseat; i ++)
		seatcust[i].clear();
	for (int i = 0; i < nticket; i ++)
	{
		scanf("%d%d", &P[i], &B[i]);
		P[i] --;
		B[i] --;
		seatcust[P[i]].push_back(B[i]);
	}
	// greedy
	if (ncustomer == 2)
	{
		vector <int> a, b;
		for (int i = 0; i < nticket; i ++)
			if (B[i] == 0)
				a.push_back(P[i]);
			else
				b.push_back(P[i]);
		sort(a.begin(), a.end());
		sort(b.begin(), b.end());
		
		int na = a.size();
		int nb = b.size();
		N = a.size();
		M = b.size();
		int match = 0;
		for (int i = 0; i < N; i ++)
			for (int j = 0; j < M; j ++)
				Map[i][j] = (a[i] + b[j] != 0);
		
		match = 0;
		memset(Link, -1, sizeof(Link));
		for (int i = 0; i < N; i ++)
		{
			memset(UsedY, 0, sizeof(UsedY));
			match += AugPath(i);
		}
		int pairs = match;
		int singles = N + M - match * 2;
		
		for (int i = 0; i < N; i ++)
			for (int j = 0; j < M; j ++)
				Map[i][j] = (a[i] != b[j]);

		int ans1 = pairs + singles;
		
		match = 0;
		memset(Link, -1, sizeof(Link));
		for (int i = 0; i < N; i ++)
		{
			memset(UsedY, 0, sizeof(UsedY));
			match += AugPath(i);
		}

		printf("%d %d\n", ans1, pairs - match);
	}
	else
	{
		int ansround = 0;
		for (int round = 0; ; round ++)
		{
			for (int i = nseat - 1; i >= 0; i --)
			{

			}
		}
	}
}

int main()
{
	freopen("B-small-attempt1.in", "r", stdin);
	freopen("B-small-attempt1.out", "w", stdout);
	int Cases;
	scanf("%d", &Cases);
	for (int Case = 1; Case <= Cases; Case ++)
	{
		printf("Case #%d: ", Case);
		fprintf(stderr, "Case #%d: \n", Case);
		Work();
		fflush(stdout);
	}
	return 0;
}
