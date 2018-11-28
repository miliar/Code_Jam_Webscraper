#include <iostream>
#include <fstream>
#include <string>
using namespace std;

string perfect_grill = "";
int flipper = -1;
int best_flips = -1;

void solve(string grill, int flips, int pancake) {
	if (grill.compare(perfect_grill) != 0) {
		for (; pancake <= grill.length() - flipper; pancake++) {
			for (int i = pancake; i < pancake + flipper; i++) {
				grill[i] = (grill[i] == '+') ? '-' : '+';
			}
			solve(grill, flips + 1, pancake + 1);
			for (int i = pancake; i < pancake + flipper; i++) {
				grill[i] = (grill[i] == '+') ? '-' : '+';
			}
		}
	}
	else {
		if (flips < best_flips) {
			best_flips = flips;
		}
	}
}

void main() {
	ifstream fin("A-small-attempt0.in");
	ofstream fout("A-small-attempt0.out");

	int inputs = 0;
	string grill = "";
	
	fin >> inputs;

	for (int i = 0; i < inputs; i++) {
		fin >> grill;
		fin >> flipper;
		perfect_grill.clear();
		best_flips = grill.length() + 1;

		for (int c = 0; c < grill.length(); c++) {
			perfect_grill += "+";
		}

		int flips = 0;
		solve(grill, flips, 0);
		if (best_flips > grill.length()) {
			fout << "Case #" << i + 1 << ": IMPOSSIBLE";
		}
		else {
			fout << "Case #" << i + 1 << ": " << best_flips;
		}
		if (i + 1 < inputs) {
			fout << endl;
		}
	}
	
	/*cout << "Press any key to continue...";
	cin.ignore();
	cin.get();*/

	fin.close();
	fout.close();
}