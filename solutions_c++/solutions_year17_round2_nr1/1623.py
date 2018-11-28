#include <bits/stdc++.h>
#include <bits/stdc++.h>
using namespace std;

int main()
{	

freopen("A-large (1).in", "r", stdin);
  freopen("A-large (1).out", "w", stdout);
	int t;
	cin >> t;
	for (int k = 1; k <= t; ++k)
	{
		double d;
		long long n;
		cin >> d >> n;
		double res =0;
		for (int i = 0; i < n; ++i)
		{	double k,s;	
			cin  >> k >> s;
			double time = (d - k ) / s;
			res = max(res,time);

		}
		
		double speed = d/res;



		cout << "Case #" << k << ": " << fixed << speed << endl;
	}
}


