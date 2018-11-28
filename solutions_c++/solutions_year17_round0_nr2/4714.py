#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <string>
#include <queue>
#include <map>
#include <algorithm>

using namespace std;

long long getNumber(int digitsCount, int firstDigit) {
	if (digitsCount < 1) return 0;
	if (firstDigit < 0 || firstDigit > 9) return 0;
	if (digitsCount == 1) return 9 - firstDigit + 1;

	static vector<vector<long long>> dynamic(1000, vector<long long>(10, -1));
	if (dynamic[digitsCount - 1][firstDigit - 1] < 0) {
		long long count = 0;
		for (int digit = firstDigit; digit < 10; ++digit) {
			count += getNumber(digitsCount - 1, digit);
		}
		dynamic[digitsCount - 1][firstDigit - 1] = count;
	}
	return dynamic[digitsCount - 1][firstDigit - 1];
}

string solve(long long n) {
	if (n < 10) {
		return to_string(n);
	}

	int digitsCount = 1;
	long long count = 9;
	while (count < n) {
		++digitsCount;
		count += getNumber(digitsCount, 1);
	}

	string answer(digitsCount, '0');

	// long long index = getNumber(digitsCount - 1, 1);
	// long long remaining = n - getNumber(digitsCount - 1, 1);
	int lastDigit = 1;
	long long number = count - getNumber(digitsCount, 1);
	for (int i = 0; i < digitsCount; ++i) {
		for (int digit = lastDigit;; ++digit, ++lastDigit) {
			answer[i] = '0' + digit;
			long long count = getNumber(digitsCount - i - 1, digit);
			if (count == 0) count = 1;
			if (number + count >= n) {
				break;
			}
			else {
				number += count;
			}
		}
	}

	return answer;
}

bool isTidy(long long n) {
	int last = 9;
	while (n) {
		if (n % 10 > last) return false;
		last = n % 10;
		n /= 10;
	}
	return true;
}

long long brute_solve(long long n) {
	int index = 0;
	for (long long number = 1; ;++number) {
		if (isTidy(number)) {
			++index;
			// cerr << index << ": " << number << endl;
			if (index == n) {
				return number;
			}
		}
	}
}

long long solve2(long long n) {
	vector<int> answer;
	int lastDigit = 9;
	while (n) {
		int digit = n % 10;
		n /= 10;
		if (digit > lastDigit) {
			for (int &d : answer) {
				d = 9;
			}
			--digit;
		}
		answer.push_back(digit);
		lastDigit = digit;
	}

	while (answer.size() && answer.back() == 0) {
		answer.pop_back();
	}

	reverse(answer.begin(), answer.end());
	long long answerLong = 0;
	for (int d : answer) {
		answerLong = answerLong * 10 + d;
	}
	return answerLong;
}

int main(int argc, char* argv[])
{
	srand(13);
	ios_base::sync_with_stdio(false);

	//cerr << getNumber(410, 1) << endl;
	//cerr << solve(1000000000000000000L).size() << endl;
	//
	//// return 0;

	//int index = 0;
	//for (long long number = 1;; ++number) {
	//	if (isTidy(number)) {
	//		++index;
	//		string answer = solve(index);
	//		cerr << index << ": " << answer << endl;
	//		if (to_string(number) != answer) {
	//			return 1;
	//		}
	//	}
	//}

	//for (long long n = 1; n <= 1000000000000000000L; ++n) {
	//	string answer = solve(n);
	//	string correctAnswer = to_string(brute_solve(n));
	//	cerr << n << ": " << answer << endl;
	//	if (answer != correctAnswer) {
	//		return 1;
	//	}
	//}

	//for (int i = 1; i < 100; ++i) {
	//	cerr << i << ": " << solve(i) << endl;
	//}

	//// cerr << solve(10) << endl;
	//// cerr << brute_solve(1000000000000000000L) << endl;

	//return 0;

	//long long last = -1;
	//for (long long number = 1;; ++number) {		
	//	if (isTidy(number)) {
	//		last = number;
	//	}
	//	cerr << number << endl;
	//	if (solve2(number) != last) {
	//		return 1;
	//	}
	//}

	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int T;
	cin >> T;
	for (int test = 1; test <= T; ++test) {
		long long n;
		cin >> n;
		cout << "Case #" << test << ": " << solve2(n) << '\n';
	}

	return 0;
}

