#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <cstdlib>
#include <set>
#include <algorithm>
using namespace std;

int T;
int R,C,O=1;
char s[30][30];

int main()
{
	freopen("1.in","r",stdin);
	freopen("1.out","w",stdout);
    scanf("%d",&T);
	int i,j,p;
	char num;
	bool o;
	while (T--)
	{
		printf("Case #%d:\n",O);
		++O;
		scanf("%d%d",&R,&C);
		memset(s,0,sizeof(s));
		for (i=1;i<=R;i++)	scanf("%s",s[i]+1);
		for	(i=1;i<=R;i++)
		{
			o=false;
			for (j=1;j<=C;j++)
			{
				if (s[i][j]!='?')
				{
					o=true;
					break;
				}
			}
			if (o)
			{
				j=1;	p=1;
				while (1)
				{
					for (;j<=C;j++)
						if (s[i][j]!='?')
						{
							num=s[i][j];
							break;
						}
					while (s[i][p]=='?' || s[i][p]==num)
					{
						s[i][p]=num;
						++p;
						if (p>C)	break;
					}
					++j;
					if (j>C)	break;
				}
			}
		}
		for (i=1;i<=R;i++)
		{
			if (s[i][1]=='?')
			{
				j=i;
				while (j<=R && s[j][1]=='?')	++j;
				if (j>R)
				{
					j=i;
					while (j>=1 && s[j][1]=='?')	--j;
				}
				for (p=1;p<=C;p++)	s[i][p]=s[j][p];
			}
		}
		for (i=1;i<=R;i++)
		{
			for (j=1;j<=C;j++)
				printf("%c",s[i][j]);
			printf("\n");
		}
	}
	return 0;
}
