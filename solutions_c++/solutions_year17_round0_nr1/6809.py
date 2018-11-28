#include<iostream>
#include<stdio.h>
#include<string.h>
#define s scanf
#define p printf
using namespace std;
char str[2005];
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("out.in","w",stdout);
	int t,k,len,m=0,i,j;
	s("%d",&t);
	while(t--)
	{
		m++;
		s(" %s",str);
		s("%d",&k);
		len=strlen(str);
		int count=0;
		for(i=0;i<len;i++)
		{
			if(str[i]=='-')
			{
				count++;
				if(i+k<=len)
				{
					for(j=i;j<i+k;j++)
				     if(str[j]=='-')
				     str[j]='+';
				     else
				     str[j]='-';
				}
				else
				{
					for(j=len-1;j>=len-k;j--)
					if(str[j]=='-')
				     str[j]='+';
				     else
				     str[j]='-';
				}
			}
		}
		int flag=0;
		for(i=0;i<len;i++)
		{
			if(str[i]=='-')
			{
				flag=1;
				break;
			}
		}
		if(flag)
		p("Case #%d: IMPOSSIBLE\n",m);
		else
		p("Case #%d: %d\n",m,count);
	}
	return 0;
}
