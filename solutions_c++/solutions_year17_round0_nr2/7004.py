#include <iostream>
#include<stdio.h>
#include<cstring>
using namespace std;

int main() 
{
	
	int t;
	char a[10000];
	scanf("%d",&t);
	for(int i=0;i<t;i++)
	{
		printf("Case #%d: ",i+1);
		scanf("%s",a);
		int n=strlen(a);
		int j=1;
		while(j<n)
		{
			while(a[j]>=a[j-1]&&j<n)
			j++;
			char c=a[j-1];
			int x=j-1;
			while(a[x]==c)
			x--;
			a[x+1]=c-1;
			for(int k=x+2;k<n;k++)
			a[k]='9';
			break;
		}
		int b=0;
		while(a[b]=='0')
		b++;
		while(b<n)
		{
		printf("%c",a[b]);
		b++;
		}
		printf("\n");
	}
	return 0;
}