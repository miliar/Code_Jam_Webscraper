#include<iostream>
using namespace std;

int main()
{   freopen("input.in","r",stdin);
	freopen("output.txt","w",stdout);
     
	int t;
	cin>>t;
	
	for(int j=1 ; j<=t ; j++)
	{
	
	int n,rem,temp,n1;
	cin>>n;
	
	for(int i=n ; i>0 ; i--)
	{
		
	if(i<10)
	{
	cout<<"Case #"<<j<<": "<<i<<endl;
	break;
	}
	
	
	else if(i%10==0 && ((i/10)%10)==0)
	{
		cout<<"Case #"<<j<<": "<<i-1<<endl;
		break;
	}
	
		
	else
	{
	temp=i;
	int flag=0;
		while(temp>10)
			{
			n1=temp/10;
			rem=temp%10;
		
		
			if(rem<(n1%10) || (n1%10==0))
			{
			flag=1;
			break;
		    }
		    
			temp=temp/10;    
			}
	
	if(flag==0)
	{
		cout<<"Case #"<<j<<": "<<i<<endl;
		break;
	}
	
	}
		
		
	}	
		
		
	
    }
	
}
