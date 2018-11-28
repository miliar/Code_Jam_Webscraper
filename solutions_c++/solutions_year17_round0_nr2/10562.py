#include<iostream>
using namespace std;
bool check(unsigned long long n)
{
	unsigned long long bf = 10;
	while(n > 0)
	{
		if(n % 10 > bf)
		{
			return false;
			break;
		}
		else
		{
			bf = n % 10;
			n /= 10;
		}
	}
	return true;
}
main()
{
	int n;
	unsigned long long x;
	cin>>n;
	for(int i = 1; i <= n; i++)
	{
		cin>>x;
		for(unsigned long long j = x; j > 0; j--)
		{
			if(check(j))
			{
				cout<<"Case #"<<i<<": "<<j<<"\n";
				break;
			}
		}
		
	}
}
