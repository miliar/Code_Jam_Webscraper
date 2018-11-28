#include<bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef map<ll,vector<pair<ll,ll> > > MyMap;
typedef vector<pair<ll,ll> > MyVector;
typedef pair<ll,ll> pll;

MyVector & getMoves(ll n,MyMap & map1)
{
	if(n==0)
	{
		MyVector &newVector = map1[n];

		return newVector;
	}


	MyMap::iterator it1 = map1.find(n);

	if(it1!=map1.end())
		return map1[n];

	if(n%2==0)
	{
		MyVector &x1 = getMoves(n/2 - 1,map1);
		MyVector &x2 = getMoves(n/2,map1);

		MyVector &newVector = map1[n];

		newVector.push_back(pll(n,1));

		int i = 0,j = 0;

		while(i<x1.size() && j<x2.size())
		{
			if(x1[i].first > x2[j].first)
			{
				newVector.push_back(x1[i]);
				i++;
			}
			else if(x1[i].first == x2[j].first)
			{
				newVector.push_back(pll(x1[i].first,x1[i].second+x2[j].second));
				i++;
				j++;
			}
			else
			{
				newVector.push_back(x2[j]);
				j++;
			}
		}

		while(i<x1.size())
		{
			newVector.push_back(x1[i]);
			i++;
		}

		while(j<x2.size())
		{
			newVector.push_back(x2[j]);
			j++;
		}

		return newVector;
	}
	else
	{
		MyVector &x = getMoves(n/2,map1);

		MyVector &newVector = map1[n];
		newVector.push_back(pll(n,1));

		for(int i=0;i<x.size();i++)
		{
			newVector.push_back(pll(x[i].first,x[i].second*2));
		}

		return newVector;
	}

	
}

int main()
{
	int t;
	cin>>t;
	for(int gh=1;gh<=t;gh++)
	{
		ll n,k;
		cin>>n>>k;

		MyMap map1;

		MyVector &vec = getMoves(n,map1);

		ll answer;

		for(int i=0;i<vec.size();i++)
		{
			if(k<=vec[i].second)
			{
				answer = vec[i].first;
				break;
			}
			else
			{
				k-=vec[i].second;
			}
		}

		if(answer%2==0)
		{
			cout<<"Case #"<<gh<<": "<<answer/2<<" "<<answer/2 - 1<<endl;
		}
		else
		{
			cout<<"Case #"<<gh<<": "<<answer/2<<" "<<answer/2<<endl;
		}
	}
}