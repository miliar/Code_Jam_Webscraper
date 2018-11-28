#include <cstdio>
#include <cstring>

int t,n,l;
char cake[1000][1000];

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	scanf("%d",&t);
	for(int c=0;c<t;++c)
	{
		scanf("%d%d",&n,&l);
		bool flag=true;
		for(int i=0;i<n;++i)
		{
			scanf("%s",cake[i]);
			char lastc='?';
			for(int j=0;j<l;++j)
			{
				char& c=cake[i][j];
				if(c=='?')
				{
					c=lastc;
				}
				else
				{
					if(lastc=='?')
						for(int k=0;k<j;++k)
							cake[i][k]=c;
					lastc=c;
				}
			}
			if(flag&&lastc!='?')
			{
				flag=false;
				for(int k=0;k<i;++k)
					strcpy(cake[k],cake[i]);
			}
			else if(!flag&&lastc=='?')
			{
				strcpy(cake[i],cake[i-1]);
			}
		}
		printf("Case #%d:\n",c+1);
		for(int i=0;i<n;++i)
			printf("%s\n",cake[i]);
	}
	return 0;
}



