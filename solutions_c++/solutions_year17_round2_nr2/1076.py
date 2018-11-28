#include<stdio.h>
int main()
{
	int i, j, t, c[7], col, col2, col3;
	char s[7]={'N','R','O','Y','G','B','V'};
	scanf("%d",&t);
	for(i=0;i<t;i++)
	{
		for(j=0;j<7;j++)
			scanf("%d", c+j);

		if(c[1]>c[0]/2 || c[3]>c[0]/2 || c[5]>c[0]/2)
			printf("Case #%d: IMPOSSIBLE\n",i+1);
		else
		{
			printf("Case #%d: ",i+1);
			if(c[1]>=c[3] && c[1]>=c[5])
			{
				col=1;
				col2=3;
				col3=5;
			}
			else if(c[3]>c[1] && c[3]>=c[5])
			{
				col=3;
				col2=1;
				col3=5;
			}
			else
			{
				col=5;
				col2=1;
				col3=3;
			}
			for(j=0;j<c[0];j++)
			{
				if(j%2==0 && c[col]>0)
				{
					printf("%c",s[col]);
					c[col]--;
				}
				else
				{
					if(c[col2]>=c[col3])
					{
						printf("%c",s[col2]);
						c[col2]--;
					}
					else
					{
						printf("%c",s[col3]);
						c[col3]--;
					}
				}
			}
			printf("\n");
		}
	}

	return 0;
}
