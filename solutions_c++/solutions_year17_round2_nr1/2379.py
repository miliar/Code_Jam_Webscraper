#include<bits/stdc++.h>
using namespace std;
int n,t;
int main()
{
	ifstream cin("1.in");
	ofstream cout("1.out");
	cin >> t;
	for(int j = 1; j <= t; j++)
	{
		double x, t = 0;
		cin >> x >> n;
		for(int i = 0 ; i < n; i++)
		{
			double a,v;
			cin >> a >> v;
			t = max(t,1.0*((x-a)/v));
		}
		cout <<"Case #" << j << ": " <<setprecision(7) << fixed << x/t << "\n";
	}
}
