#include <iostream>
#include <algorithm>
#include <iomanip>

const double EPS=0.000000001;

using namespace std;

void solve(int t)
{
	// read input
	int n,k;
	cin >> n >> k;
	double u,p[n];
	cin >> u;

	for (int i=0; i<n; i++)
		cin >> p[i];

	double v=1,sum=0;
	for (int i=0; i<n; i++)
		sum+=1-p[i];
	if (sum<u-EPS || sum>u+EPS)
	{
		// binary search
		double a=1,b=0,mid;
		for ( ; ;)
		{
			mid=(a+b)/2;
			sum=0,v=1;
			for (int i=0; i<n; i++)
			{
				if (p[i]<mid)
				{
					sum+=mid-p[i];
					v*=mid;
				}
				else v*=p[i];
			}
//			cout << mid << " " << sum << endl;

			if (sum>u-EPS && sum<u+EPS)
				break;
			if (sum>u) a=mid;
			else b=mid;
		}

	}


	// format output
	cout.setf(ios::fixed,ios::floatfield);
	cout << "Case #" << setprecision(0) << t << ": ";
	cout << setprecision(6) << v << endl;
}

int main()
{
	int t;
	cin >> t;

	for (int i=1; i<=t; i++)
		solve(i);
}
