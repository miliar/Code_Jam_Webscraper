#include <bits/stdc++.h>
using namespace std;

#define PI 3.14159265359

#define mp make_pair

typedef long long ll; 

long double mx=0;

int main() {
	int t; cin>>t;
	for(int q=1; q<=t; q++)
	{
		ll n, k, r, h, sum, flag, cnt;
		cin>>n>>k;
		vector<pair<ll, ll> > v(n), v1(n);
		for(int i=0; i<n; i++)
		{
			cin>>r>>h;
			v[i]=mp(2*r*h, r*r);
			v1[i]=mp(r*r, 2*r*h);
			//cout<<v[i].first<<" "<<v[i].second<<endl;
		}
		sort(v.begin(), v.end(), greater<pair<ll, ll> >());
		sort(v1.begin(), v1.end(), greater<pair<ll, ll> >());
		for(int i=0; i<=(n-k);i++)
		{
			sum=v1[i].first+v1[i].second;
			flag=0;
			cnt=1;
			for(int j=0; j<n&&cnt<k; j++)
			{
				if(v[j].second<=v1[i].first)
				{
					if(v[j].second==v1[i].first&&v[j].first==v1[i].second&&flag==0)
						flag=1;
					else
					{
						sum+=v[j].first;
						cnt++;
					}
				}
			}
			if(sum>mx)mx=sum;
		}
		cout<<setprecision(20)<<"Case #"<<q<<": "<<mx*PI<<endl;
		mx=0;
	}
	return 0;
}