#include <iostream>
#include <vector>
#include <map>
#include <iterator>
using namespace std;
void sole()
{
	int n,k;
	double u;
	map<double,int> M;
	cin >> n >> k >> u ;
	vector<double> v(n);
	for(int i=0;i<n;i++)
	{
		cin >> v[i];
	M[v[i]]++;
	}
	map<double,int> ::iterator i1,i2,i3;	
	while(u>0 && M.size()>1)
	{
		i1=M.begin();
		i2=i1;
		++i2;
		double req=(i2->first-i1->first)*i1->second;
		if(req > u)
		{
			double val=i1->first+u/i1->second;
			u=0;
			M.insert(make_pair(val,i1->second));
			M.erase(i1);
			break;
		}
		i2->second+=i1->second;
		u-=req;
		M.erase(i1);
	}
	if(u>0)
	{
		i1=M.begin();
		double val=min(1.0,i1->first+u/i1->second);
		int jj=i1->second;
		M.erase(i1);
		M.insert(make_pair(val,jj));
	}
	double ans=1;
	for(auto &x:M)
	{
		for(int i=0;i<x.second;i++)
		{
			ans*=x.first;
		}	
	}
	printf("%.8lf\n",ans);
	return ;
}
int main()
{
	int t;
cin >> t;
for(int i=1;i<=t;i++)
{
	printf("Case #%d: ",i);
	sole();
}
	return 0;
}