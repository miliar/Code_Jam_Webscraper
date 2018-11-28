#include <iostream>
#include <iomanip>
#include <vector>
#include <string>
#include <cstring>
#include <cstdio>
#include <algorithm>
#include <cmath>

using namespace std;


int main()
{
	int T;
	cin >> T;

	for (int t = 1; t <= T; t++)
	{
		int N, K;
		cin >> N >> K;

		vector<pair<double, int> > HR(N);
		for (int i = 0; i < N; i++)
		{
			int h, r;
			cin >> r >> h;
			double back = 2 * double(r) * double(h);
			HR[i].first = back;
			HR[i].second = r;
			cerr << i << ": " << back << " " << r << "\n";
		}
		
		sort(HR.rbegin(), HR.rend());
		
		double maxSyrup = 0;
		
		for (int i = 0; i < N - K + 1; i++)
		{
			cerr << "i: " << i << "\n";
			int maxR = -1;
			for (int j = 0; j < N; j++)
				if (maxR == -1 || HR[maxR].second < HR[j].second)
					maxR = j;
			cerr << "maxR: " << maxR << "\n";
			double syrup = double(HR[maxR].second) * double(HR[maxR].second);
			cerr << "syrup: " << syrup << "\n";
			double back = HR[maxR].first;
			HR[maxR].first = 0;
			HR[maxR].second = 0;

			int k = 1;
			for (int j = 0; j < N; j++)
			{
				if (k == K)
					break;
				if (HR[j].first > 0)
				{
					back += HR[j].first;
					k++;
				}
			}
			syrup += back;
			cerr << "back: " << back << "\n";
			cerr << "syrup: " << syrup << "\n";
			maxSyrup = max(maxSyrup, syrup);
		}
			
		cout << "Case #" << t << ": " << fixed << setprecision(9) << maxSyrup * M_PI << "\n";
	}
	
	return 0;
}

