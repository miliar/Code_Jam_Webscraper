#include<iostream>
using namespace std;

int checkN(long long n)
{
	int remainder, last_remainder;
	last_remainder = n%10;
	//cout<<"N = "<<n<<" and Last remainder : "<<last_remainder<<endl;
	n=n/10;
	while(n>0)
	{
		remainder = n%10;
		//cout<<"N = "<<n<<" and remainder : "<<remainder<<endl;
		if(remainder <= last_remainder)
		{
			last_remainder = remainder;
		}
		
		else
		{
			return 0;
		}
		n=n/10;
	}
	
	return 1;
}



int main()
{
	int t;
	cin>>t;
	
	for(int j=1;j<=t;j++)
	{
		long long n;
		cin>>n;
		
		int found=0;
		
		for(long long i=n;i>=0;i--)
		{
			if(checkN(i))
			{
				cout<<"Case #"<<j<<": "<<i<<endl;
				found=1;
				break;
			}
			
		}
	}
	
	return 0;
}
