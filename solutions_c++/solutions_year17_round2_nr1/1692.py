#include <iostream>
#include <iomanip>
using namespace std;
int main()
{
	int t,n,d,test,a,b,i;
	float speed,min,time;
	cin>>t;
	cout <<setprecision(7);
	for(test=1;test<=t;test++)
	{
		cin>>d>>n;
		min=0;
		for(i=0;i<n;i++)
		{
			cin>>a>>b;
			time=float(d-a)/float(b);
			//cout<<time;
			if(time>min)
			{
				min=time;
			}
		}
		speed=float(d)/min;
		cout<<"Case #"<<test<<": "<<speed<<"\n";
	}

}