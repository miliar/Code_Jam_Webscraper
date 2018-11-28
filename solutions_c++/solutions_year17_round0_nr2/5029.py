#include <iostream>
#include <cstdlib>
#include <ctime>
#include <cstring>
using namespace std;


typedef long long ll;

bool isOk(ll num) {

	if(num / 10 == 0) return true;

	while(num > 0) {

		if(num / 10 == 0) return true;

		if(num % 10 < (num % 100) / 10) return false;

		num /= 10;
	}

	return true;
}
ll bruteforce(ll num) {

	for(ll i = num; i>=9; i--) {
		if(isOk(i)) return i;
	}

	return -1;
}

string solve(string num) {
	
	if(num.length() == 1) return num;

	
	for(int i=1; i < num.length(); i++) {
		if(num[i-1] > num[i]) {

			cerr << "Violation between " << num[i-1] << " and " << num[i] << endl;
			for(int j = i - 1; j>=0; j--) {

				char dec = num[j] - 1;
				bool isOk = true;

				for(int k = 0; k < j; k++) {
					if(dec < num[k]) {
						isOk = false;
						cerr << "\t" << dec << " not fine, since it is violating " << num[k] << endl;
						break;
					}
				}
				if(isOk) {
					string sol = "";
					for(int k = 0; k < j; k++) sol += num[k];

					if(dec != '0') sol += dec;

					for(int k = j + 1; k < num.length(); k++) 
						sol += '9';

					return sol;
				}
			}
		}
	}
	return num;
}

int main() {

	/*
	srand(time(NULL));
	ios::sync_with_stdio(false);

	int test_limit;

	cin >> test_limit;
	int num_errors = 0;
	for(int t = 0; t < test_limit; t++ ) {
		ll someNumber = rand() % 10000000000l;

		cerr << "t: " << t << " number: " << someNumber << endl;
		ll sol1 = bruteforce(someNumber);
		string sol1_str = to_string(sol1);
		string sol2 = solve(to_string(someNumber));


		if(strcmp(sol1_str.c_str(), sol2.c_str()) != 0) {
			cout << someNumber << " " << sol1_str << " " << sol2 << endl;
			num_errors += 1;
		}
	}

	if(num_errors == 0) {
		cout << "Everything ok." << endl;
	} else {
		cout << "Number of errors: " << num_errors << endl;
	} */
	

	int T;
	cin >> T;

	string num;
	for(int t=1; t<=T; t++) {
		cin >> num;

		string sol = solve(num);
		cout << "Case #" << t << ": " << sol << "\n";
	}

	return 0;
}