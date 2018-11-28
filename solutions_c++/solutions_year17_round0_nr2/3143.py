#include <fstream>

using namespace std;

ifstream cin("input.txt");
ofstream cout("output.txt");

typedef long long lint;

// x > 0
string lint_to_str(lint x) {
	string r = "";
	while (x > 0)
		r = char('0' + x % 10) + r, x /= 10;
	return r;
}

// also > 0
lint str_to_lint(string s) {
	lint r = 0;
	for (int i = 0; i < s.length(); ++i)
		r = r * 10 + (s[i] - '0');
	return r;
}

lint tidify(lint x) {
	string s = lint_to_str(x);
	int i = 1;
	while (i < s.length() && s[i] >= s[i - 1])
		++i;
	while (i < s.length())
		s[i] = s[i - 1], ++i;
	return str_to_lint(s);
}

lint last_tidy(lint n) {
	lint l = 1, r = n + 1;
	while (l + 1 < r) {
		lint m = (l + r) / 2;
		if (tidify(m) <= n)
			l = m;
		else
			r = m;
	}
	return tidify(l);
}

int main() {
	int t;
	lint n;
	cin >> t;
	for (int i = 0; i < t; ++i) {
		cin >> n;
		cout << "Case #" << i + 1 << ": ";
		cout << last_tidy(n) << endl;
	}
	return 0;
}