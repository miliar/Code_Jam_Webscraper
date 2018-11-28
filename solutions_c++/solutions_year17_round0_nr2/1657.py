#include <cstdio>
#include <algorithm>
#include <cstdlib>
#include <cstring>
const int N = 20010;
typedef long long ll;
using namespace std;
char s[N];
bool a[N];
int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	int T,i1=1;
	scanf("%d", &T);
	while (T--)
	{
		scanf("%s", s);
		int len = strlen(s);
		int b = 1;
		while (1)
		{
			int flag = 1;
			for (int i = b; i < len; i++)
			{
				if (s[i] < s[i - 1])
				{
					s[i] = '9';
					for (int j = i + 1; j < len; j++)
						s[j] = '9';
					s[i - 1]--;
					flag = 0;
					break;
				}
			}
			if (flag)
				break;
		}
		printf("Case #%d: ",i1++);
		for (int i = 0; i < len; i++)
		{
			if (s[i] != '0')
			{
				printf("%s\n",s + i);
				break;
			}
		}
	}
	return 0;
}