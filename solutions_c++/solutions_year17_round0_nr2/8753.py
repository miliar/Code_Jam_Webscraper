#include<iostream>
#include<string>
using namespace std;

#define MAX_LENGTH 20


const char* trim(string N) {
	const char* pos = N.c_str();
	for (size_t i = 0 ; i < N.size() ; i++) {
		if (pos[i] != '0') {
			return pos + i;
		}
	}
	return pos;
}

int not_tidy(string N) {
	size_t i;
	for (i = N.size() - 1 ; i >= 1 ; i--) {
		if (N[i - 1] > N[i]) {
			return i;
		}
	}
	return i;
}

bool backoff(string& N, size_t digit) {
	// clear out
	if (0 == digit) {
		return false;
	}
	if (N[digit - 1] > '0') {
		N[digit - 1]--;
	} else if (!backoff(N, digit - 1)) {
		return false;
	}

	for (size_t i = digit; i < N.size() ; i++){
		N[i] = '9';
	}
	return true;
}

string solve(string N) {
	for (size_t i = N.size() - 1 ; i >= 1; i--) {
		if (N[i - 1] > N[i]) {
			backoff(N, i);
		}
	}
	return N;
}

int main () {
	size_t cases;
	cin >> cases;
	for (size_t i = 1 ; i <= cases ; i++) {
		string N;
		cin >> N;

		// output
		cout << "Case #" << i << ": " << trim(solve(N)) << endl;
	}
}
