#include <fstream>
#include <iostream>
#include <unordered_set>
#include <queue>
#include <string>

using namespace std;

bool isAllPlus(const string& s);
string flip(string s, int n, int pos);
int BFS(string s, int n);

int main() {
	ifstream in("A-small-attempt1.in");
	ofstream out("out.txt");
	int T;
	in >> T;
	for (int i = 1; i <= T; ++i) {
		string s;
		int n;
		in >> s >> n;
		out << "Case #" << i << ": ";
		int r = BFS(s, n);
		if (r == -1) {
			out << "IMPOSSIBLE" << endl;
		}
		else {
			out << r << endl;
		}
	}

	return 0;
}

bool isAllPlus(const string& s) {
	for (char c : s)if (c != '+')return false;
	return true;
}

string flip(string s, int n, int pos) {
	for (int i = 0; i < n; ++i) {
		if (s[i + pos] == '+') {
			s[i + pos] = '-';
		}
		else {
			s[i + pos] = '+';
		}
	}
	return s;
}

int BFS(string s, int n) {
	unordered_set<string> seen;
	int depth = 0;
	queue<string> curr, next;
	curr.push(s);
	while (!curr.empty() || !next.empty()) {
		while (!curr.empty()) {
			string cs = curr.front();
			if (isAllPlus(cs))return depth;
			curr.pop();
			seen.insert(cs);
			for (int i = 0; i < s.size() - n + 1 ; ++i) {
				string ns = flip(cs, n, i);
				if (seen.find(ns) == seen.end()) {
					next.push(ns);
				}
			}
		}
		depth++;
		swap(curr, next);
	}
	return -1;
}