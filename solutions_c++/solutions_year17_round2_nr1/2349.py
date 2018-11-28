#include <iostream>
#include <fstream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
using namespace std;

int main()
{
	freopen("A.in", "r", stdin);
	freopen("A.out", "w", stdout);

	int T;
	scanf("%d", &T);

	for (int tcase = 1; tcase <= T; ++tcase)
	{
		printf("Case #%d: ", tcase);
		double max_time = 0.0;
		int D, N;
		cin >> D >> N;
		for (int i = 0; i < N; ++i)
		{
			int K, S;
			cin >> K >> S;
			double cur_time = (double)(D - K)/(double)S;
			if (max_time < cur_time)
				max_time = cur_time;
		}
		printf("%.7f\n", D/max_time);
	}

	return 0;
}
