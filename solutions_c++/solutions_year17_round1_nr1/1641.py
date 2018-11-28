#include <stdio.h>
#include <string.h>
int main()
{
	freopen( "A-large.in", "r", stdin );
	freopen( "output.txt", "w", stdout );
	long long int n,t,i,j,sum,rsv,lol,r,c;
	char s[100][100];
	scanf("%lld",&t);
	for(lol=1;lol<=t;lol++)
	{
		scanf("%lld%lld",&r,&c);
		for(i=0;i<r;i++)
		scanf(" %s",&s[i][0]);
		for(i=0;i<r;i++)
		{
			for(j=0;j<c;j++)
			{
				if(s[i][j]!='?')
				{
					for(int x=i-1;x>=0;x--)
					{
						if(s[x][j]!='?')break;
						s[x][j]=s[i][j];
					}
					for(int x=i+1;x<r;x++)
					{
						if(s[x][j]!='?')break;
						s[x][j]=s[i][j];
					}
				}
			}
		}
//		printf("\n");
//		for(i=0;i<r;i++){
//		for(j=0;j<c;j++)
//		printf("%c",s[i][j]);
//		printf("\n");}
		for(i=0;i<c;i++)
		{
			
			if(s[0][i]=='?')
			{
			if(i!=0)
			for(int x=0;x<r;x++)
				s[x][i]=s[x][i-1];
			else
			{
				while(s[0][i]=='?')i++;
				for(int y=i-1;y>=0;y--)
				{
					for(int x=0;x<r;x++)
						s[x][y]=s[x][i];
				}
			}
			}
		}
		
		printf("Case #%lld: \n",lol);
		for(i=0;i<r;i++){
		for(j=0;j<c;j++)
		printf("%c",s[i][j]);
		printf("\n");}
	}
	return 0;
}
		
