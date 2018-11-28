#include <bits/stdc++.h>

#define pb push_back
#define f first
#define s second
#define pii pair<int, int>
#define mp make_pair
 
using namespace std;
 
const string name = "A",
             in_file = name + ".in",
             out_file = name + ".out";
 
ifstream fin(in_file);
ofstream fout(out_file);

const int MAX = 1e3 + 1;
const long double PI = 3.14159265358979323846;
struct Pancake {
	long long r, h;

	Pancake() {
		r = h = 0;
	}

	Pancake(long long r, long long h) {
		this->r = r;
		this->h = h;
	}

	long long getArea() {
		return r * h;
	}
} pancake[MAX];

bool operator <(const Pancake& x, const Pancake& y) {
    return x.r * x.h  < y.r * y.h;
}

int n, k;

long double solve() {
	sort(pancake + 1, pancake + n + 1);
	long long vaca1 = 0, maxR = 0;
	for (int i = 0; i < k; i++) {
		vaca1 += pancake[n - i].getArea();
		maxR = max(maxR, pancake[n - i].r);
	}

	long double sol1 = PI * (maxR * maxR + 2 * vaca1);

	long double vaca2 = 0;
	int indexMaxR = 0;
	maxR = 0;

	for (int i = 1; i <= n; i++) {
		if (pancake[i].r > maxR) {
			maxR = pancake[i].r;
			indexMaxR = i;
		}
	}

	vaca2 = pancake[indexMaxR].getArea();
	
	for (int i = n, count = 1; count < k; count++, i--) {
		if (i == indexMaxR) {
			count--;
			continue;
		}
		vaca2 += pancake[i].getArea();
	}

	long double sol2 = PI * (maxR * maxR + 2 * vaca2);
	return max(sol2, sol1);
}

int main() {
	int t;
	fin >> t;
	
	for (int test = 1; test <= t; test++) {
		fin >> n >> k;
		for (int i = 1; i <= n; i++) {
			fin >> pancake[i].r >> pancake[i].h;
		}

		fout << "Case #" << test << ": " << fixed << setprecision(6) << solve() << '\n';
	}

	return 0;
}