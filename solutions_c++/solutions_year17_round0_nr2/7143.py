#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <vector>
#include <unordered_set>

using namespace std;

#define DEBUG 1
typedef long long ll;

fstream fin("largeB.in");
fstream fout("largeB.out");

ll toll(const string& s){
	istringstream ss(s);
	ll ret;
	ss >> ret;
	return ret;
}

void replace(string& s, const int& pos) {
	for (int i = pos + 1; i<s.length(); ++i) {
		s[i] = s[pos];
	}
}

void rec(string& s, const string& N, const int& pos) {
	if (pos == N.length()) {
		return;
	}
	while (toll(s) <= toll(N)) {
		if (s[pos] == '9'){
			break;
		}
		s[pos]++;
		replace(s, pos);
	}
	if (toll(s) > toll(N)){
		s[pos]--;
		replace(s, pos);
	}

	rec(s, N, pos + 1);
}

ll alg(string N) {
	string s(N.length(), '1');
	if (s > N) {
		return toll(string(N.length() - 1, '9'));
	}
	if (s == N) {
		return toll(s);
	}
	rec(s, N, 0);
	return toll(s);
}

bool check(ll n) {
	vector<int> d;
	while (n != 0) {
		if (n%10 == 0) {
			return false;
		}
		d.push_back(n%10);
		n /= 10;
	}

	for (unsigned int i = 0; i<d.size() - 1; ++i) {
		if (d[i] < d[i+1]){
			return false;
		}
	}

	return true;
}


void f_main(const int& testCase) {
	string s;
	fin >> s;

	ll res = alg(s);

	if (DEBUG) {
		cout << "Case #" << testCase << ": " << res << endl;
	}
	fout << "Case #" << testCase << ": " << res << endl;
}


int main() {

	int T;
	fin >> T;
	for (int t=0; t < T; ++t) {
		f_main(t+1);
	}
	return 0;
}
