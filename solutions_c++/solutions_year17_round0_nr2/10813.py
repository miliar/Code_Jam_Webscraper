#include <iostream> 
#include <cmath>
using namespace std;

int evaluateLastDigit(int number) {
	return number%10;
}

bool lastDigitsInAscendingOrder(int number) {
	int digit1 = evaluateLastDigit(number);
	int digit2 = evaluateLastDigit(number/10);
	return digit1 >= digit2;
}

int lengthOfNumber(int number) {
	int count = 1;
	while(number/10 != 0) {
		number = number/10;
		count++;
	}
	return count;
}

int largestAscendingNumber(int number) {
	int num = number;

	while(num/10 > 0) {
		while(num/10>0 && lastDigitsInAscendingOrder(num)) {
			num = num/10;
		}

		if (!lastDigitsInAscendingOrder(num)) {
			int digitNumberNotInOrder = lengthOfNumber(num) - 1 ;
			int remainingDigits = lengthOfNumber(number) - digitNumberNotInOrder;
			int power = pow(10, remainingDigits);
			number = number - (number % power) -1;																																																																																
			num = number/pow(10, remainingDigits);
		}	
	}
	return number;
}

int main(int argc, char *argv[]) {

	int numberOfTestCases;
	int *results = new int[numberOfTestCases]; 

	cin>>numberOfTestCases;

	for(int i = 0; i <numberOfTestCases; i++) {

		int number;
		cin>>number;
		results[i] = largestAscendingNumber(number);
	}

	for(int i = 0; i < numberOfTestCases; i++) {
		cout<<"Case #"<<i+1<<": "<<results[i]<<endl;
	}	

	return 0;
}