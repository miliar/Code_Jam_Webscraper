#include <iostream>
#include <cstdio>
using namespace std;

int main()
{
	int t;
	cin>>t;
	for(int i=1;i<=t;i++)
	{
		double d;
		int n;
		cin>>d>>n;
		double p[n], v[n];
		for(int j=0;j<n;j++)
		{
			cin>>p[j]>>v[j];
		}
		double max=0;
		for(int j=0;j<n;j++)
		{
			double val = (d-p[j])/v[j];
			if(val>max)
			{
				max = val;
			}
		}
		double result = d/max;
		cout<<"Case #"<<i<<": ";
		printf("%.6f\n", result);
	}
}