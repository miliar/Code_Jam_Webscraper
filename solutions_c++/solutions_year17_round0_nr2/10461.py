// tydi number

#include <cstdio>

using namespace std;

int main(void)
{
	//freopen("input.txt", "r", stdin);
	
	int T;
	
	scanf("%d", &T);
	//printf("T: %d\n", T);
	for (int t = 1; t <= T; t++)
	{
		long long N;

		scanf("%lld", &N);

		for (long long i = N; i > 0; i--)
		{
			long long K = i;
			long long last = K % 10;
			bool flag = true;
			//printf("%lld\n", i);
			while (K > 0)
			{
				long long n = K % 10;
				K /= 10;
			//	printf("n: %lld last: %lld\n", n, last);
				if(last >= n)
					last = n;
				else if (last < n)
				{
					flag = false;
					break;
				}
			}

			if (flag)
			{
				printf("Case #%d: %lld\n", t, i);
				break;
			}
		}
	}

	return 0;
}