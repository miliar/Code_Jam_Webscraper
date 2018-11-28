//#include <bits/stdc++.h>
#include<string.h>
#include<stdio.h>
#include<algorithm>
#include<queue>
#include<vector>
#include<cmath>
#include<math.h>
#define MAX 1450

using namespace std;


void _main(int TEST)
{
	int N, K;
	scanf("%d%d", &N, &K);
	double L; 
	scanf("%lf", &L);

	double A[100] = { 0, };

	int i,j;
	for (i = 0; i < N; i++) {
		scanf("%lf",&A[i]);
	}
	std::sort(A, A + N);

	double ans = 1;
	for (i = 0; i < N; i++) {
		if (N-1==i || L < (i + 1) * (A[i + 1] - A[i])) {
			double tmp = L/(i+1);
			for (j = 0; j <= i; j++) {
				A[j] += tmp;
			}
			break;
		}
		L -= (i + 1) * (A[i + 1] - A[i]);
		for (j = 0; j <= i; j++) {
			A[j] = A[i + 1];
		}
	}


	for (i = 0; i < N; i++) {
		ans *= A[i];
	}
	printf("%.6lf\n", ans);
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
