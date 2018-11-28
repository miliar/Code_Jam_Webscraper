#include<stdio.h>
#include<string.h>
int main()
{
	int t,n,k,i,j,p,look,count;
	char s[10000];
	scanf("%d",&t);
	for(i=0;i<t;i++)
	{
		scanf("%s",s);
		scanf("%d",&k);
		n=strlen(s);
		look=0;
		count=0;
		for(j=0;j<n;j++)
		{
		    //printf("%d   %c\n",j,s[j]);
			if(s[j]=='-'&&j+k-1<n)
			{
				count++;
				//printf("%d   %c\n",j,s[j]);
				for(p=j;p<j+k;p++)
				{
					if(s[p]=='-')
					s[p]='+';
					else
					s[p]='-';
				}
			}
			else if(s[j]=='+')
			continue;
			else
			{
				look=-1;
				break;
			}
		}
		if(look==-1)
		{
			printf("Case #%d: IMPOSSIBLE\n",i+1);
		}
		else
		printf("Case #%d: %d\n",i+1,count);
	}
	return 0;
}
