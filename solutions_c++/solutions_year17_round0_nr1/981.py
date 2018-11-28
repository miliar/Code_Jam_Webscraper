#include <cstdio>
#include <cstring>

int k,n,l;
char pc[2000];

inline char flip(char c)
{
	return c=='+'?'-':'+';
}
	
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	scanf("%d",&k);
	for(int c=0;c<k;++c)
	{
		int steps=0;
		scanf("%s %d", pc, &n);
		l=strlen(pc);
		for(int i=0;i<l-n+1;++i)
		{
			if(pc[i]=='+')
				continue;
			++steps;
			for(int j=i;j<i+n;++j)
			{
				pc[j]=flip(pc[j]);
			}
			//printf("%s\n",pc);
		}
		bool succeeded=true;
		for(int j=l-n;j<l;++j)
		{
			if(pc[j]=='-')
			{
				succeeded=false;
				break;
			}
		}
		printf("Case #%d: ",c+1);
		succeeded?printf("%d\n", steps):printf("IMPOSSIBLE\n");
	}
	return 0;
}

