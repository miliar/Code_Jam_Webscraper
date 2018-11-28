#include <iostream>
#include <string>
#include <vector>
using namespace std;

class A {
public:
	string flip(string S, int K) {
		vector<int> cakes;
		int count = 0;
		for (char s : S) {
			if (s == '+') cakes.push_back(1);
			if (s == '-') cakes.push_back(-1);
		}
		for (int i = 0; i <= cakes.size() - K; i++) {
			if (cakes[i] < 0) {
				for (int j = i; j < i + K; j++) {
					cakes[j] = -cakes[j];
				}
				count++;
			}
		}
		for (int i = cakes.size() - K + 1; i < cakes.size(); i++) {
			if (cakes[i] < 0) return "IMPOSSIBLE";
		}
		return to_string(count);
	}
};

int main() {
	int t, K;
	string S;
	A A1;
	cin >> t;
	for (int i = 1; i <= t; i++) {
		cin >> S >> K;
		cout << "Case #" << i << ": " << A1.flip(S, K) << endl;
	}
}
