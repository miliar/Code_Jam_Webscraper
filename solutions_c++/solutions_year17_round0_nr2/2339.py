#include <fstream>
#include <string>

using namespace std;

string& removeLeadingZeroes(string& s) {
	int i, l = s.length() - 1;
	for(i = 0; i < l && s[i] == '0'; i++);
	s = s.substr(i);
	return s;
}

string& solve(string& s) {
	int i, l = s.length();
	for(i = 1; i < l && s[i] >= s[i - 1]; i++);
	if(i < l) {
		for(i = i - 2; i >= 0 && s[i] == s[i + 1]; i--);
		s[i + 1]--;
		for(int j = i + 2; j < l; j++) {
			s[j] = '9';
		}
	}
	return removeLeadingZeroes(s);
}

int main() {
	int t;
	string n;
	ifstream f("input.txt");
	ofstream g("output.txt");
	f >> t;
	for(int i = 1; i <= t; i++) {
		f >> n;
		g << "Case #" << i << ": " << solve(n) << '\n';
	}
	f.close();
	g.close();
	return 0;
}
