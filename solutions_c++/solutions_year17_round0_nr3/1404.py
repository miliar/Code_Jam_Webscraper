/*
+--+-+---+ 2
*/
#include<bits/stdc++.h>
#define ll long long
using namespace std;
int main()
{
	int n;
	cin>>n;
	for(int i=1;i<=n;i++)
	{
		set<pair<ll,ll> > s;
		unordered_map<ll,ll> um;
		cout<<"Case #"<<i<<": ";
		ll n,z;
		cin>>n>>z;
		s.insert(make_pair(n,1));
		um[n]=1;
		while(1)
		{
			pair<ll,ll> max1=*s.rbegin();
			z-=max1.second;
			s.erase(make_pair(max1.first,max1.second));
			if(z<=0)
			{
				if(max1.first%2)
					cout<<max1.first/2<<" "<<max1.first/2<<"\n";
				else
					cout<<max1.first/2<<" "<<max1.first/2-1<<"\n";	
				break;
			}
			if(max1.first%2)
			{
				set<pair<ll,ll> >::iterator it=s.find(make_pair(max1.first/2,um[max1.first/2]));
				if(it!=s.end())
				{
					ll temp=it->second+max1.second*2;
					um[max1.first/2]=temp;
					ll temp1=it->first;
					s.erase(it);
					s.insert(make_pair(temp1,temp));
					//it->second=temp;
				}
				else
				{
					ll temp=max1.second*2;
					um[max1.first/2]=temp;
					s.insert(make_pair(max1.first/2,temp));
				}
			}
			else
			{
				set<pair<ll,ll> >::iterator it=s.find(make_pair(max1.first/2,um[max1.first/2]));
				if(it!=s.end())
				{
					ll temp=it->second+max1.second;
					um[max1.first/2]=temp;
					ll temp1=it->first;
					s.erase(it);
					s.insert(make_pair(temp1,temp));
					//it->second=temp;
				}
				else
				{
					ll temp=max1.second;
					um[max1.first/2]=temp;
					s.insert(make_pair(max1.first/2,temp));
				}
				it=s.find(make_pair(max1.first/2-1,um[max1.first/2-1]));
				if(it!=s.end())
				{
					ll temp=it->second+max1.second;
					um[max1.first/2-1]=temp;
					ll temp1=it->first;
					s.erase(it);
					s.insert(make_pair(temp1,temp));
					//it->second=temp;
				}
				else
				{
					ll temp=max1.second;
					um[max1.first/2-1]=temp;
					s.insert(make_pair(max1.first/2-1,temp));
				}
			}

		}
	}
	return 0;
}