#include<bits/stdc++.h>
using namespace std;

int main()
{
	freopen ("input.txt","r",stdin);
	freopen ("output.txt","w",stdout);
	int t;
	cin>>t;
	int j=1;
	while(t--)
	{
		cout<<"Case #"<<j<<": ";
		j++;
		int d,n;
		cin>>d>>n;
		double max = 0.0;
		double speed,dist;
		for(int i=0;i<n;i++)
		{
			int x,s;
			cin>>x>>s;
			double t = (double)(d-x)/(double)s;
			if(t>=max)
			{
				max = t;
				dist = x;
				speed = s;
			}
		}
		double temp = (d-dist)/speed;
		printf("%.6lf\n",d/temp);
	}
	return 0;
}
