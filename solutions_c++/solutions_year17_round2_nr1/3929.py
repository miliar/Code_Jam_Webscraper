#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<climits>
#include<iomanip>
using namespace std;

int main()
{
	int ti,t;
	cin>>t;
	for(ti = 1;ti<=t;ti++)
	{
		int n,i,j;
		long double d,s,k,maxm = -10000.0000000,val;
		cin>>d>>n;
		for(i = 1;i<=n;i++)
		{
			cin>>k>>s;
			k = d-k;
			val = k/s;
			if(val-maxm>0.0000001)
			{
				maxm = val;
			}
		}
		cout<<"Case #"<<ti<<": ";
		cout<<fixed<<std::setprecision(6)<<d/maxm<<"\n";
	}
}
