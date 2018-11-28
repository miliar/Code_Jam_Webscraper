#include <iostream>
#include <string>
#include <vector>
#include <cmath>
#include <algorithm>

using namespace std;

void f() {
	long long n, k; cin >> n >> k;
	//for (int k = 1; k <= j; k++)
	//{

	long long i = ceil(log2(k+1ll));
	long long l = (n - k) >> i;
	long long r = (n - k + (1<<(i-1))) >> i;
	cout << r << ' ' << l << endl;
	//cout << " i=" << i << " r=" << r << " l=" << l << endl;
	//}
}

int main() {
	int t; cin >> t;
	for (int x = 0; x < t; ++x) {
		cout << "Case #" << x+1 << ": ";
		f();
	}
}
