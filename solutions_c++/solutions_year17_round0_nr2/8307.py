#include<stdio.h>
int main()
{
	bool b, first;
	char s[20];
	int n, i, j, k, c;
	scanf("%d",&n);
	for(i=0;i<n;i++)
	{
		printf("Case #%d: ",i+1);
		b=true;
		scanf("%s",s);
		if(s[1]==0)
			printf("%s\n",s);
		else if(s[1]=='0')
		{
			if(s[0]>'1')
				printf("%c",s[0]-1);
			for(j=1;s[j]!=0;j++)
				printf("9");
			printf("\n");
		}
		else
		{
			c=0;
			for(j=0;s[j+1]!=0;j++)
			{
				if(b)
				{
					if(s[j]>s[j+1])
					{
						if(j-c!=0 || s[j]!='1')
							printf("%c",s[j]-1);
						for(k=0;k<c;k++)
							printf("9");
						c=0;
						b=false;
					}
					else if(s[j]==s[j+1])
						c++;
					else
					{
						for(k=0;k<=c;k++)
							printf("%c",s[j]);
						c=0;
					}
				}
				else
				{
					printf("9");
				}
			}
			if(b)
			{
				for(k=0;k<c+1;k++)
					printf("%c",s[j]);
				printf("\n");
			}
			else
			{
				for(j=0;j<c+1;j++)
					printf("9");
				printf("\n");
			}
		}
	}
}
