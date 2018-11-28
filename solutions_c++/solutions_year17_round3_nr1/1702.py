#include <iostream>
#include <iomanip>
#include <cmath>
#include <utility>
#include <algorithm>
#include <vector>
#define PI 3.14159265359
using namespace std;
vector<pair<long double,long double> > v,tmp;
int main()
{
	long long T,N,K,i,j,x;
	long double Ri,Hi,tot,ans;
	cin>>T;
	for(x=1;x<=T;x++)
	{
		v.clear();
		cin>>N>>K;
		for(i=0;i<N;i++)
		{
			cin>>Ri>>Hi;
			v.push_back(pair<long double,long double>(2*Hi*Ri,Ri));
		}
		ans=0;
		for(i=0;i<N;i++)
		{
			tot=v[i].second*v[i].second+v[i].first;
			tmp.clear();
			for(j=0;j<N;j++)
			{
				if(i!=j)
				{
					if(v[j].second<=v[i].second)
					{
						tmp.push_back(v[j]);
					}
				}
			}
			if(tmp.size()>0)
			sort(tmp.begin(),tmp.end());
			if(tmp.size()>=K-1)
			{
				for(j=(long long)tmp.size()-1;j>=(long long)tmp.size()-K+1;j--)
				{
					tot+=tmp[j].first;
				}
				if(tot>ans)
					ans=tot;
			}
		}
		cout<<fixed<<setprecision(10)<<"Case #"<<x<<": "<<ans*PI<<"\n";
		
	}
	return 0;
}
