#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

typedef long long int ll;

//#define DEBUG 1

using namespace std;

template <class Type>
void output(const vector<Type>& v) {
	cout << "Print: ";
	for(int i = 0; i < v.size(); i++) {
		cout << v[i] << " ";
	}
	cout << endl;
}

bool isTidy(ll number, ll last_digit) {
	string s = to_string(number) + to_string(last_digit);
	for(int i = 0; i < s.size() - 1; i++) {
		if(s[i] > s[i+1]) return false;
	}
	return true;
}

string recursiveSolve(ll k, ll last_digit) {
	if(k==0) return "";
	if(isTidy(k, last_digit)) return to_string(k);
	k = (k / 10) * 10 - 1;
	ll suffix = k % 10;
	ll prefix = k / 10;
	return recursiveSolve(prefix, min(last_digit, suffix)) + to_string(suffix);
}

string solve(ll k) {
	return recursiveSolve(k, 9);
}

int main() {
	int T;
	cin >> T;
	for(int cas=1; cas <=T; cas++) {
		string pancakes;
		ll k;
		cin >> k;
		cout << "Case #" << cas << ": " << solve(k) << endl;
	}
	return 0;
}
