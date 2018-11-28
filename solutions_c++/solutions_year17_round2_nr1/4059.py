#include<iostream>
#include <iomanip> 
#include<fstream>

using namespace std;

ifstream input;
ofstream output;
int T;

double solve(long long beginning[], long long speed[], long long N, long long D) {
	double max = double(D - beginning[0]) / speed[0];
	for (int i = 1; i < N; i++) {
		if ((double(D - beginning[i]) / speed[i]) > max) {
			max = double(D - beginning[i]) / speed[i];
		}
	}
	return D / max;
}

int main() {

	input.open("in.in");
	output.open("p1.txt");
	input >> T;

	for (int t = 1; t <= T; t++) {

		long long D, N, *speed, *beginning;
		input >> D >> N;

		beginning = new long long[N];
		speed = new long long[N];
		
		for (int n = 0; n < N; n++) {
			input >> beginning[n];
			input >> speed[n];
		}
		output << "Case #" << t << ": " << fixed << setprecision(6) << solve(beginning, speed, N, D) << endl;

	}
}

