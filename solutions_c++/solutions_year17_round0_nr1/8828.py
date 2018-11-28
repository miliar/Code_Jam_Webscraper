#include <iostream>
#include <fstream>
#include <string>
using namespace std;

void flip(string& pan, int w, int k) {
	for (int i = 0; i < k; i++) {
		if (pan[w + i] == '-')
			pan[w + i] = '+';
		else
			pan[w + i] = '-';
	}
}

int main() {
	ifstream input;
	input.open("A-large.in");
	ofstream output("A.txt");
	int test;
	input >> test;
	for (int i = 0; i < test; i++) {
		string pancakes;
		int k;
		bool impossible = false;
		int amount = 0;
		input >> pancakes >> k;
		for (int q = 0; q<pancakes.length(); q++) {
			if (pancakes[q] == '-') {
				if (q + k > pancakes.length()) {
					impossible = true;
					break;
				}
				flip(pancakes,q, k);
				amount++;
			}
				

		}
		if (impossible)
			output  << "Case #" << i + 1 << ": IMPOSSIBLE" << endl;

		else
		output<< "Case #" << i+1 << ": " << amount << endl;
	}
	input.close();
	output.close();

}