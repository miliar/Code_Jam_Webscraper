#include <bits/stdc++.h>
using namespace std;
int main()
{
	ios::sync_with_stdio(0);
	cin.tie(0);
	cout<<fixed<<setprecision(12);

	int T, no=0;
	cin>>T;
	while(T--)
	{
		int d,n;
		cin>>d>>n;
		double ans=DBL_MAX;
		for(int i=0;i<n;i++)
		{
			double pos, v;
			cin>>pos>>v;
			ans=min(ans, d/((d-pos)/v));
		}
		cout<<"Case #"<<++no<<": "<<ans<<endl;
	}
}