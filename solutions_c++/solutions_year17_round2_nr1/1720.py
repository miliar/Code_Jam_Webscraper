#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <unordered_map>
#include <unordered_set>
#include <array>
#include <tuple>

#define ll long long
#define ull unsigned long long
#define FOR(n) for(long long i = 0; i < n; i++)
#define DFOR(n) for(long long i = n - 1; i >= 0; i--)

using namespace std;

int main() {
	int T;
	cin >> T;
	for(int temp_t = 0; temp_t < T; temp_t++) {
		cout << "Case #" << temp_t + 1 << ": ";
		ll D;
		int N;
		cin >> D >> N;
		float ans = 1000000000000000;
		FOR(N) {
			ll a, b;
			cin >> a >> b;
			float c = b * float(D) / (D - a);
			//cout << a << " " << b << " " << c << " " << (D - a) << " " << (D - a) / D << " " << b * (D - a) / D;
			if(ans > c) ans = c;
			//cout << a << " " << b << " " << c << " ";
		}
		cout.setf(ios::fixed);
		cout.precision(6);
		cout << ans << "\n";
	}
	return 0;
}