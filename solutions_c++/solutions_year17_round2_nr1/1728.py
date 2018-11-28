#include <bits/stdc++.h>
using namespace std;

int main()
{
	ios::sync_with_stdio(false);
	
	int T;
	cin >> T;
	
	for(int ii = 1; ii <= T; ii++)
	{
		printf("Case #%d: ", ii);
		
		int d, n;
		cin >> d >> n;
		
		double ans = 0;
		for(int i = 0; i < n; i++)
		{
			int k, s;
			cin >> k >> s;		
			
			double t = 1.0 *(d -k)/s;
			
			if(t > ans)
				ans = t;
		}
		
		double speed = 1.0 *d/ans;
		printf("%lf\n", speed);
	}
	
	return 0;
}
