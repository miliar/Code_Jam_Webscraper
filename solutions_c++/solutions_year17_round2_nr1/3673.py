#include <iostream>
#include <fstream>
#include <iomanip>

using namespace std;

ifstream f("A-large.in");
ofstream g("A.out");

struct Horse {
	double v, t;
	int k, d;
};
void input(Horse horse[], short &n, int &d) {
	f >> d >> n;
	for (int i = 0; i < n; i++) {
		f >> horse[i].k >> horse[i].v;
		horse[i].d = d - horse[i].k;
		horse[i].t = horse[i].d / horse[i].v;
	}
}
void output(short t, double x) {
	g << setprecision(1000) << "Case #" << t << ": " << x << "\n";
}
double maxT(Horse horse[], short n) {
	double max = -1;
	for (short i = 0; i < n; i++)
		if (horse[i].t > max)
			max = horse[i].t;
	return max;
}
int main() {
	Horse horse[1000];
	short t, n;
	int d;

	f >> t;
	for (short i = 1; i <= t; i++) {
		input(horse, n, d);
		output(i, d / maxT(horse, n));
	}
	f.close();
	g.close();
	return 0;
}