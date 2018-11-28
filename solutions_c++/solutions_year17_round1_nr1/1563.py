#include<bits/stdc++.h>
using namespace std;

char str[30][30];
int t,n,m;
int a[30][30];

int main()
{
	int i,j,k;
	scanf("%d",&t);
	for(int p=1;p<=t;p++)
	{
		scanf("%d%d",&n,&m);
		for(i=0;i<n;i++)
			scanf("%s",&str[i]);
		for(i=0;i<n;i++)
		{
			for(j=0;j<m;j++)
			{
				if(str[i][j]!='?')
				{
					k=j-1;
					while(k>=0&&str[i][k]=='?')
					{
						str[i][k]=str[i][j];
						k--;
					}
					k=j+1;
					while(k<m&&str[i][k]=='?')
					{
						str[i][k]=str[i][j];
						k++;
					}
				}
			}
		}
		
		for(i=0;i<n;i++)
		{
			for(j=0;j<m;j++)
			{
				if(str[i][j]!='?')
				{
					k=i-1;
					while(k>=0&&str[k][j]=='?')
					{
						str[k][j]=str[i][j];
						k--;
					}
					k=i+1;
					while(k<n&&str[k][j]=='?')
					{
						str[k][j]=str[i][j];
						k++;
					}
				}
			}
		}
		printf("Case #%d:\n",p);
		for(i=0;i<n;i++)
			printf("%s\n",str[i]);
	}
	return 0;
}
