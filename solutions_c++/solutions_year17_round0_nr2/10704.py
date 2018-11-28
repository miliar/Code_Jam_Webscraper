#include <iostream>
using namespace std;

bool isTidy(unsigned long long x)
{
	bool Tidy = true;
	unsigned long long div = 10, r = -1, oldR = -1;
	while(x!=0)
	{
		r = x%div;
		x /= 10;
		if(r > oldR && oldR!=-1)
		{
			Tidy = false;
			break;
		}
		oldR = r;
	}
	return Tidy;
}

int main() {
	// your code goes here
	int T;
	cin>>T;
	for(int i=1; i<=T; i++)
	{
		unsigned long long n;
		cin >>n;
		for(unsigned long long j=n; j>=1; j--)
		{
			if(isTidy(j))
			{
				cout<<"Case #"<<i<<": "<<j<<endl;
				break;
			}
		}
	}
	return 0;
}