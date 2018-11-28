/*
 * ./executable < input > output
 */
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
using namespace std;
int main()
{
	int T;
	cin >> T;
	for(int t = 1; t <= T; t++)
	{
		double D;
		int N;
		cin >> D >> N;
		double time_max = 0; // this is time minimum time the traveler must spend
		// we will be looking for the slowest traveller, i.e. maximize time;
		for(int i = 0; i < N; i++)
		{
			double Ki, Si;
			cin >> Ki >> Si;
			double distance_i = D-Ki;
			double time_i = distance_i/Si;
			if(time_i > time_max)
				time_max = time_i;
		}
		double result = D / time_max;
		cout << "Case #" << t << ": ";
		cout << fixed << result;
		cout << endl;
	}
}
