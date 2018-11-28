#include <cstdio>
#include <cstring>

using namespace std;

int main(int argc, char const *argv[])
{
	int t;
	scanf("%d", &t);
	for (int testcase = 1; testcase <= t; ++testcase)
	{
		char c[2000];
		scanf("%s", c);
		int k;
		scanf("%d", &k);
		int l = strlen(c);
		int ans = 0;
		for (int i = 0; i <= l-k; ++i)
		{
			if (c[i] == '-') {
				for (int j = i; j < i+k; ++j)
				{
					c[j] = c[j] == '-' ? '+' : '-';
				}
				ans++;
			}
		}
		bool impossible = false;
		for (int i = l-k+1; i < l; ++i)
		{
			if (c[i] == '-') {
				impossible = true;
			}
		}
		printf("Case #%d: ", testcase);
		if (impossible)
		{
			printf("IMPOSSIBLE\n");
		} else {
			printf("%d\n", ans);
		}
	}
	return 0;
}