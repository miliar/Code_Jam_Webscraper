#include <iostream>
#include <cmath>
#include <string>
#include <vector>
#include <algorithm>
#include <map>
#include <iomanip>
using namespace std;

int main()
{
	int t;
	cin>>t;
	for(int i=0;i<t;i++)
	{
		double d;
		int n;
		cin>>d>>n;
		double dis[n],s[n];
		double mint=0;
		for(int j=0;j<n;j++)
		{
			cin>>dis[j]>>s[j];
			double k=(d-dis[j])/s[j];
			if(mint<k) mint=k;
		}
		cout<<"Case #"<<i+1<<": ";printf("%.7f",d/mint);cout<<endl;
	}
	
	
}
	
