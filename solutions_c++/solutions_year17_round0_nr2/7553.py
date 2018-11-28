#include <iostream>
#include <fstream>
#include <set>

using namespace std;

ofstream g("B.out");

void output(short num[19], short n, short t) {
	g << "Case #" << t << ": ";
	short i(0);
	while (!num[i])
		i++;
	while (i < n) {
		g << num[i];
		i++;
	}
	g << "\n";
}
short length(long long x) {
	short l(0);
	while (x) {
		l++;
		x /= 10;
	}
	return l;
}
void convert(short num[19], long long temp, short &n) {
	n = length(temp);
	for (short i = n - 1; i >= 0; i--) {
		num[i] = temp % 10;
		temp /= 10;
	}
}
short findIndex(short num[19], short k) {
	if (k == 0 || num[k - 1] < num[k])
		return k;
	else
		return findIndex(num, k - 1);
}
void modify(short num[19], short n, short k) {
	num[k]--;
	k++;
	while (k < n) {
		num[k] = 9;
		k++;
	}
}
void tidy(short num[19], short n) {
	short big(0);
	for (short i = 0; i < n; i++) {
		if (num[i] >= big) {
			big = num[i];
		}
		else {
			modify(num, n, findIndex(num, i));
			return;
		}
	}
}
int main() {
	ifstream f("B-large.in");
	short num[19], t, n;
	long long temp;

	f >> t;
	for (short i = 1; i <= t; i++) {
		f >> temp;
		convert(num, temp, n);
		tidy(num, n);
		output(num, n, i);
	}
	return 0;
}