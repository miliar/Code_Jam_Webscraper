#include<cstdio>
#include<cstring>
#include<string>

using namespace std;

char s[20];

bool is_tidy(int len)
{
	for (int i = 1; i < len; i++)
		if (s[i] < s[i - 1])
			return false;

	return true;
}

int main()
{
	freopen("in.in", "rt", stdin);
	freopen("out.out", "w", stdout);

	int test;

	scanf("%d", &test);

	for (int t = 0; t < test; t++)
	{
		scanf(" %s", &s);

		int len = strlen(s);

		while (!is_tidy(len))
		{
			for (int i = 1; i < len; i++)
			{
				if (s[i] >= s[i - 1])
					continue;

				if (s[i - 1] == '0')
					while (s[i - 1] == '0')
						i--;

				s[i - 1]--;

				for (; i < len; i++)
					s[i] = '9';

			}
		}

		std::string str(s);
		str.erase(0, str.find_first_not_of('0'));

		printf("Case #%d: %s\n", t + 1, str.c_str());
	}
}