#include <cstdio>
#include <cstring>

using namespace std;

char s[1010];

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int test;scanf("%d",&test);
	for (int T=1;T<=test;T++)
	{
		scanf("%s",s);int n=strlen(s),k;
		scanf("%d",&k);int ans=0;
		for (int i=0;i<=n-k;i++)
			if (s[i]=='-')
			{
				for (int j=i;j<i+k;j++)
					if (s[j]=='+') s[j]='-'; else s[j]='+';
				ans++;
			}
		bool ok=1;
		for (int i=0;i<n;i++) if (s[i]=='-') ok=0;
		printf("Case #%d: ",T);
		if (ok) printf("%d\n",ans); else puts("IMPOSSIBLE");
	}
	return 0;
}
		
