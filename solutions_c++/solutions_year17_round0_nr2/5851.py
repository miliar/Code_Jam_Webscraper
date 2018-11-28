// basic file operations
#include <iostream>
#include <fstream>
#include <string>
using namespace std;

string decrement(string in, int pos){
	string out = in;
	if (out[pos] == '0'){
		out[pos] = '9';
		out = decrement(out, pos - 1);
	}
	else {
		out[pos] -= 1;
	}
	return out;
}

int main() {
	ifstream input;
	ofstream output;
	input.open("B-large.in");
	output.open("out.txt");
	int t;
	input >> t;
	for (int i = 1; i <= t; i++){
		string n;
		input >> n;
		string out = n;
		if (out.length() != 1){
			for (int j = out.length() - 2; j >= 0; j--) {
				if (out[j] > out[j + 1]){
					for (int k = j + 1; k < out.length(); k++){
						out[k] = '9';
					}
					out = decrement(out, j);
				}
			}
		}
		while(true){
			if (out[0] == '0'){
				out = out.substr(1);
			}
			else {
				break;
			}
		}
		output <<"Case #" << i << ": " << out << '\n';
	}
	input.close();
	output.close();
}