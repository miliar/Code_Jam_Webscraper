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
		double U;
		cin >> N >> K >> U;

		vector<double> P(N);
		for (int i = 0; i < N; i++)
			cin >> P[i];
		
		sort(P.begin(), P.end());
		P.push_back(1.0);
		
		double minP = P[0];
		
		int i;
		for (i = 1; i <= N; i++)
		{
			cerr << "U: " << U << "\n";
			double maxU = i * (P[i] - minP);
			if (U < maxU)
			{
				minP += U / i;
				break;
			}
			else
			{
				U -= maxU;
				minP = P[i];
			}
		}
		
		cerr << "i: " << i << "\n";
		cerr << "minP: " << minP << "\n";
		
		double result = 1.0;
		for (int j = 0; j < i; j++)
			result *= minP;			
		for (int j = i; j < N; j++)
			result *= P[j];			
			
		cout << "Case #" << t << ": " << fixed << setprecision(9) << result << "\n";
	}
	
	return 0;
}

