#include <bits/stdc++.h>
using namespace std;

int check(int n)
{
	int t=0;
	int j=INT_MAX;
	while(n>0)
	{	
		t = j;
		j = n%10;
		//cout<<j<<' '<<t<<'\n';
		n = n/10;
		if(t<j)
		{
			return 0;
		}
	}
	return 1;
}

int main()
{
	int n;
	cin>>n;
	int k=1;
	while(n--)
	{
		int t;
		cin>>t;
		int i=t;
		while(i>=1)
		{
			if(check(i))
			{
				cout<<"Case #"<<k<<": "<<i<<'\n';
				break;
			}
			else
			{
				--i;
			}
		}
		++k;
	}
	return 0;
}