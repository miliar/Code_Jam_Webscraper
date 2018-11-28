#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>
#include <cmath>

using namespace std;

int counter = 1;
unsigned long Integer = 0;

vector<int> splitToDigits(long tempInt, vector<int> digits)
{
	while(tempInt >= 10){
		digits.push_back(tempInt%10);
		tempInt /= 10;
	}
	digits.push_back(tempInt);
	reverse(digits.begin(), digits.end());
	
	return digits;
}

vector<int> fillNines(vector<int> digits, unsigned int index)
{
	while(index < digits.size()){
		digits[index] = 9;
		index++;
	}
	return digits;
}

long convertVect(vector<int> digits, unsigned int end)
{
	unsigned long finalInt = 0;

	if(digits[0] != 0){
		long temp = pow(10, end);
		finalInt += digits[0] * temp;
	}
	end--;

	for(unsigned int i = 1; i < digits.size(); i++)
	{
		long exp = pow(10, end);
		finalInt += digits[i] * exp;
		end--;
	}
	return finalInt;
}

long masterSwitch()
{
	vector<int> digits;	
	unsigned long tempInt = Integer;
	digits = splitToDigits(tempInt, digits);

	unsigned int end = digits.size() - 1;
	unsigned int index = end;
	while(index > 0){

		if(digits[index] >= digits[index-1] && digits[index-1] > 0){

		}else if(index-1 == 0 && digits[index-1] <= 1){
			digits = fillNines(digits, index);
			digits[index-1] = 0;
		}else if(index-1 == 0){
			digits = fillNines(digits, index);
			digits[index-1] -= 1;	
		}else if(digits[index-1] == 0){
			digits = fillNines(digits, index);
		}else{
			digits[index-1] -= 1;
			digits[index] = 9;
		}
		index--;	
	}
	
	return convertVect(digits, end);
}

void output(long masterInt)
{	
	string oString;

	oString = "Case #" + to_string(counter) + ": " + to_string(masterInt);
	cout << oString << '\n';
}

int main(int argc, char* argv[])
{
	// Gets T value
	int T;
	cin >> T;
	
	while(counter <= T){
		
		cin >> Integer;

		// finding our int
		output(masterSwitch());
			
		counter++;
	}
	counter--;

	return 0;
}
