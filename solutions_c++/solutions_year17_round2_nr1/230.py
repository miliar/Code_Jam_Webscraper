
#include <iostream>
#include <string>
#include <cmath>
#include <bitset>
#include <algorithm>
#include <map>
#include <vector>
using namespace std;
double eps = 1e-15;


int main() {
	int T;
	cin >> T;
	for (int tc = 1; tc <= T; tc++)
	{
		double D;
		int N;
		cin >> D >> N;
		double maxT = 0;
		for (int i = 0; i < N; i++)
		{
			double K, S;
			cin >> K >> S;
			maxT = max(maxT, (D - K) / S);
		}
		cout.precision(7);
		cout << "Case #" << tc << ": " << fixed<<D/ maxT << endl;

	}

}