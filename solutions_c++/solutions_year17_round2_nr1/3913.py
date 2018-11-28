#include<iostream>
#include<algorithm>
#include<iomanip>
using namespace std;
main()
{
	int t;cin>>t;
	for(int casen=1;casen<=t;casen++)
	{
		double d,ans=1e15;int n;
		cin>>d>>n;
		for(int i=0;i<n;i++)
		{
			double k,s;cin>>k>>s;
			ans=min(ans,d*s/(d-k));
		}
		cout<<"Case #"<<casen<<": "
			<<fixed<<setprecision(9)<<ans<<endl;
	}
}
