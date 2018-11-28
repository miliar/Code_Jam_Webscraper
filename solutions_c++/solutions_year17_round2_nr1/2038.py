#include <stdio.h>
#include <math.h>
#include <iostream>
#include <iomanip>

using namespace std;

int main()
{
	int T;
	cin >> T;
	for(int t = 0; t < T; t++)
	{
		int D, N;
		cin >> D >> N;
		double max=0;
		for(int n=0; n<N; n++)
		{
			int k, s;
			cin >> k >> s;
			double time = (double)(D-k)/s;
			if(time > max) max = time;
		}
		// long long tmp = D/max*1000000;
		// printf("Case #%d: %.6lf\n", t+1, tmp/1000000.0);
		printf("Case #%d: %.6lf\n", t+1, trunc(D/max*1000000.0)/1000000.0);
	}
	return 0;
}