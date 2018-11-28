#include <iostream>
#include <utility>
using namespace std;

pair<long long int, long long int> f(long long int n, long long int k);


int main()
{
	int t;
	cin>>t;

	for(int i=1;i<=t;i++)
	{
		int n, k;
		cin>>n>>k;
		pair<long long int, long long int> p;
		p = f(n, k);
		cout<<"Case #"<<i<<": ";
		cout<<p.first<<" "<<p.second<<endl;
	}
}

pair<long long int, long long int> f(long long int n, long long int k)
{
	if(k==1)
	{
		return make_pair(n/2, (n-1)/2);
	}
	else{
		if(n%2==0)
		{
			if((k-1)%2==1)
			{
				return f(n/2, k/2);
			}
			else
			{
				return f((n-1)/2, (k-1)/2);
			}
		}
		else
		{
			return f(n/2, k/2);
		}
	}
}