#include <iostream>
#include <fstream>
#include <cstring>
#include <cstdlib>
#include <cstddef>
#include <cstdint>
#include <cinttypes>
#include <cctype>
#include <vector>
#include <string>
#include <sstream>

using namespace std;

void recur(int N, int K, int vals[]) {

	if (N % 2 == 0) {

		//BASE CASE
		if (K == 1) {
			vals[0] = N/2;
			vals[1] = (N/2) -1;
			return;
		}

		//BASE CASE 2
		if (N == 2) {
			//K = 2
			vals[0] = 0;
			vals[1] = 0;
			return;
		}

		int new_K = K/2;
		int new_N;
		if (K % 2 == 0) {
			new_N = (N/2);
		}
		else {
			new_N = (N/2) - 1;
		}
		recur(new_N, new_K, vals);
	}
	else {
		//BASE CASE
		if (K == 1) {
			vals[0] = N/2;
			vals[1] = N/2;
			return;
		}

		recur(N/2, K/2, vals);

	}

}


int main() {

	int num;
	string line;
	ifstream myfile ("small2.in");
	ofstream output ("output_small2.txt");

	if (myfile.is_open()) {

		myfile >> num;
		getline(myfile, line);

		for (int i = 1; i <= num; i++) {
			getline(myfile, line);

			istringstream iss(line);

			int N;
			int K;

			iss >> N;
			iss >> K;

			int vals [2];
			recur(N, K, vals);

			output << "Case #" + to_string(i) + ": " + to_string(*vals) + " " 
			+ to_string(*(vals+1)) << '\n';	
		}

		myfile.close();
	}

	return 0;
}