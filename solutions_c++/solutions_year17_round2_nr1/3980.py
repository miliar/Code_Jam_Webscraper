#include<bits/stdc++.h>
using namespace std;

int main()
{
//	freopen("input.txt","r",stdin);
//	freopen("output.txt","w",stdout);
	int test,n;
	double d,x,maxi,sp;
//	double a[10000];
	cin>>test;
	for(int tt=1;tt<test+1;tt++)
	{
		maxi=0;
		cin>>d>>n;
		for(int i=1;i<n+1;i++)
		{
			cin>>x>>sp;
			x = d-x;
			maxi = max(maxi,(double)(x/sp));
//			cout<<maxi<<endl;
		}
		cout<<"Case #"<<tt<<": "<<fixed<<setprecision(7)<<d/maxi<<"\n";
	}
}
