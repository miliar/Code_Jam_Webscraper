#include <iostream>
#include<stdio.h>
#include<cstring>
using namespace std;

int main() 
{
	int t,k;
	char a[1000];
	scanf("%d",&t);
	for(int i=0;i<t;i++)
	{
		scanf("%s",a);
		scanf("%d",&k);
		int l=strlen(a);
		int count=0;
		int j=0;
		int flag2=0;
		while(j<l)
		{
			while(a[j]=='+'&&j<l)
			j++;
			int flag=0;
			for(int x=j;j<l;j++)
			{
				if(a[x]=='-')
				{
				flag=1;
				break;
				}
			}
			if(flag==0)
			break;
			if(l-j<k)
			{
				flag2=1;
				break;
			}
			else
			{
			count++;
			for(int x=j;x<j+k;x++)
			{
				if(a[x]=='+')
				a[x]='-';
				else
				a[x]='+';
			}
			}
		}
		if(flag2==1)
		printf("Case #%d: IMPOSSIBLE\n",i+1);
		else
		printf("Case #%d: %d\n",i+1,count);
	}
	return 0;
}