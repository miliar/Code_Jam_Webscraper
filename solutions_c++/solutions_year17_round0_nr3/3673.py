#include <stdio.h>
#include <iostream>
#include <cstring>
#include <string>
#include <vector>
#include <unordered_map>
#include <queue>
#include <stdint.h>
using namespace std;
#define small
int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);

	int T;
	scanf("%d", &T);
	int cnt = 1;
	uint64_t N, K;
	priority_queue<uint64_t> queue;

	while (T--)
	{
		bool impossible = false;
		scanf("%lld %lld", &N, &K);
		while (!queue.empty()) queue.pop();
#ifdef small
		queue.push(N);
		for (uint64_t i = 0; i < K; i++)
		{
			uint64_t value = queue.top();
			queue.pop();
			value = value - 1;
			uint64_t left, right;
			if (value % 2 == 0)
			{
				left = value / 2;
				right = value / 2;
			}
			else
			{
				left = value / 2 + 1;
				right = value / 2;
			}
			if (left == 0 && right == 0)
			{
				printf("Case #%d: ", cnt++);
				printf("%lld %lld\n", left, right);
				break;
			}
			queue.push(left);
			queue.push(right);
			if (i == K - 1)
			{
				printf("Case #%d: ", cnt++);
				printf("%lld %lld\n", left, right);
			}
		}
#else
#endif

	}
	return 0;
}