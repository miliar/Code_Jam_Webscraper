#include <cstdio>
#include <cstdlib>
#include <string>
#include <algorithm>
#include <vector>
#include <iostream>  // includes cin to read from stdin and cout to write to stdout
using namespace std;  // since cin and cout are both in namespace std, this saves some text
int D, N;
vector<pair<int, int>> H;
int main() {
	int t;
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
	for (int i = 1; i <= t; ++i) {
		cin >> D >> N;
		double ret = 0;
		for (int j = 0; j < N; j++)
		{
			int S, K;
			cin >> K >> S;
			ret = max(double(D - K) / (double)S, ret);
			//printf("%lf  \n", ret);
		}

		cout << "Case #" << i << ": " ;
		printf("%lf\n", D / ret);
		// cout knows that n + m and n * m are ints, and prints them accordingly.
		// It also knows "Case #", ": ", and " " are strings and that endl ends the line.
	}

	return 0;
}