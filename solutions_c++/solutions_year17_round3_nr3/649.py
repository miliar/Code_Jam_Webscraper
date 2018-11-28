#include <iostream>
#include <iomanip>
#include <stdio.h>
#include <string.h>
#include <string>
#include <stdlib.h>
#include <vector>
#include <utility>
#include <algorithm>

using namespace std;
typedef long long int lli;

double dmin(double a, double b)
{
	return ( a < b ) ? a : b;
}

int main()
{
	ios_base::sync_with_stdio(0); cin.tie(0);
	
	int T, N, K;
	double U;
	cin >> T;
	for(int aa=1;aa<=T;++aa)
	{
		double ans = 0;
		cin >> N >> K;
		cin >> U;
		vector<double> P(N);
		for(int i=0;i<N;++i)
			cin >> P[i];
		sort(P.begin(), P.end());
		
		double deltaU;
		double level = 0;
		int index;
		for(index=0;index<N-1 && U>0;++index)
		{ // bring the 0 to i'th elements up to the level
			deltaU = dmin((P[index+1]-P[index])*(index+1), U);
			cerr << " " << deltaU << "  " << P[index+1] << " " << P[index] << endl;
			level = P[index]+deltaU/(index+1);
			U-=deltaU;
		}
		if(U > 0)
		{
			deltaU = dmin((1-P[index])*(index+1), U);
			level = P[index]+deltaU/(index+1);
			U-=deltaU;
		}
		cerr << level << " " << U << endl;
		if(level >= 1)
			ans = 1;
		else{
			ans = 1.0;
			for(int i=0;i<N;++i)
			{
				if(P[i] < level)
					ans *= level;
				else
					ans *= P[i];
			}
		}
		
		
		cout << "Case #" << aa << ": " << fixed << setprecision(6) << ans << endl;
	}
	
	return 0;
}
