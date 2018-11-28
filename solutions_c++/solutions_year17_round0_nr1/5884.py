// basic file operations
#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main() {
	ifstream input;
	ofstream output;
	input.open("A-large.in");
	output.open("out.txt");
	int t;
	input >> t;
	for (int i = 1; i <= t; i++){
		string n;
		int k;
		input >> n;
		input >> k;
		int out = 0;
		bool possible = true;

		for (int j = 0; j < n.length(); j++){
			if (n[j] == '-'){
				if (j + k <= n.length()){
					out++;
					for (int m = 0; m < k; m++){
						if (n[j + m] == '-'){
							n[j + m] = '+';
						}
						else {
							n[j + m] = '-';
						}
					}
				}
				else {
					possible = false;
					break;
				}
			}
		}
		
		if (possible)
			output <<"Case #" << i << ": " << out << '\n';
		else
			output << "Case #" << i << ": " << "IMPOSSIBLE" << '\n';
	}
	input.close();
	output.close();
}