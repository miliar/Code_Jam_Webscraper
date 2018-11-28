#include <bits/stdc++.h>

typedef unsigned long long ull;

using namespace std;

int main()
{
	ios::sync_with_stdio(false);
	int T;
	cin>>T;
	int t(T);
	while(t--)
	{
		int d,n;
		cin>>d>>n;
		double coord[n],speed[n],y(std::numeric_limits<double>::max());
		for(int i=0;i<n;i++)
		{
			cin>>coord[i]>>speed[i];
			y=min(y,d  * speed[i] / (d-coord[i]));
		}
		cout<<fixed<<setprecision(6);
		cout<<"Case #"<<T-t<<": "<<y<<'\n';
	}
}