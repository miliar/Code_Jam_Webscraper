#define _USE_MATH_DEFINES
#include <cmath>
#include <cstdio>
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

bool sortinrev(const pair<double,double> &a, 
               const pair<double,double> &b)
{
       return (a.first > b.first);
}

int main()
{
	int t;
	cin>>t;
	for(int i=1;i<=t;i++)
	{
		int n, k;
		cin>>n>>k;
		double R[n], H[n];
		for(int j=0;j<n;j++)
		{
			cin>>R[j]>>H[j];
		}
		vector<pair<double, double> > V;
		for(int j=0;j<n;j++)
		{
			V.push_back(make_pair(R[j]*H[j], R[j]));
		}
		sort(V.begin(), V.end(), sortinrev);

		double greatest_r = V[0].second;

		for(int j=0;j<k;j++)
		{
			if(V[j].second > greatest_r)
			{
				greatest_r = V[j].second;
			}
		}
		double least_rh = V[k-1].first;

		double val = greatest_r*greatest_r + 2*least_rh;

		double min = val;

		for(int j=k;j<n;j++)
		{
			if(V[j].second > greatest_r)
			{
				if(V[j].second*V[j].second + 2*V[j].first > min)
				{
					min = V[j].second*V[j].second + 2*V[j].first;
				}
			}
		}
		double res = min;

		for(int j=0;j<k-1;j++)
		{
			res+=V[j].first*2;
		}

		double result = res*M_PI;

		cout<<"Case #"<<i<<": ";
		printf("%.7f\n", result);

	}
}