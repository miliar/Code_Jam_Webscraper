#include <fstream>
#include <string>

using namespace std;

void flip(string& s, int pos, int k) {
	for(int i = pos; i < pos + k; i++) {
		if(s[i] == '-') {
			s[i] = '+';
		}
		else if(s[i] == '+') {
			s[i] = '-';
		}
	}
}

int solve(string& s, int k) {
	int cnt = 0;
	for(int i = 0; i + k - 1 < s.length(); i++) {
		if(s[i] == '-') {
			flip(s, i, k);
			cnt++;
		}
	}
	if(s.find('-', s.length() - k) == string::npos) {
		return cnt;
	}
	return -1;
}

int main() {
	ifstream f("input.txt");
	ofstream g("output.txt");
	int t;
	f >> t;
	for(int i = 1; i <= t; i++) {
		string s;
		int k;
		f >> s >> k;
		int res = solve(s, k);
		g << "Case #" << i << ": ";
		if(res == -1) {
			g << "IMPOSSIBLE";
		}
		else {
			g << res;
		}
		g << '\n';
	}
	f.close();
	g.close();
	return 0;
}
