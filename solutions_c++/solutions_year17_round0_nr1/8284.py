#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

const int invalid_number = 1001;

string turn(const string S, const int index, const int K)
{
	// cout << "turn " << S << " " << index << endl;
	string next_S(S);
	for (int i = index; i < (index + K); i++) {
		if (next_S[i] == '+') {
			next_S[i] = '-';
		} else {
			next_S[i] = '+';
		}
	}
	// cout << "next_S " << next_S << endl;

	return next_S;
}

int flip(const string S, const int K)
{
	// cout << "flip " << S << " " << K << " " << endl;

	if (S.find('-') == string::npos) {
		// cout << "already happy." << endl;
		return 0;
	}

	if (S.size() < K) {
		// cout << "no way." << endl;
		return invalid_number;
	}
	
	// cout << "left to right" << endl;
	// cout << "S " << S << endl;
	int min_count = invalid_number;
	for (int i = 0; i <= S.size() - K; i++) {
		const string next_S = turn(S, i, K);
		if (next_S.substr(0, i + 1).find('-') != string::npos)
			continue;

		const int count = flip(next_S.substr(i + 1), K) + 1;
		min_count = min(min_count, count);
		// cout << "min_count " << min_count << endl;
	}

	// cout << "right to left" << endl;
	string reverse_S = "";
	for (auto itr = S.rbegin(); itr != S.rend(); itr++) {
		reverse_S += *itr;
	}
	// cout << "reverse_S " << reverse_S << endl;
	for (int i = 0; i <= reverse_S.size() - K; i++) {
		const string next_S = turn(reverse_S, i, K);
		if (next_S.substr(0, i + 1).find('-') != string::npos)
			continue;

		const int count = flip(next_S.substr(i + 1), K) + 1;
		min_count = min(min_count, count);
		// cout << "min_count " << min_count << endl;
	}
	
	return min_count;
}

int main()
{
	int T;
	cin >> T;
	//// cout << "T:" << T << endl;
	for (int i = 0; i < T; i++) {
		string S;
		int K;
		cin >> S >> K;
		// cout << "S:" << S << endl;
		// cout << "K:" << K << endl;
		
		const int result = flip(S, K);
		string answer = "Case #" + to_string(i + 1) + ": ";
		if (result == invalid_number) {
			answer += "IMPOSSIBLE";
		}
		else {
			answer += to_string(result);
		}
		cout << answer << endl;
	}

    return 0;
}

