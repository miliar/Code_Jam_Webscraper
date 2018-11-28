#include <fstream>
#include <string>
using namespace std;

int t;
void change(char& c);
bool findMinTimes(string s, int k, int& times);

int main() {
	ios_base::sync_with_stdio(false);

	ifstream in("input.in");
	ofstream out("output.out");

	in >> t;
	for (int cnt = 1; cnt <= t; ++cnt) {
		string s;
		in >> s;
		int k;
		in >> k;
		out << "Case #" << cnt << ": ";
		int times = 0;
		if (findMinTimes(s, k, times)) out << times << "\n";
		else out << "IMPOSSIBLE\n";
	}

	in.close(); out.close();
	return 0;
}

void change(char& c) {
	if (c == '-') c = '+';
	else c = '-';
}

bool findMinTimes(string s, int k, int& times) {
	int size = s.size();
	for (int i = 0; i <= size - k; ++i) {
		if (s[i] == '-') {
			for (int j = i; j < i + k; ++j)
				change(s[j]);
			++times;
		}
	}
	for (int i = 0; i < size; ++i)
		if (s[i] == '-') return false;
	return true;
}