#include <stdio.h>
#include <string.h>
int main()
{
	freopen( "B-large.in", "r", stdin );
	freopen( "output.txt", "w", stdout );
	long long int n,t,i,j,sum,rsv,lol;
	char s[100];
	scanf("%lld",&t);
	for(lol=1;lol<=t;lol++)
	{
		scanf(" %s",&s[0]);
		n=strlen(s);
		for(i=n-1;i>0;i--)
		{
			if(s[i]<s[i-1])
			{
//				printf("%lld\n",i);
				for(j=i;j<n;j++)
				s[j]='9';
				s[i-1]--;
			}
		}i=0;
		if(s[0]=='0')i++;
		printf("Case #%lld: ",lol);
		for(;i<n;i++)
		printf("%c",s[i]);
		printf("\n");
	}
	return 0;
}
		
