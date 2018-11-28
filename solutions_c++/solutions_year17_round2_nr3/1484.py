#include<iostream>
#include<fstream>
#include<iomanip>
double compute(int route[], int distance[], int speed[], int N);
using namespace std;
int main() {
	int T;
	ifstream input;
	ofstream output;
	input.open("h.txt");
	output.open("ex3)1.txt");
	input >>T;
	for (int t = 1; t <= T; t++) {
		int N, Q;
		input >> N >> Q;
		int distance[1000], speed[1000];
		for (int i = 0; i < N; i++)
			input >> distance[i] >> speed[i];
		int route[1000];
		int x;
		int k = 1;
		route[0] = 0;
		for (int i = 0; i < N; i++)
			for (int j = 0; j < N; j++){
				input>>x;
				if (x != -1) {
					route[k] = x;
					k++;
				}
			}
		int u1, q1;
		input >> u1>>q1;
		output<<"Case #"<<t<<": "<<fixed<<setprecision(6)<<compute(route, distance, speed, N)<<endl;
	}
	system("pause");
	return 0;
}
double compute(int route[], int distance[], int speed[], int N) {
	double mintime[1000];
	for (int i = 1; i < N; i++)
		mintime[i] = -1;
	mintime[0] = 0;
	for (int i = 0; i < N-1; i++) {
		int totaldist = 0;
		for (int j = i+1; j < N; j++) {
			totaldist += route[j];
			if (totaldist > distance[i])
				break;
			double temp = double(totaldist) / speed[i] + mintime[i];
			if (mintime[j] == -1)
				mintime[j] = temp;
			if (temp < mintime[j])
				mintime[j] = temp;
		}
	 }

	return mintime[N - 1];
}