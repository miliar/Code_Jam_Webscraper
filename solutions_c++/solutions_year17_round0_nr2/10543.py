#include <iostream>

using namespace std;

typedef unsigned long long ull;

bool isTidyNumber(ull x)
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
	for(int i=1;i<=t;i++)
	{
		ull n;
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
	}
	return 0;
}