#include <iostream>
#include <vector>
#include <string>
#include <cstring>
#include <cstdio>
#include <algorithm>

using namespace std;

int main()
{
	int T;
	cin >> T;
	
	for (int t = 1; t <= T; t++)
	{
		int D, N;
		cin >> D >> N;
		
		double last = 0.0;
		
		for (int i = 0; i < N; i++)
		{
			int K, S;
			cin >> K >> S;
			last = max(last, (D - K) / (double)S);
		}
//		printf("Case #%d: %.8g\n", t, D / last);
		cout.precision(17);
		cout << "Case #" << t << ": " << D / last << "\n";
	}
	
	return 0;
}

