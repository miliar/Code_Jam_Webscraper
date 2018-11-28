#include <iostream>
#include <algorithm>
using namespace std;

int T, N;
double D, K[1000], S[1000], time;

int main()
{
	cin >> T;
	for (int testCase = 1; testCase <= T; testCase++)
	{
		cin >> D >> N;
		for (int i = 0; i < N; i++)
			cin >> K[i] >> S[i];

		time = 0;
		for (int i = 0; i < N; i++)
			time = max(time, (D - K[i]) / S[i]);
		
		cout.setf(ios::showpoint); 
		cout << fixed;
		cout.precision(6);
		cout << "Case #" << testCase << ": " << D / time << endl;
	}

	return 0;
}