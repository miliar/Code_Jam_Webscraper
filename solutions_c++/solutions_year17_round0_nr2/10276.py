#include <iostream>

using namespace std;

bool isTidyNumber(long long x)
{
	int t=x%10;
	x=x/10;
	while(x)
	{
		if(t<x%10)
			return false;
		t=x%10;
		x/=10;	
	}
	return true;
}

int main()
{
	int t;
	cin>>t;
	int i=1;
	while(t--)
	{
		long long n;
		cin>>n;
		while(n)
		{
			if(isTidyNumber(n))
			{
				cout<<"Case #"<<i<<": "<<n<<endl;
				break;
			}
			n--;
		}
		i++;	
	}
	return 0;
}