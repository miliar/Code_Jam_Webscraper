#include<iostream>
#include<cstdio>

using namespace std;

int main()
{
	int T;
	scanf("%d ", &T);
	for(int t=1; t<=T; t++)
	{
		cout << "Case #" << t << ": ";
		int D, N, K, S;
		double result = 0;
		scanf("%d %d ", &D, &N);
		while(N--)
		{
			scanf("%d %d ", &K, &S);
			double r = (D-K);
			r /= S;
			if(r>result)
				result = r;
		}
		printf("%.6f\n", D/result);
	}
	return 0;
}

