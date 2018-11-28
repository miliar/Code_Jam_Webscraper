#include <iostream>
#include <fstream>
#include <set>

using namespace std;

int main() {
	int numCases;
	ifstream fin("A-large.in");
//	ofstream fout("A.out");
	FILE * fout = fopen("A.out", "w");
	fin >> numCases;
	for (int cases = 1; cases < numCases+1; cases++) {
		long dest, num;
		fin >> dest >> num;
		double time = 0;
		for (int i = 0; i < num; i++) {
			long pos, speed;
			fin >> pos >> speed;
			double tmp = (dest - pos) * 1.0 / speed;
			if (tmp > time) {
				time = tmp;
			}
		}
		double ans = dest / time;
		fprintf(fout, "Case #%d: %.06f\n", cases, ans);
	}
	fin.close();
//	fout.close();
	fclose(fout);
	return 0;
}
