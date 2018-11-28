#include<algorithm>
#include<stack>
#include<queue>
#include<list>
#include<string.h>
#include<deque>
#include<set>
#include<map>
#include<iterator>
#include<ctime>
#include<iterator>
#include<numeric>
#include<fstream>
#include<iostream>
#include<stdio.h>
#include<stdlib.h>
#include<cmath>
#include<vector>

using namespace std;
long long limit=9223372036854775807;
main()
{
	freopen("input.in","r",stdin);
	freopen("output.txt","w",stdout); 
	char a[10000],b[10000];
	int t,s=1;
	long long int num,num1;
	long long int i, sum,len,j,k,x,y,m,len1,l;
	scanf("%d",&t);
	
	while(t>0)
	{
	num=0;
	num1=0;
	sum=0;
	x=0;
	y=0;
	
	cin>>a;
	
	len=strlen(a);
	for(int i=0;i<len;i++)
	{
		sum=((int)(a[i]))-48;
		num=(num*10)+sum;
	}
	num1=num;
	sum=0;
	int count=0;
	while(count<len1)
	{
		x=0;
		count++;
		num1=num;
	for(int i=0;i<len-1;i++)
	{
		j=((int)(a[i]))-48;
	

		k=((int)(a[i+1]))-48;
		if((j-k)>0)
		{
				for(int m=i+1;m<=len-1;m++)
				{
					sum=((int)(a[m]))-48;
					x=(x*10)+sum;
				}
				x=x+1;
		
		num1=num1-x;
		
		if(num1 != num)
		{
			num=num1;
		for(i=0;num1>0;i++)
		{
			b[i]=((char)(num1%10))+48;
			num1=num1/10;
		
		}
		b[i]='\0';
		len=strlen(b);
		
		int z=0;
		for(int i=len-1;i>=0;i--)
		{
			a[z]=b[i];
			z++;
		}
		a[len]='\0';
		len=strlen(a);
		
	}
		break;
		}
	}
	
}
	printf("\ncase #%d: %lld\n", s,num);
	s++;
	t--;
}

}
