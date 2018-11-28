#include <bits/stdc++.h>
using namespace std;

int T;
long long N, ans;

bool is_tidy(long long N)
{
	int last = 10;
	while (N) {
		int digit = N%10;
		N /= 10;
		if (digit > last) return false;
		last = digit;
	}
	return true;
}

long long naive(long long N)
{
	while (!is_tidy(N)) N--;
	return N;
}

long long fast(long long N)
{
	string s("000" + to_string(N));
	bool decr_next = false;
	for (int i = s.length()-2; i>0; i--)
		if (s[i] > s[i + 1] || decr_next) {
			for (int j=i+1; j<s.length(); j++)
				s[j] = '9';
			if (s[i] == '0') {
				s[i] = '9';
				decr_next = true;
			}
			else {
				s[i] = s[i] - 1;
				decr_next = false;
			}
		}
	return _atoi64(s.c_str());
}

int main() 
{
	/*
	for (int i=1; i<100000; i++)
		if (naive(i) != fast(i))
			cout << i << endl;
	*/

	cin >> T;
	for (int t=1; t<=T; t++) {
		cin >> N;
		ans = fast(N);
		cout << "Case #" << t << ": " << ans << endl;
	}
}
