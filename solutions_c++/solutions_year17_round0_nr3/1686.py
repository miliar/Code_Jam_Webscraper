#include <iostream>
#include <fstream>
#define ll long long
using namespace std;

ifstream in("C-large.in");
//ifstream in("input.txt");
ofstream out("output.txt");

int T, tt;
ll N, K;

int main() {

	long long temp1, temp2;
	in >> T;

	for (tt = 1; tt <= T; ++tt) {
		in >> N >> K;
		temp1 = N;
		temp2 = K;
			
		// for the last stoll
		while (K > 1) {
			if (N % 2 == 0) {
				if (K % 2 == 0) { N = N / 2, K = K / 2; }
				else { N = N / 2 - 1, K = (K / 2); }
			}

			else {
				if (K % 2 == 0) { N = (N - 1) / 2, K = K / 2; }
				else { N = (N - 1) / 2, K = (K - 1) / 2; }
			}
			//out << N << " " << K << endl;
		}
		out << "Case #" << tt << ": " << N / 2 << " " << (N - 1) / 2 << endl;
		//out << "Case #" << tt << ": " << Max << " " << Min << endl;
	}

	in.close();
	out.close();
}