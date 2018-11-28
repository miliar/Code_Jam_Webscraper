#include<stdio.h>
int main()
{
	bool b;
	int n, k, i, j, c, l;
	char s[1001];
	scanf("%i",&n);
	for(i=0;i<n;i++)
	{
		b=true;
		c=0;
		scanf("%s %d", s, &k);
		for(j=0;s[j+k-1]!=0;j++)
		{
			if(s[j]=='-')
			{
				for(l=0;l<k;l++)
				{
					if(s[j+l]=='+')
						s[j+l]='-';
					else
						s[j+l]='+';
				}
				c++;
			}
		}
		printf("Case #%d: ",i+1);
		for(;s[j]!='\0';j++)
		{
			if(s[j]!='+')
			{
				printf("IMPOSSIBLE\n");
				b=false;
				break;
			}
			
		}
		if(b)
			printf("%d\n",c);
		
	}
	return 0;
}
