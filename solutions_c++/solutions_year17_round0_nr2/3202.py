#include <cstdio>
using namespace std;

#ifdef _MSC_VER
#pragma warning(disable: 4996) // Disable deprecation
#endif 

char* Solve(char *s)
{
	int cnt = 1;
	int j = 1;
	for (; s[j] && s[j - 1] <= s[j]; ++j)
	{
		if (s[j - 1] == s[j])
		{
			++cnt;
		}
		else
		{
			cnt = 1;
		}
	}
	if (s[j] != 0)
	{
		s[j - cnt] -= 1;
		for (int i = j - cnt + 1; s[i]; ++i)
		{
			s[i] = '9';
		}
		if (s[0] == '0')
		{
			return s + 1;
		}
	}
	return s;
}

int main()
{
//	freopen("b.in", "r", stdin);

	char buff[32];
	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; ++t)
	{
		scanf("%s", buff);
		char *s = Solve(buff);
		printf("Case #%d: %s\n", t, s);
	}

	fclose(stdout);
	return 0;
}
