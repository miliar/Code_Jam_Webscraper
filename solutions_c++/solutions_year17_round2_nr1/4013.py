#include<iostream>
#include<iomanip>
using namespace std;
int main()
{
	int T;
	cin>>T;
	for(int j=1;j<=T; j++)
	{
		double destination;
		int n;
		cin>>destination;
		cin>>n;
		double a[n][2];
		for(int i=0;i<n; i++)
		{
			cin>>a[i][0]>>a[i][1];
		}
		double timeArray[n];
		for(int i=0; i<n; i++)
		{
			timeArray[i]=(destination-a[i][0])/a[i][1];
		}
		double maxTime=0.0;
		for(int i=0; i<n; i++)
		{
			if(timeArray[i]>maxTime)
			{
				maxTime=timeArray[i];
			}
		}
		float annieSpeed=(destination/maxTime);
		cout<<fixed;
		cout<<"Case #"<<j<<": "<<setprecision(6)<<annieSpeed<<"\n";
	}
	return 0;
}
