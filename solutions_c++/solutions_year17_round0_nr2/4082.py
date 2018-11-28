#include<cstdio>
#include<cstring>
#include<cmath>
#include<cstdlib>
#include<algorithm>
using namespace std;
int a[10];
char s[20];
int T, n, m, l, ok, cnt;
int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	scanf("%d", &T);
	for(int i = 1; i <= T; i++)
	{
		scanf("%s", s);
		n = strlen(s);
		for(int j = n - 1; j >= 1; j--)
		{
			if(s[j] < s[j - 1])
			{
				for(int k = n - 1; k >= j; k--)s[k] = '9';
				s[j - 1]--;
			}
		}
		printf("Case #%d: ", i);
		if(s[0] != '0')printf("%c", s[0]);
		printf("%s", s + 1);
		printf("\n");
		memset(s, 0, sizeof(s));
	}
}
