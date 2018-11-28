#include <bits/stdc++.h>

using namespace std;

typedef long long int ll;

int main()
{
	int t;
	cin >> t;
	for(int i=1;i<=t;i++)
	{
		cout << "Case #" << i << ": ";
		int n,k;
		cin >> n >> k;
		vector<pair<int,int> > a,b,l,r;
		a.push_back(make_pair(0,n+1));
		int x,y,z;
		pair<int,int> p;
		while(k--)
		{
			for(int j=0;j<a.size();j++)
			{	
				if((a[j].second - a[j].first)>1)
				{
					x = a[j].first + (a[j].second - a[j].first)/2;
					y = x - a[j].first - 1;
					z = a[j].second - x - 1;
					l.push_back(make_pair(min(y,z),max(y,z)));
				}
				else
					l.push_back(make_pair(0,0));	
				
			}
			int idx=0;
			p = l[0];
			
			for(int j=1;j<l.size();j++)
			{
				if(p < l[j])
				{
					p = l[j];
					idx = j;
				}

			}
			
			for(int j=0;j<a.size();j++)
			{
				if(j==idx)
				{
					x = a[j].first + (a[j].second - a[j].first)/2;
					b.push_back(make_pair(a[j].first,x));
					b.push_back(make_pair(x,a[j].second));
				}
				else
					b.push_back(a[j]);
			}
			l.clear();
			a=b;
			// cout << b.size() << endl;
			b.clear();
		}
		cout << p.second << " " << p.first <<  endl;
	}
}