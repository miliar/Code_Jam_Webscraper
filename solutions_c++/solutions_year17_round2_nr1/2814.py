//#include <bits/stdc++.h>
#include<string.h>
#include<stdio.h>
#include<algorithm>

using namespace std;

bool check(int D, int k1,int s1, int k2,int s2) {
	if (k1>k2 && (double)(D - k1) / s1 < (double)(D - k2) / s2) return true;
	if (k1 < k2 && (double)(D - k1) / s1 < (double)(D - k2) / s2) return true;
	return false;
}

void _main(int TEST)
{
	int D,N;
	scanf("%d%d", &D, &N);

	int K[1010] = { 0, }, S[1010] = { 0, };

	pair<int, int> KS[1010];
	double ans = 0;
	for (int i = 0; i < N; i++) {
		scanf("%d%d", &KS[i].first, &KS[i].second);
		double tmp = (double)(D - KS[i].first) / KS[i].second;
		if (tmp > ans) ans = tmp;
	}
	
	printf("%.6llf\n", D/ans);

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
