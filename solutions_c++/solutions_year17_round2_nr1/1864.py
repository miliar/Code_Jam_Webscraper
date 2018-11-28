#include <stdio.h>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;
int main()
{
	int T;
	scanf("%d", &T);

	for (int c = 1; c <= T; c++) {
		double N, D;

		scanf("%lf %lf", &D, &N);
		printf("Case #%d: ", c);
		vector<double>ANS(N);
		for (int i = 0; i < N; i++) {
			double K, S;
			cin>>K>>S;
			double dist = D - K;
			ANS[i] = dist / S;
		}
		sort(ANS.begin(), ANS.end());
		printf("%.6lf\n", D/ANS[N-1]);

	}
	return 0;
}
