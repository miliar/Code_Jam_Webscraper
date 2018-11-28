#include <cstdio>
#include <cstring>

using namespace std;

char s[20];

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int test;scanf("%d",&test);
	for (int T=1;T<=test;T++)
	{
		scanf("%s",s);
		int n=strlen(s);
		for (int k=0;k<n;k++)
		{
			for (int i=1;i<n;i++)
				if (s[i]<s[i-1])
				{
					s[i-1]--;
					for (int j=i;j<n;j++) s[j]='9';
					break;
				}
		}
		int k=0;if (s[0]=='0') k++;
		printf("Case #%d: ",T);
		for (int i=k;i<n;i++) putchar(s[i]);
		puts("");
	}
	return 0;
}

