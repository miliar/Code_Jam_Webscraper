#include <bits/stdc++.h>
using namespace std;

char s[110];

int main()
{
	int T,tc=0;
	scanf("%d",&T);
	while(T--)
	{
		scanf("%s",s);
		int n = strlen(s);
		for (int i=n-1;i>0;i--) {
			if (s[i]<'0') s[i]+=10,s[i-1]--;
			for (int j=0;j<i;j++)
				if (s[j]>s[i]) {
					for (int k=i;k<n;k++) s[k]='9';
					s[i-1]--;
					break;
				}
		}
		int cnt=0;
		for (;cnt<n-1;cnt++)
			if (s[cnt]!='0') break;
		printf("Case #%d: %s\n",++tc,s+cnt);
	}
}
