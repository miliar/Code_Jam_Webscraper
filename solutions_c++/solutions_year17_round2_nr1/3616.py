#include <bits/stdc++.h>
using namespace std;

#define ll long long int;

int main(int argc, char const *argv[])
{
	int t;
	cin>>t;
	int n[100];
	double s[100][1000];
	long long int d[100],k[100][1000];
	double result[100];
	for (int i = 0; i < t; ++i)
	{
		cin>>d[i]>>n[i];
		for (int j = 0; j < n[i]; ++j)
		{
			cin>>k[i][j]>>s[i][j];
		}
	}
	for (int i = 0; i < t; ++i)
	{
		double max=(d[i]-k[i][0])/s[i][0];
		int index;
		for (int j = 1; j < n[i]; ++j)
		{
			double time=(d[i]-k[i][j])/s[i][j];
			if(time>max)
			{
				max=time;
				index=j;
			}	
		}
		result[i]=d[i]/max;
	}
	for (int i = 0; i < t; ++i)
	{
		//cout<<"Case #"<<i+1<<": "<<(double)result[i]<<endl;
		printf("Case #%d: %lf\n",i+1,result[i]);
	}
	return 0;
}