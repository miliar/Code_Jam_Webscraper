#include<bits/stdc++.h>
using namespace std;
#define ll long long int
bool tidynumber(ll n)
{
	vector<int> vec;
	while(n!=0)
	{
		vec.push_back(n%10);
		n=n/10;
	}
	for(int i=0;i<vec.size()-1;i++)
	{
		if(vec[i]<vec[i+1])return false;
	}
	return true;
}
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	ll t,n,i=1;
	cin>>t;
	while(t--)
	{
		cin>>n;
		while(!tidynumber(n))
		{
			n--;
		//	cout<<n<<endl;
		}
		cout<<"Case #"<<i<<": "<<n<<endl;
		i++;
	}
	return 0;
}

