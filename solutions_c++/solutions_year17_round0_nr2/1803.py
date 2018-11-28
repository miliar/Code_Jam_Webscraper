#include <cstdlib>
#include <iostream>
#include <cstring>

using namespace std;

typedef long long LL;

char s[20];
int a[20];
void Solve()
{
	cin >> s;
	int l = strlen(s);
	for (int i = 0; i < l; ++i)
		a[i + 1] = s[i] - '0';
	for (int i = l; i > 1; --i)
		if (a[i] < a[i - 1])
		{
			for (int j = i; j <= l; ++j) a[j] = 9;
			int j = i - 1;
			--a[j];
			while (a[j] < 0 && i)
			{
				a[j] += 10;
				--a[--j];
			}
		}
	int i = 1;
	while (a[i] == 0) ++i;
	while (i <= l) printf("%d", a[i++]);
	puts("");
}

int T;
int main()
{
	cin >> T;
	for (int i = 1; i <= T; ++i)
	{
		printf("Case #%d: ", i);
		Solve();
	}
	return 0;
}
