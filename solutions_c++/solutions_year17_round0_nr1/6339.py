#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <fstream>
#include <string>
using namespace std;

void SolveA(ifstream* i, ofstream* o) {
	string states;
	int K;
	*i >> states;
	*i >> K;
	int flips = 0;
	for (int i = 0; i < states.length() - K + 1; i++) {
		if (states[i] == '-') {
			//flip
			flips++;
			for (int j = i; j < i + K; j++) {
				states[j] = states[j] == '-' ? '+' : '-';
			}
		}
	}
	for (int i = states.length() - K; i < states.length(); i++) {
		if (states[i] == '-') {
			*o << "IMPOSSIBLE";
			return;
		}			
	}
	*o << flips;
}
void main() {
	ifstream input = ifstream(fopen("d:\\input.txt", "r"));
	ofstream output = ofstream(fopen("d:\\output.txt", "w"));
	int T;
	input >> T;
	for (int i = 0; i < T; i++) {
		output << "Case #" << (i+1) << ": ";
		SolveA(&input, &output);
		output << endl;
	}		
	//system("pause");
}
