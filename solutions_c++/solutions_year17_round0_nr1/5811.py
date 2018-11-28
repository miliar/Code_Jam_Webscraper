#include<iostream>
#include<fstream>
#include<string>

using namespace std;

int main() {

	ifstream input;
	ofstream output;
	input.open("A-large.in");
	output.open("output.txt");

	int t;
	input >> t;
	for (int i = 0;i < t;i++) {
		string pancakes;
		int k;
		input >> pancakes >> k;

		int flip = 0;
		for (int j = 0;j <= pancakes.length()-k;j++) {
			if (pancakes[j] == '-') {
				flip++;
				for (int f = 0;f < k;f++) {
					if (pancakes[j+f] == '+')
						pancakes[j+f] = '-';
					else
						pancakes[j+f] = '+';
				}
			}
		}
		for (int j = 0;j < k;j++) {
			if (pancakes[pancakes.length() - 1 - j] == '-') {
				flip = -1;
				break;
			}
		}

		if (flip == -1) {
			output << "Case #" << i+1 << ": IMPOSSIBLE" << endl;
		}
		else {
			output << "Case #" << i+1 << ": " << flip << endl;
		}
	}

	return 0;
}