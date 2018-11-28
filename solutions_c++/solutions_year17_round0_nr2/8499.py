#include <iostream>
#include <cstdio>
using namespace std;
typedef long long LL;

LL digit[20]={1};
int main(void)
{
	int T, ti = 0;
	scanf("%d",&T);
	for(int i=1;i<=18;i++)
		digit[i] = digit[i-1]*10;
	while(++ti<=T)
	{
		LL n;int c = 0;
		scanf("%lld",&n);
		while(n/digit[c+1]) ++c;
		printf("Case #%d: ",ti);
		if(c == 18) {puts("99999999999999999");continue;}
		else if(c == 0) {printf("%lld\n", n);continue;}	
		int p = n/digit[c], s = c;
		for(int i=c-1;i>=0;i--)
			if(p>(n%digit[i+1])/digit[i])
			{
				if(n/digit[s+1]) printf("%lld",n/digit[s+1]);
				if((n%digit[s+1])/digit[s]-1)
					printf("%lld",(n%digit[s+1])/digit[s]-1);
				for(int j=0;j<s;j++) putchar('9');
				puts("");
				break;
			}
			else if(i)
			{
				if(p<(n%digit[i+1]/digit[i]))
					s = i;
				p = (n%digit[i+1])/digit[i];
			}
			else 
				printf("%lld\n", n);
	}
	return 0;
}
