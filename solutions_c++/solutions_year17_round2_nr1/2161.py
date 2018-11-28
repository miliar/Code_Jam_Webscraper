#include<iostream>
#include<stdio.h>
#include<vector>
#include<algorithm>
#include<string.h>
#include<map>
using namespace std;
int main()
{
	int t;
	cin>>t;
	for(int ti =1;ti<=t;ti++)
	{
		double d;
		int n;
		cin>>d;
		cin>>n;
		double start, speed;
		cin>>start>>speed;
		double ans;
		ans = (d-start)/speed;
		for(int i=0;i<n-1;i++)
		{
			cin>>start>>speed;
			ans = ( ((d-start)/speed) < ans )?ans:(d-start)/speed;
		};
		ans = d/ans;
		cout<<"Case #"<<ti<<": ";
		printf("%.6f\n",ans );
	}
	return 0;
}