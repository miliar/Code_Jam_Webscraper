#include <iostream>
#include <fstream>
using namespace std;

int main() {
	ifstream in("b.in");
	ofstream out("b.out");
	long long n, i, j;
	char s[1001];
	in >> n;
	for (i = 1; i <= n; ++i) {
		in >> s;
		out << "Case #" << i << ": ";
		j = 0;
		while (s[j + 1] != '\0' && s[j] <= s[j + 1]) {
			++j;
		}
		if (s[j + 1] == '\0') {
			out << s << '\n';
			continue;
		}
		while (j && s[j] == s[j - 1]) {
			--j;
		}
		--s[j];
		for (++j; s[j] != '\0'; ++j) {
			s[j] = '9';
		}
		for (j = 0; s[j] == '0'; ++j);
		out << (s + j) << '\n';
	}
}

