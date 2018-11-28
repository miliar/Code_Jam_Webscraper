#include<iostream>
#include<algorithm>
#include<iomanip>
using namespace std;
main()
{
	int t;cin>>t;
	for(int count=1;count<=t;count++)
	{
		int n,k;cin>>n>>k;
		double u;cin>>u;
		double p[50];
		for(int i=0;i<n;i++)cin>>p[i];
		sort(p,p+n);
		double f=0.0,l=1.0;
		double ans=0.0;
		for(int rep=0;rep<100;rep++)
		{
			double m=(f+l)/2;
			bool flag=true;
			double nowu=u;
			double nowans=1.0;
			for(int i=0;i<n;i++)
			{
				double nowp=p[i];
				if(nowp<m)
				{
					if(nowu<m-nowp)
					{
						flag=false;
						break;
					}
					else
					{
						nowu-=m-nowp;
						nowp=m;
					}
				}
				nowans*=nowp;
			}
			if(flag)ans=max(ans,nowans);
			(flag?f:l)=m;
		}
		cout<<"Case #"<<count<<": "<<fixed<<setprecision(9)<<ans<<endl;
	}
}
