#include <bits/stdc++.h>
using namespace std;

int t,d,k,s,n;
double maxx,x,v;

int main()
{
	cin >> t;
	for(int z=1;z<=t;z++)
	{
		cin >> d >> n;
		maxx = 0;
		for(int i=0;i<n;i++)
		{
			cin >> k >> s;
			x = (d-k)/(double)s;
			maxx = max(x,maxx);
		}
		v = d/(double)maxx;
		cout << setprecision(10) << fixed << "Case #" << z << ": " << v << endl;
	}
}
