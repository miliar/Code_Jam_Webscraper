#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <fstream>
#include <string>
using namespace std;

bool isTiny(string number) {
	for (int i = 0; i < number.length() - 1; i++)
		if (number[i] > number[i + 1])
			return false;
	return true;
}

void SolveA(ifstream* i, ofstream* o) {
	string number;
	*i >> number;
	do {
		for (int i = 0; i < number.length() - 1; i++)
			if (number[i] > number[i + 1])
			{
				//big tiny point
				//decrease this and any others
				for (int k = i; k >= 0; k--) {
					number[k]--;
					if (number[k] == 47)
						number[k] = '9';
					else
						break;
				}
				for (int k = i + 1; k < number.length(); k++)
				{
					number[k] = '9';
				}
				break;
			}
	} while (!isTiny(number));



	
	//print
	bool isStarted = false;
	for (int i = 0; i < number.length(); i++) {
		if (number[i] != 48)
			isStarted = true;
		if (isStarted)
			*o << number[i];
	}
}

void main() {
	ifstream input = ifstream(fopen("d:\\input.txt", "r"));
	ofstream output = ofstream(fopen("d:\\output.txt", "w"));
	int T;
	input >> T;
	for (int i = 0; i < T; i++) {
		output << "Case #" << (i + 1) << ": ";
		SolveA(&input, &output);
		output << endl;
	}
	//system("pause");
}
