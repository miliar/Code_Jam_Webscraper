#include <stdio.h>
#include <string.h>

int main()
{
	int T;
	scanf("%d", &T);

	for (int t = 1; t <= T; t++)
	{
		char arr[20];
		scanf("%s", arr);

		int N = strlen(arr);

		for (int i = N - 1; i >= 1; i--)
		{
			if (arr[i] == '0' || arr[i] < arr[i - 1])
			{
				for (int j = i; j < N; j++)
				{
					arr[j] = '9';
				}

				for (int j = i - 1; j >= 0; j--)
				{
					if (arr[j] > '0')
					{
						arr[j]--;
						break;
					}
					else
					{
						arr[j] = '9';
					}
				}
			}
		}

		char* ans = arr;
		for (ans = arr; *ans == '0'; ans++);

		printf("Case #%d: %s\n", t, ans);
	}
	
	return 0;
}