#include<bits/stdc++.h>
using namespace std;


int main()
{
	
	int t;
	cin>>t;
	while(t--)
	{
	
		int d,n,x,s;
		cin>>d>>n;
		double maxtime = -1;
		for(int i=0;i<n;i++)
		{	cin>>x>>s;
			double time = (double)(d-x)/(double)s;
			maxtime=max(time,maxtime);
		}
		
		double speed=(double)d/maxtime;
		printf("%.6f\n",speed);

	}
	
}
