#include <iostream>
#include <stdio.h>
#include <string.h>
using namespace std;

int main() 
{
	int t,i,j,k,len,count,x;
	char s[1001];
	scanf("%d",&t);
	for(j=1;j<=t;j++)
	{
		cout<<"Case #"<<j<<": ";
		scanf("%s%d",s,&k);
		len=strlen(s);
		count=0;
		for(i=0;i<=len-k;i++)
		{
			if(s[i]=='-')
			{	//cout<<i;
				count++;
				for(x=i;x<i+k;x++)
				{
					if(s[x]=='+')
						s[x]='-';
					else
						s[x]='+';
				}
			}
		}
		for(i=0;i<len;i++)
			if(s[i]=='-')
				count=-1;
		if(count==-1)
			printf("IMPOSSIBLE\n");
		else
			printf("%d\n",count);
	}
	return 0;
}
