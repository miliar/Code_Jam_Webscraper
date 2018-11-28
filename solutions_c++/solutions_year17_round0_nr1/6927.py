#include <cstdio>
#include <iostream>
#include <string>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <vector>
#include <cstdlib>

using namespace std;

int main()
{
	int T;
	cin >> T;
	for (int i = 1; i <= T; i++)
	{
		int answer = 0;
		int K;
		char str[1010];
		scanf(" %[^ ] %d", str, &K);
		int len = strlen(str);

		int temp = len - K;
		for (int x = 0; x <= temp; x++)
		{
			if (str[x] == '-')
			{
				answer++;
				for (int l = 0, index = x; l < K; l++, index++)
				{
					(str[index] == '+') ? str[index] = '-' : str[index] = '+';
					//printf("(str[%d]=%c)", index, str[index]);
				}
			}
		}

		int flag = 0;
		for (int x = temp; x < len; x++)
		{
			if (str[x] == '-')
			{
				flag = 1;
				break;
			}
		}
		if (flag)
		{
			printf("Case #%d: IMPOSSIBLE\n",i);
		}
		else printf("Case #%d: %d\n", i, answer);
	}
}