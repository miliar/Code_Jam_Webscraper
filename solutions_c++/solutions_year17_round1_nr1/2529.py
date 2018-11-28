#include <stdio.h>
#include <string.h>

char cake[30][30];

int main()
{
	int t,n,m,x=0,i,j,k,l;
	char c;
	scanf("%d",&t);
	while(t--)
	{
		scanf("%d%d",&n,&m);
		for(i=0;i<n;i++) scanf("%s",&cake[i]);
		for(i=0;i<n;i++)
		{
			for(l=0,j=0;j<m;j++)
			{
				if(cake[i][j]!='?')
				{
					for(c=cake[i][j],k=l;k<j;k++) cake[i][k]=c;
					l=j+1;
				}
			}
			if(l!=0) for(k=l;k<m;k++) cake[i][k]=c;
		}
		for(j=0;j<m;j++)
		{
			for(l=0,i=0;i<n;i++)
			{
				if(cake[i][j]!='?')
				{
					for(c=cake[i][j],k=l;k<i;k++) cake[k][j]=c;
					l=i+1;
				}
			}
			if(l!=0) for(k=l;k<n;k++) cake[k][j]=c;
		}
		printf("Case #%d:\n",++x);
		for(i=0;i<n;i++) printf("%s\n",cake[i]);
	}
}
