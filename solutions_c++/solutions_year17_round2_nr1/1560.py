#include<iostream>
#include<fstream>
#include <iomanip> 
using namespace std;
double compute(long long start[], long long speed[], long long N, long long D);
int main() {
	long long T;
	ifstream input;
	input.open("h.txt");
	ofstream output;
	output.open("ex1.txt");
	input >> T;
	for (long long t = 1; t <= T; t++) {
		long long D, N;
		input >> D >> N;
		long long*speed;
		speed = new long long[N];
		long long*start;
		start = new long long[N];
		for (long long n = 0; n < N; n++) {
			input >> start[n] >> speed[n];
		}
		output<< "Case #"<<t<<": "<<fixed<<setprecision(6)<<compute(start, speed, N, D)<<endl;
	}

	system("pause");
	return 0;
}

double compute(long long start[], long long speed[], long long N, long long D) {
	double max = double(D - start[0]) / speed[0];
	for (int i = 1; i < N; i++) {
		if ((double(D - start[i]) / speed[i]) > max) {
			max = double(D - start[i]) / speed[i];
		}
	}
	return D / max;
}