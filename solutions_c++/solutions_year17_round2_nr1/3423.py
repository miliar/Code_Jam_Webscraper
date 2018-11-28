#include <bits/stdc++.h>
using namespace std;
int main()
{
	int t;
	cin>>t;
	int c=1;
	while(t--)
	{
	//	vector<pair<int,int> >v;
		double nk,nh,a,b,max=0,d;
		cin>>nk>>nh;
		for(double i=0;i<nh;i++)
		{
			cin>>a>>b;
			//v.push_back(make_pair(a,b));
			if(a==nk)
				continue;
			d = (nk-a)/b;
			if(max<d)
				max=d;
		}
	/*	for(int i=v.size()-1;i>=0;i--)
		{
			int d = nk-v[i].first;
			int v1 = v[i].second;
			double ans = d/(double)v1;
			if(max<ans)
				max = ans;
		}*/
		double ai = nk/max;
		printf("Case #%d: %.6lf\n",c,ai);
		c++;
	}
	return 0;
}
