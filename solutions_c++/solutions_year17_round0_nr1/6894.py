#include <iostream>
#include <cstdio>
#include <vector>
using namespace std;

#define _CRT_SECURE_NO_WARNINGS

int T;
char pancakes[1100];
int K;

int main()
{
	FILE* file;
	freopen_s(&file, "input.txt", "r", stdin);
	FILE* file_2;
	freopen_s(&file_2, "output.txt", "w", stdout);
	scanf_s("%d", &T);
	for (int test_i = 0; test_i < T; test_i++)
	{
		scanf_s(" %s", pancakes, sizeof(pancakes));
		scanf_s(" %d", &K);

		int result = 0;
		int max_size = strlen(pancakes) - K;
		for (int i = 0; i <= max_size; i++)
		{
			if (pancakes[i] == '-')
			{
				for (int j = i; j < i + K; j++)
				{
					if (pancakes[j] == '-')
					{
						pancakes[j] = '+';
					}
					else
					{
						pancakes[j] = '-';
					}
				}
				result++;
			}
		}

		bool possible = true;
		for (int i = max_size; i < max_size + K; i++)
		{
			if (pancakes[i] == '-')
			{
				possible = false;
			}
		}


		if (possible)
		{
			printf_s("Case #%d: %d\n", test_i + 1, result);
		}
		else
		{
			printf_s("Case #%d: IMPOSSIBLE\n", test_i + 1);
		}

	}
	return 0;
}