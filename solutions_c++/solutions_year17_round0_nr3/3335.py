#include <iostream>
#include <fstream>
#include <algorithm>
#include <stdio.h>
#include <string>
#include <math.h>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <bitset>

#define pb push_back
#define mp make_pair
#define mod 1000000007

using namespace std;

long long int t, n, k, x, y;


int main() {
	freopen("C-large.in","r",stdin);
	freopen("data.out","w",stdout);

	scanf("%d", &t);
	for (int i = 1; i <= t; i++) {
		scanf("%lld%lld", &n, &k);
		x = 1;
		y = 0;
		while (k > 0) {
			if (k - x <= 0) {
				if (x - k < y) {
					n--;
				}
				if (n % 2) {
					cout << "Case #" << i << ": " << n / 2 << ' ' << n / 2 << '\n';
				}
				else {
					cout << "Case #" << i << ": " << n / 2 << ' ' << n / 2 - 1 << '\n';
				}
				break;
			}
			/*for (int j = 0; j < x; j++) {
			if (j < y) {
			cout << n - 1 << ' ';
			}
			else {
			cout << n << ' ';
			}
			}
			cout << '\n';*/
			if (!(n % 2)) {
				y += x;
			}
			n >>= 1;
			k -= x;
			x <<= 1;

		}
	}
}
