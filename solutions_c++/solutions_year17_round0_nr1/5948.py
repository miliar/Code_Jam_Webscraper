#include<bits/stdc++.h>
using namespace std;
char s[1002];
int main()
{
	int i,j,t,k,l,ans,no=0;
	scanf("%d",&t);
	while(t--)
	{
		ans=0;
		no++;
		scanf(" %s %d",s,&k);
		l=strlen(s);
		for(i=0;i<l;i++)
		{
			if((s[i]=='-')&&(i+k-1<l))
			{
				ans++;
				for(j=i;j<=i+k-1;j++)
					if(s[j]=='+') s[j]='-';
					else s[j]='+';
			}
		}
		for(i=0;i<l;i++)
			if(s[i]=='-')
				break;
		if(i==l) printf("Case #%d: %d\n",no,ans);
		else printf("Case #%d: IMPOSSIBLE\n",no);
	}
	return 0;
}