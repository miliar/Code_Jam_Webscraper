#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <vector>
#include <string>
#include <fstream>

#define IN_FILE "B-large.in"
#define OUT_FILE "outL.txt"

using namespace std;

typedef long long ll;
typedef long double ld;
ll s1[50], s2[50];

int main() {
	ios::sync_with_stdio(0);
	ifstream xin(IN_FILE);
	ofstream xout(OUT_FILE);
	cin.rdbuf(xin.rdbuf());
	cout.rdbuf(xout.rdbuf());
	ll i, j, k, t1, t2, t3, t4, t, n, l, cnt=0,ans,f;
	cin >> t;
	while (t--) {
		cin >> n;
		for (i = 0; i < 40; i++) {
			s1[i] = 0;
		}
		i = 0;
		f = -1;
		while (n > 0) {
			t1 = n % 10;
			s1[i++] = t1;
			n /= 10;
		}
		for (i = 39; i > 0 ; i--) {
			if (s1[i] > s1[i - 1]) {
				f = i;
				break;
			}
		}
		ans = 0;
		if (f == -1) {
			t1 = 1;
			for (i = 0; i < 40; i++) {
				t2 = t1*s1[i];
				ans += t2;
				t1 *= 10;
			}
		}
		else {
			t1 = -1;
			for (i = f; i < 39; i++) {
				if (s1[i + 1] < s1[i]) {
					t1 = i;
					break;
				}
			}
			s1[t1]--;
			for (i = t1 - 1; i >= 0; i--) {
				s1[i] = 9;
			}
			ans = 0;
			t1 = 1;
			for (i = 0; i < 40; i++) {
				t2 = t1*s1[i];
				ans += t2;
				t1 *= 10;
			}
		}
		cnt++;
		cout << "Case #" << cnt << ": " << ans << "\n";
	}
	system("pause");
	return 0;
}
