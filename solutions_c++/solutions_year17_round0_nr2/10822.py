#include <iostream>
#include <vector>
#include <sstream>
#include <string>
#include <algorithm>

using namespace std;

void printArray(int arr[], int size) {
	for (int i = 0; i < size; i++) {
		if (arr[i] != 0) {
			cout << arr[i];
		}
	}
	cout << endl;
}

bool isAscending(int arr[], int size) {
	for (int i = 0; i < size - 1; i++) {
		if (arr[i] > arr[i + 1]) {
			return false;
		}
	}
	return true;
}

vector<int> convertToVector(long long m) {
	std::vector<int> digits;

	while (m)
	{
		digits.push_back(m % 10);

		m /= 10;
	}
	reverse(digits.begin(), digits.end());
	return digits;
}

int main() {
	int T;
	cin >> T;
	for (int i = 0; i < T; i++) {
		long long N;
		cin >> N;
		vector<int> res = convertToVector(N);
		int *thearray = &res[0];
		if (isAscending(thearray, res.size())) {
			cout << "Case #" << i + 1 << ": " << N << endl;
		}
		else {
			for (int k = res.size() - 1; k >= 0; k--) {	
				if (k == res.size() - 1) {
					res[k] = 9;
					res[k - 1] = res[k - 1] - 1;
				}
				else if (k > 0) {
					if (res[k - 1] > res[k]) {
						res[k] = 9;
						res[k - 1] = res[k - 1] - 1;
					}
				}
			}
			int *thearray = &res[0];
			cout << "Case #" << i + 1 << ": ";
			printArray(thearray, res.size());
		}
	}
	return 0;
}

