#include <iostream>
#include <fstream>
#include <vector>
#include <string>

using namespace std;

bool check_done(vector<int>& v) {
	for (int& i : v)
		if (i != 1) return false;
	return true;
}

int get_solution(vector<int>& v, const int& k) {
	int flip = 0;
	if (k > v.size())
		return -1;

	for (int i = 0; i <= v.size() - k; i++) {
		if (v[i] == 0) {
			for (int j = 0; j < k; j++) {
				v[i + j] = 1 - v[i + j];
			}
			flip++;
		}
	}
	if (check_done(v))
		return flip;
	return -1;
}

void solve(istream& is, ostream& os) {
	int n;
	is >> n;

	for (int i = 0; i < n; i++) {
		string s; int k;
		is >> s >> k;

		vector<int> pan(s.size());
		for (int j = 0; j < s.size(); j++) {
			if (s[j] == '-') pan[j] = 0;
			else if(s[j] == '+') pan[j] = 1;
		}

		if (check_done(pan)) {
			os << "Case #" << i + 1 << ": 0\n";
		}
		else {
			int a = get_solution(pan, k);
			if (a == -1) {
				os << "Case #" << i + 1 << ": IMPOSSIBLE\n";
			}
			else {
				os << "Case #" << i + 1 << ": " << a << "\n";
			}
		}
	}
}

int main() {
	ifstream infile("A-large.in");
	ofstream outfile("A-large.out");
	solve(infile, outfile);
}