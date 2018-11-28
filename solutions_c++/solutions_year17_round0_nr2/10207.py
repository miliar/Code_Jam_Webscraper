#include <iostream>
#include <string>
#include <map>
#include <queue>

using namespace std;

bool tidy(long int num);

int last_tidy(long int num);

int main() {

	int t;

	long int num;

	cin >> t;


	for (int i = 0; i < t; ++i) {
		
		cin >> num;

		
		cout << "Case #" << (i + 1) << ": "<< last_tidy(num)<< endl;
		
	}

	return 0;
}

bool tidy(long int num) {

	int current = num % 10;

	while (num > 0) {

		int d = num % 10;

		if (d > current)
			return false;

		current = d;

		num /= 10;
	}

	return true;
}

int last_tidy(long int num) {
	
	while (!tidy(num)) {

		--num;
	}

	return num;
}