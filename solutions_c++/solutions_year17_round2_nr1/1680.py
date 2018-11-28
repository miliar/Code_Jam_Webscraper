#include <iostream>
#include <fstream>
#include <algorithm>
#include <math.h>
#include <iomanip>

using namespace std;

int main() {
	ofstream fout("ridelarge.out");
	ifstream fin("ridelarge.in");
	int T;
	fin >> T;
	for (int t = 0; t < T; t++) {
		int D, N;
		fin >> D >> N;
		double speed;
		for (int n = 0; n < N; n++) {
			double ts, tp;
			double tt;
			fin >> tp >> ts;
			tt = (D - tp) / ts;
			double sp = D / tt;
			if (n == 0) speed = sp;
			else if (speed > sp)  speed = sp;
		}
		cout << "Case #" << t + 1 << ": " << setprecision(17) << speed << endl;
		fout << "Case #" << t + 1 << ": " << setprecision(17) << speed << endl;
	}
	system("pause");
}