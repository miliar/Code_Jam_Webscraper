#include <iostream>
#include<bits/stdc++.h>

using namespace std;


long long int fun2(long long int x,long long int y,long long int count)
{
	//	cerr<<x<<"__"<<y<<"__"<<count<<endl;
		long long int z= x;
		long long int new_n=0;
		long long int c=1;
		while(z/10>0)
		{
			
			new_n+= 9*c;
			c*=10;
			z=z/10;
		}
		
		new_n+=((z%10) -1)*c;
	return new_n;
}
	
long long int fun(long long int x)
{
	int temp;
	long long int count =1;
	long long int y=0;
	int flag=0;
	while(1)
	{
		if(flag==0)
		{
				temp = x%10;
			y+=count *temp;
			}
		else temp=x%10-1;
		
		x=x/10;
		
		//cerr<<"----"<<y<<endl;
		count*=10;
		
		if(x>0)
		{
			if(temp>=x%10 )
			{
				flag=0;
				continue;
				}	
			else 
			{
				flag=1;
				y=fun2(y+count*(x%10),y,count);
				
				//cerr<<x<<"___"<<y<<endl;
			}
		}
		else 
		break;		
	}
//	cerr<<"___"<<y<<endl;
	long long int c_y=1;
	long long int temp1=y;
	while(temp1>0)
	{
		temp1=temp1/10;
		c_y*=10;
	}
	
//	cerr<<c_y<<(x/10)*c_y +y;
	return (x/10)*c_y +y;		
}
	

int main()
{
	
	
	freopen("tidy.in","r",stdin);
	freopen("tidy.out","w",stdout);
	
	
	int t;
	cin>>t;

	for(int i=1;i<=t;i++)
	{
		long long int n;
		cin>>n;
		if(n/10==0)
			cout<<"Case #"<<i<<": "<<n<<endl;
		else
		{
			long long int ans = fun(n);
			cout<<"Case #"<<i<<": "<<ans<<endl;
		}
			
	}
	
	return 0;
	
}

