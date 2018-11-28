#include <iostream>
#include <string>
#include <stack>
#include <queue>
#include <map>
#include <utility>

typedef unsigned long long ull;

using namespace std;

void SolveA(string s, int K) {
	int ans = 0;
	for (int i = 0; i < s.length() - K + 1; ++i) {
		if (s[i] == '-') {
			++ans;
			for (int j = i; j < i + K; ++j) {
				s[j] = s[j] == '-' ? '+' : '-';
			}
		}
	}
	if (s.find('-') != string::npos) {
		cout << "IMPOSSIBLE";
		return;
	}

	cout << ans;
}

void SolveB(string s) {
	for (int i = s.length() -1; i > 0; --i) {
		char prev = s[i - 1];
		char curr = s[i];
		if (curr < prev) {
			s[i - 1] = s[i - 1] - 1;
			for (int j = i; j < s.length(); ++j) {
				s[j] = '9';
			}
		}
	}
	cout << s.substr(s.find_first_not_of('0'));
}

void SolveC(ull N, ull K) {
	map<ull, ull> S;
	S[N] = 1;
	ull m = 0;
	ull M = 0;
	while (K > 0) {
		auto x = *(S.rbegin());
		K -= min(K, x.second);
		S.erase(x.first);
		if (x.first % 2 != 0) {
			m = (x.first - 1) >> 1;
			M = m;
			S[m] += (x.second << 1);
		}
		else {
			M = x.first >> 1;
			m = (x.first - 2) >> 1;
			S[M] += x.second;
			S[m] += x.second;
		}
	}
	cout << M << ' ' << m;
}

void main() {
	int T;
	cin >> T;
	for (int i = 0; i < T; ++i) {
		ull N;
		cin >> N;
		ull K;
		cin >> K;
		cout << "Case #" << i + 1 << ": ";
		SolveC(N, K);
		cout << endl;
	}
}