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
		int r, c;
		input >> r >> c;
		char** cake = new char*[r];
		char prevChar = ' ';
		bool firstCharMet = false;
		int firstQuestionMark = -1;
		for (int j = 0; j < r; j++){
			cake[j] = new char[c];
		}

		for (int j = 0; j < r; j++){
			prevChar = ' ';
			firstQuestionMark = -1;
			for (int k = 0; k < c; k++){
				input >> cake[j][k];
				if (cake[j][k] != '?'){
					firstCharMet = true;
					prevChar = cake[j][k];
					if (firstQuestionMark != -1){
						for (int l = firstQuestionMark; l < k; l++){
							cake[j][l] = prevChar;
						}
						firstQuestionMark = -1;
					}
				}
				else if (prevChar != ' '){
					cake[j][k] = prevChar;
				}
				else if (k + 1 == c && firstCharMet){
					for (int l = 0; l < c; l++){
						cake[j][l] = cake[j - 1][l];
					}
				}
				else if (firstQuestionMark == -1) {
					firstQuestionMark = k;
				}
			}
		}

		for (int j = r-1; j >= 0; j--){
			if (cake[j][0] == '?'){
				for (int j1 = 0; j1 <= j; j1++){
					for (int k = 0; k < c; k++){
						cake[j1][k] = cake[j+1][k];
					}
				}
				break;
			}
		}

		output << "Case #" << i << ": " << '\n';
		for (int j = 0; j < r; j++){
			for (int k = 0; k < c; k++){
				output << cake[j][k];
			}
			output << '\n';
		}
		for (int j = 0; j < r; j++){
			delete cake[j];
		}
		delete cake;
	}
	input.close();
	output.close();
}