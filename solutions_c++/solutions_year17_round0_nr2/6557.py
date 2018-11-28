#include <iostream>
#include <vector>
using namespace std;
void printDigits(vector<int> digits) {
	for (int i = digits.size() -1; i >= 0; --i) {
		cout << digits[i] << " " ;
	}
	cout << endl;
}


std::vector<int> digitize(long int num) {
	std::vector<int> digits;
	while (num) {
		digits.push_back(num % 10);
		num = num / 10;
	}

/*
	cout << "after digitize: ";
	printDigits(digits);
	cout << endl;*/


	return digits;
}



long int reconstruct(std::vector<int> digits) {
	long int num = 0;
	int multiplier = 1;
	for (int i = 0; i < digits.size(); ++i) {
		num += digits[i] * multiplier;
		multiplier *= 10;
	}

	return num;
}

bool isTidy(long int num) {
	vector<int> digits = digitize(num);
	for (int i = 0; i < digits.size() - 1; ++i) {
		if (digits[i] < digits[i+1]) {
			return false;
		}
	}
	return true;
}

long int largestTidyNum(long int num)
{
	while(num > 0) {
		if (isTidy(num)) {
			return num;
		}
		num --;
	}
	return num;
	/*
	std::vector<int> digits = digitize(num);
	for (int i = 0; i < digits.size(); ++i) {
		if (digits[i] < digits[i+1]) {
			digits[i] = 9;
			digits[i+1] -= 1;
		}
		printDigits(digits);
	}
	return reconstruct(digits);*/

}

int main() {
	int N;
	std::cin >> N;

	for (int i = 0; i < N; ++i) {
		long int num;
		std::cin >> num;

		long int tidyNum = largestTidyNum(num);

		std::cout << "Case #" << i + 1 << ": " << tidyNum << std::endl;
	}
	return 0;

}