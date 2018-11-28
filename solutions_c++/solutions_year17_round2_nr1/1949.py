#include<bits/stdc++.h>
using namespace std;
int main()
{
	std::ios::sync_with_stdio(false);
    int t;
	cin>>t;
	for(int i=1;i<=t;i++)
	{
		double d,n,a[2][2000+10];
		cin>>d>>n;
		for(int j=0;j<n;j++)
			cin>>a[0][j]>>a[1][j];
			
		double mini=-1;
		for(int j=0;j<n;j++)
			if((d-a[0][j])/a[1][j]>mini)
				mini=(d-a[0][j])/a[1][j];
		cout<<"Case #"<<i<<": "<<setprecision(6)<<fixed<<d/mini<<"\n";	
	}
}
