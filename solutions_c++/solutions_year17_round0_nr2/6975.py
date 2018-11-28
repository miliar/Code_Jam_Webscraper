//Irvin Gonzalez
//

#include <iostream>
#include <string>
#include <cmath>

using namespace std;

void solve() {
	long long n;
	cin >> n;

	int maxd = (int)log(n);

	for(int d = 1; d <= maxd; ++d) {
		if(n >= (long long)pow(10.0, d))
		{
			int a = (n % ((long long)pow(10.0, d))) /
				((long long)pow(10.0, d - 1));
			int b = (n % ((long long)pow(10.0, d + 1))) /
				((long long)pow(10.0, d));

			if(a < b) {
				n -= (n % ((long long)pow(10.0, d)) + 1); }
		}
	}
	cout << n;

}
int main() {
	int T;
	cin >> T;
	for (int i = 1; i <= T; ++i) {
		cout << "Case #" << i << ": ";
		solve();
		cout << endl; 
	}
	return 0; 
}
