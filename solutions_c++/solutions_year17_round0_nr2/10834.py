#include<iostream>
#include<fstream>
using namespace std;
ifstream in("B-small-attempt0.in");
ofstream out("output.out");
void tidy(long long x,int i) {
	int a = x % 10;
	int b = (x / 10) % 10;
	long long y = x;
	while ((a>=b) && (x)) {
		x /= 10;
		a = b;
		b = (x / 10) % 10;
	}
	if (!x) {
		out << "Case #" << i << ": " << y << endl;
	}
	else
		tidy(y - 1, i);
}
int main()
{
	int t;
	long long n;
	in >> t;
	long long y;
	for (int i = 1; i <= t; i++) {
		in >> n;
		if (n / 10 == 0) {
			y = n;
			out << "Case #" << i << ": " << y << endl;
		}
		else
			tidy(n,i);
	}
	return 0;
}