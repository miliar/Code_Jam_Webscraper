#include <cstdio>
#include <string.h>

char str[10101];

int main(){

	int n=0;

	scanf("%d", &n);

	for (int i = 0; i < n; ++i)
	{
		int amount=0, flips = 0, impossible = 0;

		scanf("%s %d", str, &amount);

		int len = strlen(str);

		for (int j = 0; (j < len) && (!impossible); ++j)
		{
			if (str[j] == '-')
			{
				if ((j + amount) <= len)
				{
					for (int k = 0; k < amount; ++k)
					{
						if (str[j+k] == '-')
							str[j+k] = '+';
						else
							str[j+k] = '-';
					}
					flips++;
				} else 
					impossible =1;
			}
		}

		if (impossible)
		{
			printf("Case #%d: IMPOSSIBLE\n", i+1);
		}
		else {
			printf("Case #%d: %d\n", i+1, flips );
		}
	}
}