#include <iostream>
#include <vector>
#include <map>
#include <string>
#include <algorithm>
#include <fstream>
#include <iomanip>

using namespace std;

const double pi = 3.141592653589;

class A {
public:
	double h, r;
	A() {

	}
	bool operator>(A &rhs) {
		return this->r*this->h < rhs.r*rhs.h;
	}
	bool operator<(A &rhs) {
		return this->r*this->h > rhs.r*rhs.h;
	}
};

int main() {
	ifstream ifs("in.txt", ios::in);
	ofstream ofs("out.txt", ios::out);
	int T;
	ifs >> T;
	for (int loop = 0; loop < T; loop++) {
		int n, k;
		double ans = 0;
		ifs >> n >> k;
		vector<A> a;
		a.resize(n);
		for (int i = 0; i < n; i++)
			ifs >> a[i].r >> a[i].h;
		sort(a.begin(), a.end());
		double ma = 0;
		int idd = 0;
		for (int i = 0; i < k - 1; i++) {
			ans += a[i].h*a[i].r * 2 * pi;
			if (a[i].r > ma) {
				ma = a[i].r;
				idd = i;
			}
		}
		int id = -1;
		double maa = a[idd].r * a[idd].r * pi + a[k - 1].r*2*a[k - 1].h*pi;
		for (int i = k - 1; i < n; i++) {
			if (maa < a[i].r * a[i].r * pi + a[i].h * 2*a[i].r*pi) {
				maa = a[i].r * a[i].r * pi + a[i].h * 2 * a[i].r*pi;
				id = i;
			}
		}
		if (id > 0) {
			ans += maa;
		}
		else {
			ans += a[idd].r * a[idd].r * pi + a[k - 1].r * 2 * a[k - 1].h*pi;
		}
		ofs << "Case #" << (loop+1) << ": " << fixed << setprecision(16) << ans << endl;
	}
	return 0;
}