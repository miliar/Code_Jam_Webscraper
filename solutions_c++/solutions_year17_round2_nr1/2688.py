#include<bits/stdc++.h>
using namespace std;
int main()
{
	freopen("1codejamqn1.txt","r",stdin);
	freopen("1solution1.txt","w",stdout);
	int t;
	cin>>t;
	for(int i=1;i<=t;i++)
	{
		long long d,n;
		cin>>d>>n;
		long long dd,sp;
		double timet,time=0;
		for(int j=1;j<=n;j++)
		{
			cin>>dd>>sp;
			dd=d-dd;
			timet=dd/(sp*1.0);
			if(timet>=time)
			{
				time=timet;
			}
		}
		double ans=d/time;
		cout<<"Case #"<<i<<": ";
		printf("%.6lf",ans);
		cout<<endl;
	}
}
