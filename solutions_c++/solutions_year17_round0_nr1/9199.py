#include<iostream>
#include<cstring>
using namespace std;
int main()
{
	int t,m;
	cin>>t;m=1;
	while(t--)
	{
		char a[10000];
		cin>>a;
		long long int i,j,k,len,count=0;
		cin>>k;
		len=strlen(a);
		for(i=0;i<len-k+1;i++)
		{
			if(a[i]=='-')
			{
				for(j=i;j<i+k;j++)
				{
					if(a[j]=='-'){a[j]='+';}
					else if(a[j]=='+'){a[j]='-';}	
				}
			count++;
			}
		}
		//cout<<a<<endl;
		int flag=0;
		for(i=0;i<len;i++)
		{
			if(a[i]=='-')
		flag=1;
		}
		
		cout<<"Case #"<<m<<": ";
		if(flag==1)
		{
		cout<<"IMPOSSIBLE"<<endl;}
	else{
		cout<<count<<endl;	
		}		
	}
	
	
	
	
	
	
	
	
	
	
	
	return 0;
	
}
