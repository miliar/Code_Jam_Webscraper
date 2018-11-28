#include <iostream>
#include <string>
#include <cstring>
#include <fstream>
#include <algorithm>
#include <numeric>
using namespace std;

bool complete(string s) {
	for (int i = 0; i < s.size(); ++i) {
		if (s[i] == '-') return false;
	}
	return true;
}

string reverse_pancake(string s, int a, int b) {
	for (int i = a; i < a + b; ++i) {
		s[i] = s[i] == '-' ? '+' : '-';
	}
	return s;
}

int fill(string s, int k, int n, int sum) {
	if (n > s.size() - k && !complete(s) || n >= s.size()) return numeric_limits<int>::max();
	if (complete(s)) return sum;
	return min(fill(s, k, n + 1, sum), fill(reverse_pancake(s, n, k), k, n + 1, sum + 1));
}

int main() {
	ifstream cin("A-small-attempt0.in");
	ofstream cout("A-small-attempt0.out");
	int t;
	cin >> t;
	for (int i = 0; i < t; ++i){
		string s;
		int k;
		cin >> s >> k;
		int result = fill(s, k, 0, 0);
		if (result != numeric_limits<int>::max()) cout << "Case #" << i+1 << ": " << result << endl;
		else cout << "Case #" << i + 1 << ": IMPOSSIBLE" << endl;
	}
	cin.close();
	cout.close();
	system("pause");
}
