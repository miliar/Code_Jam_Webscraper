#include<stdio.h>
#include<string.h>
void flip(char s[],int a,int n)
{
	int i;
	for(i=a;i<n;i++)
	{
		if(s[i]=='-')
		s[i] = '+';
		else
			s[i] = '-';		
	}
}
int main()
{
	freopen("A-large.in", "rt", stdin);
	freopen("Result.out", "wt", stdout);

	int test,Cases,j,r,k,p,c,flag=0;
	char s[1000];
	scanf("%d",&Cases);
	for(test=0;test<Cases;test++)
	{
		printf("Case #%d:",test+1);
		c =0;
		r = 0;
		scanf("%s",s);
		p = strlen(s);
		scanf("%d",&k);
		int n =0;
		for(j=0;j<p;j++)
		{
			if(s[j]!='+')
			{
				r = j+k;
				if(r>p)
				{
					printf(" IMPOSSIBLE\n");
					flag = 1;
					break;
				}
				flip(s,j,r);
				c++;
			}
		}
		if(flag!=1)
			printf(" %d\n",c);
		flag = 0;
	}
	return 0;
}
