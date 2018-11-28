#include <iostream>
#include <string>
#include <list>
using namespace std;
void result(int, int);
int translate(char);
void main() {
	int t;
	cin >> t;

	for (int i = 0; i < t; i++) {
		list <int> l;
		string s; int k;
		cin >> s; cin >> k;
		int len = s.length();
		for (int c = 0; c < k; c++) {
			l.push_back(translate(s[c]));
		}
		int flips = 0;
		for (int c = k; c < len; c++) {
			int front = l.front();
			l.pop_front();
			if (front == -1) {
				flips++;
					for (list<int>::iterator it = l.begin(); it != l.end(); ++it) {
						*it *= -1;
					}
			}
			l.push_back(translate(s[c]));
		}
		int front = l.front();
		if (front == -1) {
			flips++;
		}
		for (auto it = l.cbegin(); it != l.cend() && flips != -1; ++it) {
			if (*it != front) {
				flips = -1;
			}
		}
		result(i, flips);
	}
}

void result(int nb, int flips) {
	cout << "Case #" << nb+1 << ": ";
	if (flips == -1) {
		cout << "IMPOSSIBLE";
	}
	else {
		cout << flips;
	}
	cout << endl;
}

int translate(char c) {
	if (c == '+') {
		return 1;
	}
	else {
		return -1;
	}
}