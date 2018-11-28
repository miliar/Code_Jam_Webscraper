// TidyNumber.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
using namespace std;

bool checkValid(long long input) {

	while (input > 0) {
		long long temp = input / 10;
		if (temp % 10 > input % 10) {
			return false;
		}
		input = temp;
	}

	return true;
}

int* getDigit(long long input, int* output) {
	long long temp = input;
	int index = 0;
	int array[20];
	while (temp > 0) {
		array[index] = temp % 10;
		index++;
		temp /= 10;

	}
	int outputIndex = 0;
	while (index > 0) {
		*(output + outputIndex) = array[index - 1];
		index--;
		outputIndex++;

	}

	return output;
}




long long tidyNumber(long long input) {
	long long temp = input;
	int length = 0;
	while (temp > 0) {
		temp /= 10;
		length++;
	}
	temp = input;

	while (!checkValid(temp)) {
		int Null[20];
		int* array = getDigit(temp, Null);
		int index = 0;
		while (*(array + index) < *(array + index + 1)) {
			index++;
		}
		// find the first digit where the conflict exists
		
		while (index < (length - 1)) {
			(*(array + index + 1)) = 0;
			index++;
		}

		long long arrayInt = 0;
		index = 0;
		while (index < length) {
			arrayInt += *(array + index);
			arrayInt *= 10;
			index++;
		}
		temp = arrayInt / 10 - 1;

	}

	return temp;
	


}

int main()
{
	
	int testNum;
	cin >> testNum;
	int output[20];
	for (int index = 0; index < testNum; index++) {
		long long input;
		cin >> input;
		long long output = tidyNumber(input);
		//int* result = getDigit(input, output);
		cout << "Case #" << (index + 1) << ": " << output << "\n";
	}

    return 0;
}

