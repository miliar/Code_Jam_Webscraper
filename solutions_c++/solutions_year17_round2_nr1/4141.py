#include<bits/stdc++.h>
using namespace std;
int main()
{
	int t;
	cin>>t;
	for(int i=0;i<t;i++)
	{
		int d,n;
		cin>>d>>n;
		double max=0;
		for(int i=0;i<n;i++)
		{
			double h,s;
			cin>>h>>s;
			double t=(d-h)/s;
			if(t>max)
			max=t;
			
		}
		double f=d/max;
		cout<<fixed;
		std::cout << std::setprecision(6) << f << '\n';
		
	}
}
