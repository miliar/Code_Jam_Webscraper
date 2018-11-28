
#include <iostream>
#include <string>
using namespace std;

void changeNum(string &s, int loc) {
	s[loc] -= 1;
	for (int k = loc + 1; k < s.length(); k++) {
		s[k] = '9';
	}
}

int main() {
	int t;
	long long n;
	cin >> t;
	for (int j = 1; j <= t; j++) {
		cin >> n;
		string num = to_string(n);
		int loc = 0;
		int count = 0;
		for (int i = 0; i < num.length() - 1; i++) {
			if (num[i] == num[i + 1]) 
				count++;
			
			if (num[i] != num[i + 1]) {
				loc = i;
				int m = i + 1;
				if (m > 1) {
					if (num[m - 1] == num[m - 2])
						loc = loc - count;
				}
				count = 0;
			}
					
			if (num[i] > num[i + 1]) {
				changeNum(num, loc);
				break;
			}
		}
		if (num[0] == '0'){
			num[0] = 32;
			cout << "Case #" << j << ":" << num << endl;
		}
		else
			cout << "Case #" << j << ": " << num << endl;
	}
	return 0;
}
