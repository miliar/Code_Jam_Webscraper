#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <string>
using namespace std;

using ll = long long;

ll const INF = 1000000000;



int main(void) {

	ios::sync_with_stdio(false);

	ifstream cin("input.txt");
	ofstream cout("output.txt");

	int T;
	cin >> T;

	for (int test = 1; test <= T; test++) {

		string s;
		cin >> s;
		int A[20];

		for (int i = 0; i < 20; i++)A[i] = 0;

		for (int i = 0; i < s.length(); i++) {
			A[i] = s[i] - '0';
		}

		for (int i = s.length() - 2; i >= 0; i--) {
			if (A[i] > A[i + 1] && A[i] != 0) {
				A[i]--;
				for (int j = i + 1; j < s.length(); j++) {
					A[j] = 9;
				}
			}
		}

		cout << "Case #" << test << ": ";
		for (int i = 0; i < s.length(); i++) {
			if (i == 0 && A[i] == 0) continue;
			cout << A[i];
		}
		cout << "\n";

	}

	return 0;
}