#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
using namespace std;

#define DEBUG	1

#define MAX_N	1001

int T;
int D, N;
int K[MAX_N];
int S[MAX_N];

void solve()
{
	double maxT = 0;
	double time;

	for (int i = 0; i < N; i++)
	{
		time = (double)(D - K[i]) / (double)S[i];
		if (time > maxT)
			maxT = time;
	}
	printf("%f", (double)D / maxT);
}


int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);

	cin >> T;
	for (int t = 0; t < T; t++)
	{
		cin >> D >> N;
		for (int i = 0; i < N; i++)
		{
			cin >> K[i] >> S[i];
		}

		printf("Case #%d: ", t + 1);
		solve();
		printf("\n");
	}

	return 0;
}
