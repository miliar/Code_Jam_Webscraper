#include <iostream>
#include <cstdio>
using namespace std;

char str[1005];
int main(void)
{
	int T, ti = 0;
	scanf("%d",&T);
	while(++ti<=T)
	{
		int c = 0, i, k;
		scanf("%s%d",str,&k);
		for(i=0;str[i+k-1];i++)
			if(str[i]=='-')
			{
				c+=1;
				for(int j=i;j<i+k;j++)
					str[j]=(str[j]=='-'?'+':'-');
			}
		for(;str[i];i++)
			if(str[i]=='-') {c = -1; break;}
		printf("Case #%d: ",ti);
        if(c == -1) puts("IMPOSSIBLE");
		else printf("%d\n",c);
	}
	return 0;
}
