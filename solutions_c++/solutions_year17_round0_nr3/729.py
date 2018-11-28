#include <iostream>
#include <fstream>
#include <cmath>

using namespace std;

int main() {
	ifstream fin ("C.in");
	ofstream fout ("C.out");

	int T; 
	fin >> T;
	for (int t = 1; t <= T; t++) {
		long long N, K; 
		fin >> N >> K;
		while (K != 1) {
			if (K % 2 == 1 && N % 2 == 0) 
				N = N / 2 - 1;
			else
				N = N / 2;
			K /= 2;
		}
		fout << "Case #" << t << ": ";
		if (N % 2 == 0)
			fout << (N/2) << " " << (N/2)-1;
		else
			fout << (N/2) << " " << (N/2);
		fout << endl;
	}

	fout.close();

	return 0;
}