#include<bits/stdc++.h>
using namespace std;
int main()
{
	int t;
	cin>>t;
	for(int i = 0; i<t; i++)
	{
		double d, n, a[2][2000];
		cin>>d>>n;
		for(int j = 0; j<n; j++)
			cin>>a[0][j]>>a[1][j];
		double min = -1;
		for(int j = 0; j<n; j++)
			if((d - a[0][j])/a[1][j] > min)
				min = (d - a[0][j])/a[1][j];
		cout<<"Case #"<<i + 1<<": ";
			printf("%6f\n",d/min);
	}
}
