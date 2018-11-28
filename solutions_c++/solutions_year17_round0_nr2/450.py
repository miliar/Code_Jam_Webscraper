#include<iostream>
#include<algorithm>
#include<math.h>
#include<string.h>
using namespace std;
int lengthOfNumber(long long int input) {
	int length = 1;
	while (input != 0) {
		input /= 10;
		if (input != 0) length += 1;
	}
	return length;
}
int numberAtN(long long int input, int length, int pos) {
	int newpos = length - pos;
	long long int div = 1;
	while (newpos != 0)
	{
		div *= 10;
		newpos -= 1;
	}
	long long int no = input / div;
	return no % 10;
}
long long int findTidyNumber(long long int input) {
	int length = lengthOfNumber(input), currPos = 1;
	long long int output = 0;
	if (length == 1)
		return input;
	while (true)
	{
		int precDigit = numberAtN(input, length, currPos);
		int currDigit = numberAtN(input, length, currPos + 1);
		if (precDigit < currDigit) {
			output += precDigit;
			output *= 10;
			currPos += 1;
			if (currPos == length) {
				output += numberAtN(input, length, currPos);
				return output;
			}
		}
		else if (precDigit == currDigit) {
			int newpos = currPos, count = 0, precDigitN, currDigitN;
			while (newpos < length) {
				precDigitN = numberAtN(input, length, newpos);
				currDigitN = numberAtN(input, length, newpos + 1);
				newpos += 1;
				if (precDigitN != currDigitN) break;
			}
			if (precDigitN == currDigitN) {
				output += precDigit;
				int mul = length - currPos;
				while (mul != 0)
				{
					output *= 10;
					output += precDigitN;
					mul -= 1;
				}
				return output;
			}
			else if (precDigitN < currDigitN) {
				int mul = newpos - currPos - 1;
				while (mul != 0)
				{
					output += precDigit;
					output *= 10;
					mul -= 1;
				}
				currPos = newpos - 1;
			}
			else {
				output += precDigit;
				int mul = length - currPos;
				while (mul != 0)
				{
					output *= 10;
					mul -= 1;
				}
				output = output - 1;
				return output;
			}
		}
		else
		{
			output += precDigit;
			int mul = length - currPos;
			while (mul != 0)
			{
				output *= 10;
				mul -= 1;
			}
			output = output -  1;
			break;
		}
	}
	return output;
}
int main() {
	int NoOfTestCases;
	cin >> NoOfTestCases;
	for (int i = 0; i < NoOfTestCases; i++) {
		long long int input;
		cin >> input;
		cout << "Case #" << i + 1 << ": " << findTidyNumber(input) << endl;
	}
	return 0;
}