#include <bits/stdc++.h>
using namespace std;

int k;
char a[1100];

int main()
{
	int T,pcnt=0;
	scanf("%d",&T);
	while(T--)
	{
		scanf("%s %d",a,&k);
		int ans=0,n=strlen(a);
		for (int i=0;i<=n-k;i++)
		if (a[i]=='-') {
			ans++;
			for (int j=i;j<i+k;j++)
				a[j]=a[j]=='-'?'+':'-';
		}
		for (int i=0;i<n;i++)
			if (a[i]!='+') goto no;
		printf("Case #%d: %d\n",++pcnt,ans);
		continue;
no:
		printf("Case #%d: IMPOSSIBLE\n",++pcnt);
	}
}
