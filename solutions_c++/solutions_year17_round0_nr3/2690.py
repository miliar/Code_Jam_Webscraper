#include <bits/stdc++.h>
using namespace std;
#define ll long long int
struct res{
	ll max;
	ll min;
};

struct res sol(ll n,ll k)
{
	struct res r;
	if(k==1)
	{
		r.max = n/2;
		r.min = (n-1)/2;
		return r;
	}
	else
	{
		if(k%2==0)
			return sol(n/2,k/2);		
		else
		return sol((n-1)/2,k/2);
	}
	
}

int main()
{
	int test;
	cin>>test;
	int count =0;
	ll n,k;
	while(test--)
	{
		count++;
		
	cin>>n>>k;
	cout<<"Case #"<<count<<": "; 
	struct res r= sol(n,k);
	cout<<r.max<<" "<<r.min<<endl;
	}	
}


