#include<stdio.h>
#include<iostream>
#include<stdlib.h>
#include<algorithm>
#include<vector>
#include<list>
#include<math.h>
#include<utility>
#include<queue>
#include<set>
#include<functional>
#include<fstream>
#include<string.h>
#define fori(n) for(int i=0;i<n;i++)
#define forj(n) for(int j=0;j<n;j++)
#define foo(a,b,c) for(int i=a;i<b;i+=c)
#define fo(a,b) for(int i=a;i<b;i++)
#define get(x) scanf("%d",&x)
#define getll(x) scanf("%lld",&x)
#define ll long long 
#define cin fin
#define cout fout
using namespace std;

int main()
{
	ifstream fin;
	ofstream fout;
	fin.open("inputal.in", ios::in);
	fout.open("outputal.txt", ios::out);
	int tst;
	cin>>tst;
	
	for(int t=1;t<=tst;t++)
	{
		int k;
		char str[1005];
		
		
		cin>>str;
		cin>>k;
		
		int l=strlen(str);
		
		int count=0;
	//	while(!happy(str,l,k))
	//	{
			for(int i=0;i<l;i++)
		   {
			  if(str[i]=='-' && i+k<=l)
			  {
			  	count++;
			  	for(int j=i;j<i+k;j++)
			  	{
			  		
			  		
			  			if(str[j]=='-')
			  		    str[j]='+';
			  		    else
			  		    str[j]='-';
					
			  	
				}
			//	cout<<str<<endl;
			  }
			  
		   }
		   int flag=0;
		   for(int i=0;i<l;i++)
		   {
		   	if(str[i]=='-')
		   	{
		   		flag=1;
		   		break;
			   }
		   	
		   }
		   if(flag)
		   cout<<"Case #"<<t<<": "<<"IMPOSSIBLE"<<endl;
		   else
		   cout<<"Case #"<<t<<": "<<count<<endl;
	//	}
		
	}
	
	
	return 0;
}
