#include <bits/stdc++.h>
using namespace std;

void query()
{
	map<double,int> prop;
	int n, k;
	cin >> n >> k;
	double u;
	cin >> u;
	for (int i=0;i<n;i++)
	{
		double p;
		cin >> p;
		prop[p]++;
	}
	while (u > 0)
	{		
		auto i=prop.begin();
		double curr=i->first;
		double num=i->second;		
		double target=1.0;
		if (curr == 1.0) break;
		if (prop.size() >1)
		{
			target=next(prop.begin())->first;			
		}	
		prop.erase(i);
		if (((target-curr)*num) >= u)
		{		
			prop[curr+u/num] += num;
			u=0;
			break;
		} else
		{		
			prop[target]+=num;
			u-=(target-curr)*num;
		}
	}
	double result=1.0;
	for (auto i: prop)
	{
		result *= pow(i.first,i.second);
	}
	cout << setprecision(15) << result << endl;
}
	
int main()
{	
	ios::sync_with_stdio(false);	
	int q;
	cin >> q;
	for (int i=0;i<q;i++)
	{
		cout << "Case #"<<i+1<<": ";
			query();
	}
}