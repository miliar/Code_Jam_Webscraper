#include <iostream>
#include <vector>
#include <cstdio>
#include <algorithm>
#include <set>
#include <map>
#include <cassert>
#include <numeric>
#include <string>
#include <cstring>
#include <cmath>
using namespace std;

#ifdef LOCAL
	#define eprintf(...) fprintf(stderr, __VA_ARGS__)
#else
	#define eprintf(...) 42
#endif

typedef long long int int64;

const int LEN = 30;
char str[LEN];

void solve()
{
	scanf("%s", str);
	int n = strlen(str);

	int fst = -1;
	for (int i = 1; i < n; i++)
	{
		if (str[i] < str[i - 1] )
		{
			fst = i;
			break;
		}
	}
	if (fst == -1)
	{
		printf("%s\n", str);
		return;
	}
	int pos = fst - 1;
	while (pos > 0 && str[pos - 1] == str[pos] ) pos--;
	str[pos]--;
	for (int i = pos + 1; i < n; i++)
		str[i] = '9';
	int x = 0;
	while (str[x] == '0') x++;
	printf("%s\n", str + x);
}

void multitest()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int n;
	scanf("%d", &n);
	for (int i = 1; i <= n; i++)
	{
		printf("Case #%d: ", i);
		eprintf("Case #%d .. %d\n", i, n);
		solve();
	}


}

int main(int argc, char **)
{
	if (argc == 1)
		multitest();
	else
		solve();

	return 0;
}


