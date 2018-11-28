#include <iostream>
#include <vector>
#include <string>
#include <math.h>
typedef unsigned long long int ulint;
using namespace std;
int main() {
	int t; cin >> t;
	for(int i_t = 1; i_t <= t; ++i_t) {
		ulint n; cin >> n;
		ulint k; cin >> k;
		ulint temp = k;
		ulint m = 1;
		while(pow(2,m) <= k) {
			m++;
		}

		ulint k_rem = k - pow(2,m - 1) + 1;
		ulint n_rem = n - pow(2, m - 1) + 1;
		ulint block_size = n_rem / pow(2,m - 1);
		ulint n_div_rem = n_rem - block_size * pow(2,m - 1);
		
		if(k_rem <= n_div_rem) {
			block_size++;
		}
		if(block_size % 2 == 1) {
			cout << "Case #" << i_t << ": " << block_size / 2 << " " << block_size / 2 << endl;
		} else {
			cout << "Case #" << i_t << ": " << block_size / 2 << " " << - 1 + block_size / 2 << endl;
		}
	}
}

