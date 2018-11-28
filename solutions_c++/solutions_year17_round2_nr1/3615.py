#include <bits/stdc++.h>
using namespace std;
int main()
{
	freopen("A-large (1).in","r",stdin);
	//freopen("out.txt","w",stdout);
	double a;
	cin>>a;
	double D,N;
	for(double t=1;t<=a;t++)
	{
		cout<<"Case #"<<t<<": ";
		cin>>D>>N;
		double maxiD=0;
		double maxi=0;
		double x,y,izi,lol;
		for(double i=0;i<N;i++)
		{
			cin>>x>>y;
			lol=D-x;
			izi=lol/y;
			maxi=max(maxi,izi);
		}
		maxi=D/maxi;
		printf("%.6f\n",maxi);
		//cout<<maxi<<endl;
	}
}