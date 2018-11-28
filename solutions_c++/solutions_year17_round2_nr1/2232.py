#include<bits/stdc++.h>
using namespace std;
int main()
{
	freopen("a.in","r",stdin);
    freopen("b.out","w",stdout);
	long int t,d,n,*pos,*speed;
	double *time;
	cin>>t;
	for(int p=1;p<=t;p++)
	{
		cin>>d>>n;
		pos=new long int[n];
		speed=new long int[n];
		time=new double[n];
		for(long int i=0;i<n;i++)
		{
			cin>>pos[i]>>speed[i];
		}
		for(long int i=0;i<n;i++)
		{
			time[i]=((d-pos[i])*1.0)/speed[i];
		}
		double high=0;
		for(long int i=0;i<n;i++)
		{
			if(high<time[i])high=time[i];
		}
		double ans=(d*1.0)/high;
		cout << fixed << setprecision(6);
		cout<<"Case #"<<p<<": "<<ans<<endl;
	}
	return 0;
}
