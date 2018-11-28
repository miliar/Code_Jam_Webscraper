#include <iostream>
#include <vector>

using namespace std;


int solve(string s, int k) {
	
	int counter = 0;
	for(int i=0; i<s.length() - k + 1; i++) {

		if(s[i] == '-') {
			counter += 1;
			for(int j = i; j < i + k; j++) {
				if(s[j] == '-') {
					s[j] = '+';
				} else {
					s[j] = '-';
				}
			}
		}
	}

	for(int i=0; i<s.length(); i++) {
		if(s[i] == '-') return -1;
	}

	return counter;
}

int main() {
	ios::sync_with_stdio(false);

	int T;
	cin >> T;

	string s;
	int K;
	for(int t=1; t<=T; t++) {

		cin >> s >> K;

		int result = solve(s, K);
		if(result != -1)
			cout << "Case #" << t << ": " << result << "\n";
		else
			cout << "Case #" << t << ": IMPOSSIBLE\n";
	}

	return 0;
}