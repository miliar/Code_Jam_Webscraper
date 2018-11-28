#include <iostream>
#include <string>

using namespace std;

long long int get_tidy(long long int n) {
	
	if (n < 10) {
		return n;
	}
	
	string s = to_string(n);
	string t = "";
	for (int i = 0; i < s.length(); i++) {
		t += "9";
	}

	for (int i = 0; i < s.length() - 1; i++) {
		int p = s[i] - '0';
		int q = s[i+1] - '0';

		if (p <= q) {
			t[i] = s[i];
			if (i+2 == s.length()) {
				t[i+1] = s[i+1];
			}
		} else {
			int j = i;
			while((j >= 0) && (s[j] == s[i]))  {
				j--;
			}
			t[j+1] = (p-1+'0');
			for (int k = j+2; k < s.length(); k++) {
				t[k] = '9';
			}
			break;
		}
	}

	return stoll(t);
}

bool is_tidy(long long int n) {
	string s = to_string(n);
	for (int i = 0 ; i < s.length()-1; i++) {
		int p = s[i] - '0';
		int q = s[i+1] - '0';
		if (p > q) {
			return false;
		} 
	}
	return true;
}

int main() {
	
	int t;
	long long int *A;
	cin >> t;
	A = new long long int[t];
	for (int i = 0; i < t; i++) {
		cin >> A[i];
	}

	for (int i = 0; i < t; i++) {
		long long int tidy = get_tidy(A[i]);
		if (is_tidy(tidy)) {
			cout << "Case #" << i+1 << ": " << tidy << endl; 

		} else {
			cout << "not tidy!!!!!!!!!" << endl;
		}
	}
}