#include <stdio.h>
#include <stdlib.h>
#include <string.h>
using namespace std;

int main()
{
	int t;
	scanf("%d",&t);
	for(int i=0;i<t;i++)
	{
		char s[1001];
		int k;
		scanf("%s",s);
		scanf("%d",&k);
		int len=strlen(s);
		int num=0;
		for(int j=0;j<=(len-k);j++)
		{
			if(s[j]=='-')
			{
				num++;
				for(int l=0;l<k;l++)
				{
					if(s[j+l]=='-')
						s[j+l]='+';
					else
						s[j+l]='-';
				}
			}
		}
		bool possible= true;
		for(int j=(len-k);j<len;j++)
		{
			if(s[j]=='-')
			{
				possible=false;
				break;
			}

		}
		printf("Case #%d: ",i+1);
		if(possible)
			printf("%d\n",num);
		else
			printf("IMPOSSIBLE\n");		
	}
}
