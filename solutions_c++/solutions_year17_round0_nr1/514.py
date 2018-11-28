#include <cstdio>
#include <algorithm>
#include <cstdlib>
#include <cmath>
#include <vector>
#include <set>
#include <queue>

using namespace std;

char buff[50000];
bool flip[50000];

int K;

void solve()
{
	int N = strlen(buff);
	memset(flip, 0, 2*N*sizeof(bool));
	int j = K;
	char current = '+';
	int count = 0;
	for (int i=0; i<N; ++i, ++j)
	{
		if (current != buff[i])
		{
			if (i+K > N)
			{
				printf("IMPOSSIBLE");
				return;
			}
			flip[j] = true;
			current = buff[i];
			++count;
		}
		//sprintf(flip[j]?"1":"0");
		if (flip[j-K+1])
		{
			if (current == '+')
				current = '-';
			else
				current = '+';
		}
	}
	printf("%d", count);
}

int main()
{
	int T;
	scanf("%d\n", &T);
	for (int i=0; i<T; ++i)
	{
		scanf("%s%d\n", buff, &K);
		printf("Case #%d: ", i + 1);
		solve();
		printf("\n");
	}
	return 0;
}
