#include <bits/stdc++.h>

#define pb push_back
#define f first
#define s second
#define pii pair<int, int>
#define mp make_pair
 
using namespace std;
 
const string name = "B",
             in_file = name + ".in",
             out_file = name + ".out";
 
ifstream fin(in_file);
ofstream fout(out_file);

void decrease(string& number, int pos) {
	if (number[pos] != '0') {
		number[pos]--;
		return;
	}

	number[pos] = '9';
	decrease(number, pos - 1);
} 

string remove_leading_zeros(string& number) {
	string result = "";
	bool not_zero = false;
	for (char digit : number) {
		if (not_zero || digit != '0') {
			result += digit;
			not_zero = true;
		}
	}
	return result;
}

string solve(string& number) {
	for (int i = number.size() - 1; i > 0; i--) {
		if (number[i - 1] > number[i]) {
			for (int j = i; j < (int)number.size(); j++) {
				number[j] = '9'; 
			}
			decrease(number, i - 1);
		}
	}
	return remove_leading_zeros(number);
} 

int main() {
	int t;
	fin >> t;

	for (int test = 1; test <= t; test++) {
		string number;
		fin >> number;
		fout << "Case #" << test << ": " << solve(number) << '\n';
	}
	return 0;
}