#include <bits/stdc++.h>
using namespace std;
typedef long long int ll;

int main(void)
{
	int t, case_no;
	cin >> t;
	for(case_no = 1; case_no <= t;case_no++)
	{
		double d,n;
		cin >> d >> n;
		double max_time = 0.0;
		for(int i = 0;i < n;i++)
		{
			double k,s;
			cin >> k >> s;
			if((d-k)/s > max_time)
				max_time = (d-k)/s;
		}
		
		cout << "Case #" << case_no << ": ";
		printf("%.6lf\n", d/max_time);
	}
	return 0;
}