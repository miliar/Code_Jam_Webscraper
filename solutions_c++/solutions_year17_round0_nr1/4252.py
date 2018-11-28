#include <iostream> 
#include <string>
using namespace std;



void flip_next_k(string &s, int k, int i) {
	for (int j = 0; j < k; ++j) {
		if (s[i+j] == '+') s[i+j] = '-';
		else s[i+j] = '+';
	}
}


bool next_k_positive(string &s, int k, int i) {
	for (int j = i; j < s.size(); ++j) {
		if (s[j] == '-') return false;
	}
	return true;
}
	

void number_flips(string s, int k) {
	int i = 0;
	int nflips = 0;
	for (int i = 0; i <= s.size() - k; ++i) {
		if (s[i] == '-') {
			flip_next_k(s,k,i);
			++nflips;
		}
	}
	if (next_k_positive(s,k,i)) cout << nflips << endl;
	else cout << "IMPOSSIBLE" << endl;
}


int main() {
	int t, k;
	string s;
	cin >> t;
	for (int i = 1; i <= t; ++i) {
		cout << "Case #" << i << ": ";
		cin >> s;
		cin >> k;
		number_flips(s,k);
	}
}
