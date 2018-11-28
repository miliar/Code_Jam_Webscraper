#include <iostream>
#include <fstream>
using namespace std;

int min, max;

void calc(int N, int K) {
	int h = ceil(log2(K + 1));
	long long siblings = pow(2, h - 1);

	double magical = N * pow(2, -(h - 1)) + pow(0.5, h - 1) - 1;

	double e = magical - floor(magical);
	if (e == 0) {
		double result = (magical - 1) / 2;
		min = floor(result);
		max = ceil(result);
	}
	else {
		long long required = K + 1 - pow(2, h - 1);
		long long more = e * siblings;
		
		if (required <= more) {
			double result = (ceil(magical) - 1) / 2;
			min = floor(result);
			max = ceil(result);
		}
		else {
			double result = (floor(magical) - 1) / 2;
			min = floor(result);
			max = ceil(result);
		}
	}
	if (min == -1) min = 0;
	/*bool even = ((N % 2) == 0);

	tree[0][0] = N;
	tree[0][1] = even ? 0 : 1;
	tree[0][2] = even ? 1 : 0;

	for (int i = 1; i < treeHeight; i++) {
		
	}*/
}

int main() {
	ifstream infile("in2.in");
	ofstream out("out12.txt");
	int T;
	infile >> T;

	for (int t = 0; t < T; t++) {
		long long N, K;
		infile >> N >> K;
		
		calc(N, K);
		out << "Case #" << t + 1 << ": " << max << " " << min << endl;
	}

	system("pause");
	return 0;
}
