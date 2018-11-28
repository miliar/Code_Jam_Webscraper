#include <string>
#include<cmath>
#include<cstdlib>
#include <fstream>
#include <iostream>

using namespace std;

int main(){

	ifstream input;
	input.open("A-large.in");
	ofstream output;
	output.open("output_file.txt");
	int out=0;
	int num;
	int step;
	string cupcakes;
	input >> num;
	for (int i = 0; i < num; i++) {
		out = 0;
		input >> cupcakes;
		input >> step;
		for (int j = cupcakes.length() - 1; j >= 0; j--) {
			if (cupcakes[j] == '-') {
				if (j >= step-1) {
					out++;
					cupcakes[j] = '+';
					for (int k = 1; k <= step-1;k++) {
						if (cupcakes[j - k] == '-')cupcakes[j - k] = '+';
						else cupcakes[j - k] = '-';
					}
				}
			}

		}

		if (cupcakes.find('-') == -1)
			output <<"Case #"<<i+1<<": "<< out << endl;
		else
			output << "Case #" << i + 1 << ": " << "IMPOSSIBLE" << endl;
	}
	return 0;
}