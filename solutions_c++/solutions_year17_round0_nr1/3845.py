#include<cstdio>
#include<cstring>
#include<bitset>

using namespace std;

char s[1002];

int get_min(bitset<1000>& b, int k, int len)
{
	if (b.count() == len)
		return 0;

	int cnt = 0;

	for (int i = 0; i < len - k + 1; i++)
	{
		if (b[i])
			continue;

		cnt++;

		for (int j = i; j < i + k; j++)
			b.flip(j);
	}

	return b.count() == len ? cnt : -1;
}

int main()
{
	freopen("in.in", "rt", stdin);
	freopen("out.out", "w", stdout);
	int test, k, len;

	scanf("%d", &test);

	for (int t = 0; t < test; t++)
	{
		scanf(" %s %d", s, &k);
		len = strlen(s);
		bitset<1000> b;

		for (int i = 0; i < len; i++)
			b[i] = s[i] == '-' ? 0 : 1;

		int res = get_min(b, k, len);

		if (res == -1)
			printf("Case #%d: IMPOSSIBLE\n", t + 1);
		else
			printf("Case #%d: %d\n", t + 1, res);
	}

	return 0;
}