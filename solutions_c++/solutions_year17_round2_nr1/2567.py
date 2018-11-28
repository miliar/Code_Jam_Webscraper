#include <stdio.h>


int main(int argc, char** argv)
{
	freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);
    
	int T;
	scanf("%d", &T);
	
	for (int test = 0; test < T; test++)
	{
		int D, N;
		scanf("%d %d", &D, &N);
		double max_time = -1.0f;
		for (int j = 0; j < N; j++)
		{
			int d, v;
			scanf("%d %d", &d, &v);
			float tmp = ((double)(D - d))/v;
			max_time = tmp > max_time ? tmp : max_time;
		}
		
		double res = D / max_time;
		
		printf("Case #%d: %0.7f\n", test + 1, res);
	}	
	return 0;
}
