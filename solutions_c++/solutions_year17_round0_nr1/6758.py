#include <stdio.h>
#include <string.h>
using namespace std;

int main()
{
	int T, K, i, j, len, k, count;
	char S[1100];

	scanf("%d", &T);

	for(i = 1; i <= T; i++)
	{
		count = 0;
		scanf("%s%d", S, &K);

		len = strlen(S);

		for(j = 0; j < len; j++)
		{
			if(S[j] == '+')
			{
				continue;
			}
			else if(len - j < K)
			{
				count = -1;
				break;
			}
			else
			{
				count++;
				for(k = 0; k < K; k++)
				{
					if(S[j + k] == '+')
					{
						S[j + k] = '-';
					}
					else
					{
						S[j + k] = '+';
					}
				}
			}
		}

		if(count != -1)
		{
			printf("Case #%d: %d\n", i, count);
		}
		else
		{
			printf("Case #%d: IMPOSSIBLE\n", i);
		}
	}
	return 0;
}