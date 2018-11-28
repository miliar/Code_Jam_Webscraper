#include <iostream>
#include <algorithm>
#include <iomanip>

const double PI=3.1415926535897932384;

using namespace std;

void solve(int t)
{
	// read input
	int n,k;
	cin >> n >> k;
	pair<long long,long long> p[n];

	for (int i=0; i<n; i++)
	{
		cin >> p[i].second >> p[i].first;
		p[i].first*=p[i].second;
	}
	sort(p,p+n);

	double best=0;
	for (int i=0; i<n; i++)
	{
		double area=PI*p[i].second*p[i].second+PI*2*p[i].first;
//		cout << i << " " << p[i].first << " " << p[i].second << " " << area << endl;
//		break;
		int cnt=1;
		for (int j=n-1; j>=0 && cnt<k; j--)
            if (i!=j && p[i].second>=p[j].second)
            {
            	cnt++;
            	area+=PI*2*p[j].first;
//            	cout << "  " << j << endl;
            }
		best=max(area,best);
	}

	// format output
	cout.setf(ios::fixed,ios::floatfield);
	cout << "Case #" << setprecision(0) << t << ": ";
	cout << setprecision(9) << best << endl;
}

int main()
{
	int t;
	cin >> t;

	for (int i=1; i<=t; i++)
		solve(i);
}
