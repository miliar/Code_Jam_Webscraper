#include <stdio.h>
#include <iostream>
#include <cstring>
#include <string>
#include <vector>
#include <unordered_map>
using namespace std;
int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);

	int T;
	scanf("%d", &T);
	int cnt = 1;
	int N, K;
	const int max_value = 1024;
	char ch[max_value];
	bool map[max_value];
	
	while (T--)
	{
		bool impossible = false;
		scanf("%s %d", ch, &K);
		N = strlen(ch);
		for (int i = 0; i < N; i++)
		{
			map[i] = ch[i] == '-' ? false : true;
		}
		int res = 0;
		for (int i = 0; i < N-K+1; i++)
		{
			if (map[i] == false)
			{
				res++;
				for (int j = i; j < i + K; j++)
				{
					map[j] = !map[j];
				}
			}
		}
		for (int i = N - K + 1; i < N; i++)
		{
			if (map[i] == false)
			{
				impossible = true;
				break;
			}
		}
		printf("Case #%d: ", cnt++);
		if (impossible)
		{
			printf("IMPOSSIBLE\n");
		}
		else
		{
			printf("%d\n", res);
		}
	}
	return 0;
}