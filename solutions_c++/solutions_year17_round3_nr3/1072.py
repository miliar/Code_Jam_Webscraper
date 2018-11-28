#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>
#define float double
using namespace std;
int main()
{
	int t;
	cin>>t;
	for(int tc=1;tc<=t;tc++)
	{
		int n,k;
		cin>>n>>k;
		float avail;
		cin>>avail;
		float giv=0,temp;
		vector<float>data(n);
		for(int a=1;a<=n;a++)
		{
			cin>>data[a-1];
			giv+=data[a-1];
		}
		sort(data.rbegin(),data.rend());
		float avg=(giv+avail)/n;
		int c=0;
		while(avg<data[c])
		{
			c++;
			float sum=0;
			for(int d=c;d<n;d++)
				sum+=data[d];
			if(n!=c)
			avg=(sum+avail)/(n-c);
			else
			avg=avail;
		}
		float ans=pow(avg,n-c);
		for(int d=0;d<c;d++)
			ans*=data[d];
		printf("Case #%d: %.7lf\n",tc,ans);
	}
}

