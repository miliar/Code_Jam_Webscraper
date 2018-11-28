#include<bits/stdc++.h>
using namespace std;

int main()
{
	int t;
	cin>>t;
	for(int gh=1;gh<=t;gh++)
	{
		int d,n;
		cin>>d>>n;

		vector<long double> v,pos;
		for(int i=0;i<n;i++)
		{
			int speed,pos1;
			cin>>pos1>>speed;

			v.push_back(speed);
			pos.push_back(pos1);
		}

		long double min1 = (v[0]*d)/(d - pos[0]);
		for(int i=1;i<v.size();i++)
		{
			long double temp = (v[i]*d)/(d - pos[i]);
			min1 = min(min1,temp);
		} 

		printf("Case #%d: %.9Lf\n",gh,min1);
	}
	return 0;
}