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

int num[25];

int main() {
	ios::sync_with_stdio(0);
	ifstream xin(IN_FILE);
	ofstream xout(OUT_FILE);
	cin.rdbuf(xin.rdbuf());
	cout.rdbuf(xout.rdbuf());
	int t;
	int tc = 1;
	cin >> t;
	while (t--) {
		for (int i = 0; i < 25; i++)
			num[i] = 0;
		ll n;
		cin >> n;
		ll tn = n;
		int curr = 0;
		while (tn > 0) {
			num[curr++] = tn % 10;
			tn /= 10;
		}
		curr = -1;
		int focus = -1;
		for (int i = 24; i >= 0; i--) {
			if (num[i] > curr)
				curr = num[i];
			else if (num[i] < curr) {
				focus = i;
				break;
			}
		}
		if (focus != -1) {
			int found = -1;
			for (int i = focus + 1; i < 24; i++) {
				if (num[i + 1] < num[i]) {
					found = i;
					break;
				}
			}
			num[found]--;
			for (int i = found - 1; i >= 0; i--)
				num[i] = 9;
		}
		ll ans = 0;
		for (int i = 24; i >= 0; i--) {
			ans *= 10ll;
			ans += num[i];
		}
		cout << "Case #" << tc << ": " << ans << "\n";
		tc++;
	}
	system("pause");
	return 0;
}
