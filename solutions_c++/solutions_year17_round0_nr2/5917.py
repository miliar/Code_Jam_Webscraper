#include <bits/stdc++.h>
using namespace std;
#define ll long long int
char s[20],ans[20];
int l;
bool calc(int x,int p)
{
	if(x==l) 
		{
			ans[x]='\0';
			return true;
		}
	if(calc(x+1,s[x]-'0')&&(s[x]-'0'>=p))
	{
		ans[x]=s[x];
		return true;
	}
	else if(s[x]!='0')
	{
		if(s[x]-1-'0'<p) return false;
		ans[x]=s[x]-1;

		for(int i=x+1;i<l;i++) ans[i]='9';
			ans[l]='\0';
		return true;
	}
	return false;
}
int main()
{
	int t,i,no=0;
	scanf("%d",&t);
	while(t--)
	{
		no++;
		scanf(" %s",s);
		l=strlen(s);
		printf("Case #%d: ",no);
		if(calc(0,0))
		{
			bool f=false;
			for(i=0;ans[i]!='\0';i++)
			{
				if(f) printf("%c",ans[i]);
				else
				{
					if(ans[i]=='0') continue;
					else f=true,printf("%c",ans[i]);
				}

			}
			if(!f) printf("0");
		}
		else printf("0");
		printf("\n");
	}
	return 0;
}