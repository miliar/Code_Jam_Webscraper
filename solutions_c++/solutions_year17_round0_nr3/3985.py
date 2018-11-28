#include <iostream>
using namespace std;
int main()
{
	int t;
	cin>>t;
	for (int i = 1; i <= t; ++i)
	{
		int n,k;
		cin>>n>>k;
		k--;
		int p=1,q=k;
		int x,y;
		if(n%2==0)
		{
			x=n/2;
			y=x-1;
		}
		else
			x=y=n/2;

		

		while(q>=p)
		{
			q-=p;
			p*=2;
			if(x%2==0)
			{
				x=x/2;
				y=x-1;
			}
			else
				x=y=x/2;
			
		}
		cout<<"Case #"<<i<<": ";
		int z=(n-k+q)%p;
		if(z==0)
			z=p;
		if(z>q)
			cout<<x<<" "<<y<<endl;
		else
		{
			if(x==y)
				cout<<x<<" "<<(y-1)<<endl;
			else
				cout<<(x-1)<<" "<<y<<endl;
		}
	}
}
