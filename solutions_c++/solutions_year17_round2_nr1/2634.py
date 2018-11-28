#include<bits/stdc++.h>
using namespace std;


int main()
{
	freopen("testcase.txt","r",stdin);
	freopen("output.txt","w",stdout);
	
	long long int T,N,D;
	double ans,D1,S1;
	
	cin>>T;
	for(long long int t=1;t<=T;t++)
	{
		long double mint=0,time1;
		cin>>D>>N;
		
		for(int i=0;i<N;i++)
		{
			cin>>D1>>S1;
			time1=((D-D1)*1.0)/(S1*1.0);
			mint=max(time1,mint);
		}
		
		ans=(D*1.0)/mint;
		printf("Case #%lld: %0.9f\n",t,ans);
		//cout<<"Case #"<<t<<": "<<ans<<endl;
	}
}
