// PancakeFlipper.cpp : Defines the entry point for the console application.
//



#include "stdafx.h"
#include <iostream>
#include <string>

using namespace std;

bool allFlipped(char* cArr) {
	int charIndex =0;
	while (*(cArr + charIndex) == '+') charIndex++;

	if (*(cArr + charIndex) == '-') return false;
	else return true;
}

int pancakeFlipper(char* cArr, int size) {

	int flipCount = 0;
	int outofBoundFlag = 0;
	while (!allFlipped(cArr)) {
		
		int charIndex = 0;
		while (*(cArr + charIndex) == '+') {
			charIndex++;
		}
		// find the first pancake needed to be flipped
		if ((*(cArr + charIndex + size -1) != '+' && *(cArr + charIndex + size -1) != '-')) {
			outofBoundFlag = 1;
			break;
		}
		int flipIndex = 0;
		while (flipIndex < size) {
			if (*(cArr + charIndex + flipIndex) == '-') *(cArr + charIndex + flipIndex) = '+';
			else *(cArr + charIndex + flipIndex) = '-';
			flipIndex++;
			flipCount++;
		}


	}

	flipCount /= size;

	if (outofBoundFlag) return -1;
	return flipCount;
}


int main()
{
	int testNum;
	cin >> testNum;

	for (int index = 0; index < testNum; index++) {
		string str;
		cin >> str;
		int size;
		cin >> size;
		const char* cstr = str.c_str();
		char* cArr = new char[str.length() + 1];
		strcpy(cArr, str.c_str());
		int output = pancakeFlipper(cArr, size);
		if (output == -1)
			cout << "Case #" << index + 1 << ": IMPOSSIBLE\n";
		else
			cout << "Case #" << index + 1 << ": " << output << "\n";
	}

    return 0;
}

