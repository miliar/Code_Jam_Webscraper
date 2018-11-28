#include <bits/stdc++.h>
using namespace std;

int main()
{
	ios_base::sync_with_stdio(false);
	ifstream cin("input.txt"); ofstream cout("output.txt");
	int tc;
	cin>>tc;
	for(int tmp=1;tmp<=tc;tmp++)
	{
		long long n,k;
		cin>>n>>k;
		map<pair<long long, long long>, long long> v;
		v[make_pair((n-1)/2,(n-1) - (n-1)/2)]=1;
		cout<<"Case #"<<tmp<<": ";
		while(true)
		{
			auto it=v.end();
			it--;
			pair<long long,long long> r=it->first;
			long long mn=r.first,mx=r.second;
			//cout<<k<<" "<<mn<<" "<<mx<<" "<<it->second<<"\n";
			if(k<=it->second)
			{
				cout<<mx<<" "<<mn<<"\n";
				break;
			}
			long long t=mn-1;
			if(t>=0)
			{
				v[make_pair(t/2,t-t/2)]+=it->second;
			}
			t=mx-1;
			if(t>=0)
			{
				v[make_pair(t/2,t-t/2)]+=it->second;
			}
			k-=it->second;
			v.erase(it);
		}
	}
}
