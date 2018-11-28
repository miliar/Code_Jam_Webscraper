#include <iostream>
using namespace std;

int main() {
	int t;
	cin >> t;
	for(int i = 1; i <= t; i++) {
		long long n;
		cin >> n;
		string s = to_string(n);
		for(int i = 0; i < s.length() - 1; i++) {
			if(s[i] > s[i+1]) {
				int idx = -1;
				for(int j = i; j >= 0; j--) {
					if(s[j] == s[i])
						idx = j;
					else
						break;
				}
				s[idx] -= 1;
				for(int j = idx+1; j < s.length(); j++)
					s[j] = '9';
				break;
			}
		}
		cout << "Case #" <<  i <<  ": " << stoll(s) << endl;
	}
}
