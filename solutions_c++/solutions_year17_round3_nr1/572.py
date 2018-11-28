//#include <bits/stdc++.h>
#include<string.h>
#include<stdio.h>
#include<algorithm>
#include<queue>
#include<vector>
#include<cmath>
#include<math.h>
#define MAX 1010
#define PI 3.1415926535897932384626433832795

using namespace std;

pair<long long, long long> D[MAX];
pair<long long, long long> Da[MAX];

long long Dy[MAX][MAX] = { 0, };

void _main(int TEST)
{
	int N,  K;
	long long ans;
	scanf("%d%d", &N,&K);
	


	int i, j, k;


	for (i = 0; i < N; i++) {
		for (j = 0; j < K; j++) {
			Dy[i][j] = 0;
		}
		D[i].first = D[i].second = 0;
		Da[i].first = Da[i].second = 0;
	}
	for (i = 0; i < N; i++) {
		scanf("%lld%lld", &D[i].first, &D[i].second);
		Da[i].first = D[i].first;
		Da[i].second = (long long)(D[i].first * D[i].second ) * 2;
	}

	std::sort(Da, Da + N);

	for (i = 0; i < N; i++) {
		Dy[i][0] = Da[i].second + Da[i].first * Da[i].first;
	}

	for (i = 1; i < K; i++) {
		for (j = 0; j < N; j++) {
			double min = -1;
			for (k = j + 1; k < N; k++) {
				if (min < Dy[k][i - 1]) min = Dy[k][i - 1];
			}
			if(min!= -1) Dy[j][i] = min + Da[j].second;
			else Dy[j][i] = -1;
		}
	}

	ans = 0;
	for (i = 0; i < N; i++) {
		if (ans < Dy[i][K - 1]) ans = Dy[i][K - 1];
	}


	printf("%.9llf\n", (double)ans * PI);
	return;
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int TEST;

	scanf("%d", &TEST);
	for (int i = 1; i <= TEST; i++)
	{
		//cerr << i << endl;
		printf("Case #%d: ", i);
		_main(i);
	}
	return 0;
}
