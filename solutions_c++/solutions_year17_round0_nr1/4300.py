#include<cstdio>
#include<cstdlib>
#include<cstring>

using namespace std;

int T,k;

char s[10000];

int main()
{
	scanf("%d",&T);
	for (int t=1;t<=T;t++)
	{
		scanf("%s",s+1);
		int l=strlen(s+1);
		scanf("%d",&k);
		int ans=0;
		for (int a=1;a+k-1<=l;a++)
			if (s[a]=='-')
			{
				ans++;
				for (int b=0;b<k;b++)
					if (s[a+b]=='+') s[a+b]='-';
					else s[a+b]='+';
			}
		bool able=true;
		for (int a=1;a<=l;a++)
			if (s[a]=='-') able=false;
		printf("Case #%d: ",t);
		if (able) printf("%d\n",ans);
		else printf("IMPOSSIBLE\n");
	}

	return 0;
}
