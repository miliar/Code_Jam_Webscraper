#include<bits/stdc++.h>
using namespace std;

pair<long long,long long> fn(long long n)
{
	if(n%2==1)
	{
		return make_pair(n/2,n/2);
	}
	else
	{
		return make_pair(n/2,n/2-1);
	}
}

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	int t;
	cin>>t;
	long long n,k;

	for(int trm=1;trm<=t;trm++)
	{

		cout<<"Case #"<<trm<<": ";
		cin>>n>>k;

		long long cpo=k;

		long long cnt=0;

		while(cpo)
		{
			cnt++;
			cpo/=2;
		}

		cnt--;

		long long gg = (1LL<<cnt);
		long long ff = k-gg;

		pair<long long,long long> ret=fn((n-ff)/gg);

		cout<<ret.first<<" "<<ret.second<<endl;


	}
}