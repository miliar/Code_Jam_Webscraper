#include <iostream>
#include <cstdlib>
#include <deque>

using namespace std;

deque<char> getDigits(long long N)
{
	deque<char> ans;
	while (N > 0) {
		ans.push_front(N % 10);
		N /= 10;
	}
	return ans;
}

deque<char> getTidy(deque<char> digits)
{
	int numDigits = digits.size();
	int problem;
	for (problem = 1; problem < numDigits; problem++) {
		if (digits[problem - 1] > digits[problem])
			break;
	}
	if (problem == numDigits)
		return digits;

	while (digits[problem - 1] > digits[problem]) {
		digits[problem - 1]--;
		problem--;
		if (problem == 0)
			break;
	}

	deque<char> ans;
	if (digits[0] > 0) {
		ans.push_back(digits[0]);
	}
	for (int i = 1; i <= problem; i++) {
		ans.push_back(digits[i]);
	}
	for (int i = problem + 1; i < numDigits; i++) {
		ans.push_back(9);
	}
	return ans;
}

int main()
{
	int T;
	cin >> T;
	for (int t = 0; t < T; t++) {
		long long N;
		cin >> N;
		deque<char> ans = getTidy(getDigits(N));
		cout << "Case #" << t+1 << ": ";
		for (char d : ans) {
			cout << (int)d;
		}
		cout << endl;
	}
}