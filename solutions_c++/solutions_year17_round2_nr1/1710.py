#include <iostream>
#include <iomanip>
using namespace std;

int main()
{
	int t;
	cin>>t;
	int it=1;
	while(it<=t)
	{
		long int d,n,i;
		cin>>d>>n;
		long int x,s;
		double max=0.0;
		for(i=0;i<n;i++)
		{
			cin>>x>>s;
			x=d-x;
			double time=(double) x;

			time/=s;
			if(time>max)
			{
				max=time;
			}

		}

		double ans=0.0;
		ans=(double)d;
		ans/=max;


		cout <<fixed;

		cout<<"Case #"<<it<<": "<<setprecision(6)<<ans<<endl;

		it++;
	}

	return 0;
}