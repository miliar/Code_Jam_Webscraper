#include <iostream>
#include <string>
#include <vector>

using namespace std;


int main()
{
	ios::sync_with_stdio(false);
	int T;
	cin >> T;
	for (int t = 0; t < T; t++)
	{
		int N, D;
		cin  >> D >> N;
		
		double mx = 0.0;
		
		for (int i = 0; i < N; ++ i)
		{
			int K, M;
			cin >> K >> M;
			double current =  (double) (D-K) / M;
			if (current > mx) mx = current;
		}

		cout.precision(7);
		
		cout << "Case #" << t+1 << ": " ;
		cout << fixed << (double) D / mx << endl;
	
	}

}