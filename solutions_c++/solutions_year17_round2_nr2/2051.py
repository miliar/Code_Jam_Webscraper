#include <stdio.h>
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

char str[7] = "ROYGBV";

int main()
{
	freopen("B-small-attempt1.in", "r", stdin);
	freopen("output.txt", "w", stdout);

	int T;
	int test_case;

	scanf("%d", &T);
	for (test_case = 1; test_case <= T; test_case++) 
	{
		int n;
		int arr[6];
		scanf("%d", &n);
		for (int i = 0; i < 6; i++)
		{
			scanf("%d", &arr[i]);
		}

		int max = -1;
		int max_index = 0;
		for (int i = 0; i < 6; i++)
		{
			if (arr[i] > max)
			{
				max = arr[i];
				max_index = i;
			}
		}

		int result = 0;
		for (int i = 0; i < 6; i++)
		{
			if (i == max_index)
				continue;
			result += arr[i];
		}

		if (max > result)
		{
			printf("Case #%d: IMPOSSIBLE\n", test_case);
			continue;
		}

		int aa;
		int bb;

		if (max_index == 0)
		{
			aa = 2;
			bb = 4;
		}
		else if (max_index == 2)
		{
			aa = 0;
			bb = 4;
		}
		else if (max_index == 4)
		{
			aa = 2;
			bb = 0;
		}

		printf("Case #%d: ", test_case);
		int temp = 0;
		int flag = 0;

		for (int i = 0; i < n; i++)
		{
			if (arr[max_index] == arr[aa] + arr[bb])
				flag = 1;

			if (flag == 0)
			{
				arr[max_index]--;
				arr[aa]--;
				arr[bb]--;
				printf("%c%c%c", str[max_index], str[aa], str[bb]);
				i += 2;
			}
			else
			{
				if (temp == 0 && max > 0)
				{
					if (max <= 0)
					{
						temp = !temp;
						continue;
					}
					printf("%c", str[max_index]);
					max--;
				}
				else
				{
					for (int j = 0; j < 6; j++)
					{
						if (j == max_index)
							continue;
						if (arr[j])
						{
							printf("%c", str[j]);
							arr[j]--;
							break;
						}
					}

				}
				temp = !temp;
			}
		}

		printf("\n");

	}

}
/*

*/