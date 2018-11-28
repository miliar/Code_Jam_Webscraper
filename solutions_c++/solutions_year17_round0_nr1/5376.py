#include "stdio.h"

int main()
{
	int t;
	scanf("%d", &t);
	for (int tc = 0; tc < t; tc++)
	{
		printf("Case #%d: ", tc+1);

		char cstring[1001] = { 0 };
		int K = 0;
		scanf("%s %d", cstring, &K);

		int length = 0;
		while (cstring[length] != NULL)
		{
			length++;
		}
		bool isImposible = false;
		int command = 0;
		for (int i = 0; i < length; i++)
		{
			if (cstring[i] == '-')
			{
				command++;
				for (int j = 0; j < K; j++)
				{
					if (i + j >= length)
					{
						isImposible = true;
						break;
					}
					else
					{
						if (cstring[i + j] == '-')
						{
							cstring[i + j] = '+';
						}
						else //if (cstring[i + j] == '-')
						{
							cstring[i + j] = '-';
						}
					}
				}
			}
			if (isImposible == true)
				break;
		}
		if (isImposible == true)
		{
			printf("IMPOSSIBLE");
		}
		else
		{
			printf("%d", command);
		}
		printf("\n");
	}
	
}