#include <iostream>
#include <string.h>
using namespace std;

int main() {
	int t;
	scanf("%d",&t);
	int jj;
	for(jj=0;jj<t;jj++)
	{
		char a[10001];
		scanf("%s",a);
		int len = strlen(a);
		int k,j,cnt=0,i = 0;
		scanf("%d",&k);
		for(i=0;i<len;i++)
		{
			if(a[i]=='-' && i <=len-k)
			{
				for(j=i;j<k+i;j++)
			{
				if(a[j]=='+')
				a[j] = '-';
				else
				a[j] = '+';
				
			}	
			cnt++;
			}
			
		}
		int com = 1;
		for(i=0;i<len;i++)
		{
			if(a[i]=='-')
			{
				printf("Case #%d: IMPOSSIBLE\n",jj+1);
				com = 0;
				break;
			}
		}
		if(com)
		printf("Case #%d: %d\n",jj+1,cnt);
	}
	// your code goes here
	return 0;
}