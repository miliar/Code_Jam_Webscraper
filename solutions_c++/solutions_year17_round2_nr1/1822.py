
#include <iostream>
#include<bits/stdc++.h>
using namespace std;

int main() {
		ios::sync_with_stdio(false);
		cin.tie(0);
	int t,i;
	cin>>t;;
	for(i=1;i<=t;i++)
	{
		//float y;
		int n,j;
		long double d;
		cin>>d>>n;
		double k[n],s[n];
		double time[n];
		for(j=0;j<n;j++)
		{
			cin>>k[j]>>s[j];
			//time[i]=(float)(d-k[i])/(float)s[i];
		}
		for(j=n-1;j>=0;j--)
		{
			time[j]=(d-k[j])/s[j];
			if(j!=n-1)
			{
				time[j]=max(time[j],time[j+1]);
			}
		}
		//y=d/max;
		//cout<<" "<<max<<"\n";
		//cout<<d<<" "<<time[0]<<" ";
		printf("Case #%d: %.7lf\n",i,double(d/time[0]));
		//cout<<"Case #"<<i<<": "<<y;
	}
	return 0;
}

