#include <iostream>
#include <fstream>
#include <string>

using namespace std;

ofstream g("A.out");

void output(short t, short x) {
	g << "Case #" << t << ": ";
	if (x == -1)
		g << "IMPOSSIBLE\n";
	else
		g << x << "\n";
}
void convert(string s, bool parity[], short &n) {
	n = s.length();
	for (short i = 0; i < n; i++)
		if (s[i] == '+')
			parity[i] = 0;
		else
			parity[i] = 1;
}
void zero(bool x[], short n, short &flips) {
	for (short i = 0; i < n; i++)
		x[i] = 0;
	flips = 0;
}
void pancake(bool parity[], bool flip[], short n, short k, short &flips) {
	for (short i = 0; i <= n - k; i++) {
		if (parity[i] ^ flip[i]) {
			flips++;
			for (short j = i; j <= i + k - 1; j++) {
				flip[j] = !flip[j];
			}
		}
	}
	for (short i = n - k + 1; i < n; i++)
		if (parity[i] ^ flip[i]) {
			flips = -1;
			return;
		}
}
int main() {
	ifstream f("A-large.in");
	short t, n, k, flips(0);
	bool parity[1000], flip[1000];
	string s;

	f >> t;
	for (int i = 1; i <= t; i++) {
		f >> s >> k;
		convert(s, parity, n);
		zero(flip, n, flips);
		pancake(parity, flip, n, k, flips);
		output(i, flips);
	}
}