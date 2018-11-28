#include <bits/stdc++.h>
using namespace std;
int main()
{
	int t,q;
	cin>>t;
	q=1;
	while(t--)
	{
		double d,n,k,s,time,max=0;
		cin>>d>>n;
		while(n--)
		{
			cin>>k>>s;
			if(k==d)
				continue;
			time= (d-k)/s;
		//	cout<<time;
			if(time > max)
				max=time;
		//	cout<<max<<endl;
		}
		printf("Case #%d: %lf\n",q,(d/max));
		q++;
	}
	return 0;
}