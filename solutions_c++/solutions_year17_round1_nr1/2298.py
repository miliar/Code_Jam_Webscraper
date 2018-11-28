#include <iostream>
#include <string>
using namespace std;
int t;
// int ca=1;
int main()
{
	scanf("%d",&t);
	int r,c;
	char m[30][30];
	char e[30];
	char ee[30];
	for(int ca=1;ca<=t;ca++)
	{
		// cout<<t<<endl;
		scanf("%d %d",&r,&c);
		getchar();
		memset(e,'?',sizeof(e));
		for(int i=0;i<r;i++)
		{
			for(int j=0;j<c;j++)
			{
				scanf("%c",&m[i][j]);
				// cout<<m[i][j];
				if(m[i][j]!='?')
					e[i]=m[i][j];
			}

			getchar();

		}
		for(int i=0;i<r;i++)
			for(int j=c-1;j>=0;j--)
			{
				if(m[i][j]=='?')
					m[i][j]=e[i];
				else
					e[i]=m[i][j];
			}
		for(int j=0;j<c;j++)
		{
			for(int i=0;i<r;i++)
			{
				if(m[i][j]!='?')
					ee[j]=m[i][j];
			}
		}
		for(int j=0;j<c;j++)
		{
			for(int i=r-1;i>=0;i--)
			{
				if(m[i][j]=='?')
					m[i][j]=ee[j];
				else
					ee[j]=m[i][j];
			}
		}
		printf("Case #%d:\n",ca);
		for(int i=0;i<r;i++)
		{
			for(int j=0;j<c;j++)
			{
				printf("%c",m[i][j]);
			}
			printf("\n");
		}

	}
	return 0;
}