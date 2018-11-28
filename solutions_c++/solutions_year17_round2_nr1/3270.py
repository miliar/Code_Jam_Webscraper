#include <iostream> 
#include <string>
#include <fstream>
#include <vector>
#include <set>
#include <algorithm>
#include <map>
#include <iomanip>

using namespace std;


int main() {
	ifstream fin("in.txt");
	ofstream fout("out.txt");

	int T;
	fin >> T;
	for (int caseNo = 1; caseNo <= T; caseNo++) {
		cout << caseNo << endl;
		long D, N;
		fin >> D >> N;

		vector<long> pos(N,0);
		vector<long> speed(N,0);
		long double slowest = 9999999999999;
		for (int n = 0; n < N; n++) {
			fin >> pos[n] >> speed[n];

			long double time = (long double)(D - pos[n]) / speed[n];
			cout << pos[n] << " " << speed[n] << " " << time << " " << D / time << endl;
			slowest = min(D / time, slowest);
		}
		
		cout << D << " " << N << endl;

		fout << "Case #" << caseNo << ": " << fixed << std::setprecision(9) << slowest << endl;
		cout << "Case #" << caseNo << ": " << fixed << std::setprecision(9) << slowest << endl;
		//cout << t;
	}

}