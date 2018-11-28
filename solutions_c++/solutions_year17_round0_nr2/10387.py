#include<iostream>
using namespace std;

int tidy(long long int num)
{	long long int b;
	int flag=1;
	while(num>0)
	{
		b=num%10;
		num=num/10;
		if(b<num%10)
			flag=0;
		//cout<<flag;
	}
	return flag;
}


int main()
{
	int t;
	
	cin>>t;
	
	for(int j=0;j<t;j++)
	{		
		long long int a,i=0,ans;
		cin>>a;
		while(i<=a)
		{
			if(tidy(i))
				ans=i;
			i++;		
		}
		cout<<"Case #"<<j+1<<": "<<ans<<"\n";
   	}
	
}

