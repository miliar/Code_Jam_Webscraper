// Example program
#include <iostream>
#include <string>
#include <vector>

using namespace std;


int sub(vector<int> & num, int index) {
	num[index] = num[index] - 1;
	if (num[index] == -1) {
		num[index] = 9;
		return sub(num, index - 1);
	}
	return index;
}

int main() {
	int t;
	cin >> t;
	for (int x = 0; x < t; x++) {
		string input;
		cin >> input;
		vector<int> num;
		for (int i = 0; i < input.length(); i++) {
			num.push_back(input[i] - '0');
		}

		int i = num.size() - 1;
		while ( i > 0 ) {
			if (num[i-1] > num[i]) { // ...52... for exmaple
				for (int j = i; j < num.size(); j++) {
					num[j] = 9;
				}
				i = sub(num, i - 1) + 1;
			}
			i--;
		}

		int startIndex = 0;
		for (int i = 0; i < num.size(); i++) {
			if (num[i] != 0) {
				startIndex = i;
				break;
			}
		}
		cout << "Case #" << (x+1) << ": ";
		for (int i = startIndex; i < num.size(); i++) {
			cout << num[i];
		}
		cout << endl;
	}
}

