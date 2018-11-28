#include<bits/stdc++.h>
using namespace std;
char s[100010];
int main()
{
	//freopen("input.in", "r", stdin);
//freopen("output.out", "w", stdout);
	int t,i,j,k;
	scanf("%d",&t);
	int temp=t;
	while(t--)
	{	
		scanf("%s %d",s,&k);
		int n=strlen(s),cnt=0,flag=0;
		for(i=0;i<n;i++)
		{
			if (s[i]=='+')
				continue;
			else
			{
				if (i+k>n)
				{	flag=1;break;}
				for(j=i;j<i+k;j++)
				{
					if (s[j]=='+')
						s[j]='-';
					else s[j]='+';
				}
				cnt++;
			}
		}
		printf("Case #%d: ",temp-t);
		if (flag)
			printf("IMPOSSIBLE\n");
		else printf("%d\n",cnt);
	}
	return 0;
}
		
