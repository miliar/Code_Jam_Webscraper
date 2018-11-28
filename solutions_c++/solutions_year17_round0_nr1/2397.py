// CodeJam.cpp : Defines the entry point for the console application.
//
#include <iostream>
#include <string>

using namespace std;

void flip(string & s, int start, int count)
{
	for (int i = 0; i < count; ++i) {
		if (s[start + i] == '-') {
			s[start + i] = '+';
		}
		else {
			s[start + i] = '-';
		}
	}
}

int main()
{
	int t, k, result, s_st;
	string s;
	cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
	for (int i = 1; i <= t; ++i) {
		result = 0;
		cin >> s >> k;
		for (s_st = 0; s_st < s.size() - k+1; ++s_st) {
			if (s[s_st] == '-') {
				flip(s, s_st, k);
				result++;
			}
		}
		bool success = true;
		for (s_st; s_st < s.size(); ++s_st){
			if (s[s_st] == '-') {
				success = false;
				break;
			}
		}
		if (success) {
			cout << "Case #" << i << ": " << result << endl;
		}
		else {
			cout << "Case #" << i << ": " << "IMPOSSIBLE" << endl;
		}
	}
	cin >> t;
	return 0;
}

