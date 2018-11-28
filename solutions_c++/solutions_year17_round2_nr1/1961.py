#include <iostream>
#include <algorithm>
#include <iomanip>

using namespace std;

int main()
{
	cout << fixed;
	cout << setprecision(9);

	int T, t;

	cin >> T;

	double D, N, K, S, slowest;

	for (t = 1; t <= T; t++)
	{
		slowest = 0.0;

		cin >> D >> N;

		for (int j = 0; j < N;j++)
		{
			cin >> K >> S;

			if (D - K > 0)
			{
				slowest = max(slowest, (D-K)/S);
			}
		}		

		cout << "Case #" << t << ": " << (D/slowest) << endl;
	}

	return 0;
}