#include "iostream"
#include "cstdio"
#include "cstdlib"
#include "string.h"

using namespace std;



char s[100];
int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
	int T, cas = 0;
	scanf("%d",&T);
	while(T--)
	{
		cas++;
		scanf("%s", s);
		int len = strlen(s);
		int pos = len;
		for (int i = 1; i < len; i++)
		{
			if (s[i] < s[i-1])
			{
				pos = i;
				break;
			}
		}
		if (pos == len)
		{
			printf("Case #%d: %s\n", cas, s);
			continue;
		}
		pos--;
		for (int i = pos; i >= 1; i--)
		{
			if (s[i] == s[i-1])
			{
				pos = i-1;
			}
			else break;
		}
		s[pos]--;
		for (int i = pos + 1; i < len; i++)
		{
			s[i] = '9';
		}
		char* pp = s;
		if (pos == 0 && s[0] == '0') pp = s + 1;
		printf("Case #%d: %s\n", cas, pp);
	}
	return true;
}
