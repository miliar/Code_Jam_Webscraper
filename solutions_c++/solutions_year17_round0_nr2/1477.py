#include <bits/stdc++.h>
using namespace std;

typedef long long LL;

char s[20];

void solve()
{
	scanf("%s",s);
	int l=strlen(s),p=-1;
	for (int i=1;i<l;i++)
		if (s[i]<s[i-1])
		{
			p=i;
			break;
		}
	if (p==-1)
		puts(s);
	else
	{
		p--;
		while (p&&s[p]==s[p-1]) p--;
		s[p]--;
		if (p||s[p]>'0')
		{
			for (int i=0;i<=p;i++)
				putchar(s[i]);
			for (int i=p+1;i<l;i++)
				putchar('9');
		}
		else
			for (int i=1;i<l;i++)
				putchar('9');
		puts("");
	}
}

int main()
{
	freopen("read.txt","r",stdin);
	freopen("write.txt","w",stdout);
	int T;
	scanf("%d",&T);
	for (int i=1;i<=T;i++)
	{
		printf("Case #%d: ",i);
		solve();
	}
	return 0;
}
