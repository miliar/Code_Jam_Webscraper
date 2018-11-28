#include <iostream>
#include <fstream>
using namespace std;

int main() {
	ifstream fin;
	fin.open("A-large.in");
//	fin.open("A-small-attempt0.in");
//	fin.open("A-small-attempt1.in");
//	fin.open("A-small-attempt2.in");
//	fin.open("A-small-practice.in");

	ofstream fout;
	fout.open("A-large.out");
//	fout.open("A-small-attempt0.out");
//	fout.open("A-small-attempt1.out");
//	fout.open("A-small-attempt2.out");
//	fout.open("A-small-practice.out");

	int t;
	fin >> t;
	for (int j = 1; j <= t; ++j) {
		long long D, N;
		fin >> D >> N;

		double maxHour = -1.0;
		for(int i = 0; i < N; i++) {
			long long ki, si;
			fin >> ki >> si;

			double di = D - ki;
			double hi = di / si;
			if(hi > maxHour)
				maxHour = hi;
		}

		double speed = D / maxHour;
//		fout << "Case #" << j << ": " << speed << endl;

		long long intSpeed = (long long) speed;
		fout << "Case #" << j << ": " << intSpeed << ".";

//		double diff = speed - intSpeed;
//		diff *= 1000000;
//		fout.precision(6);
//		fout << diff;

		double diff = speed - intSpeed + 1.0;
		diff *= 1000000;
		long long intDiff = (long long) diff;
		fout << intDiff/100000 % 10;
		fout << intDiff/10000 % 10;
		fout << intDiff/1000 % 10;
		fout << intDiff/100 % 10;
		fout << intDiff/10 % 10;
		fout << intDiff % 10;

		fout << endl;
	}

	fin.close();
	fout.close();
	return 0;
}

