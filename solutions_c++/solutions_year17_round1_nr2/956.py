#include <algorithm>
#include <iostream>
#include <cstdio>
#include <vector>
#include <map>
using namespace std;

bool isvalid(int x, int v, int n) {
	return (n * x * 9 <= v * 10 && v * 10 <= n * x * 11);
}

bool intersect(pair <int, int> A, pair <int, int> B) {
	return max(A.first, B.first) <= min(A.second, B.second);
}

int minvalid(int x, int v) {
	return ((v * 10) + (x * 11) - 1) / (x * 11);
}
int maxvalid(int x, int v) {
	return (10 * v) / (9 * x);
}

void sol() {
	int n, p;
	cin >> n >> p;

	if (n == 1) {
		int x;
		cin >> x;
		int ans = 0;
		for (int i = 0; i < p; i++) {
			int t;
			cin >> t;
			ans += (isvalid(x, t, minvalid(x, t)) || isvalid(x, t, maxvalid(x, t)));
		}
		cout << ans << endl;
	} else {
		int ing[2];
		for (int i = 0; i < 2; i++) {
			cin >> ing[i];
		}
		int a[p];
		for (int i = 0; i < p; i++) {
			cin >> a[i];
		}
		int b[p];
		for (int i = 0; i < p; i++) {
			cin >> b[i];
		}
		sort(a, a + p);
		sort(b, b + p);
		int ans = 0;
		for (int m1 = 0; m1 < (1 << p); m1++) {
			for (int m2 = 0; m2 < (1 << p); m2++) {
				if (__builtin_popcount(m1) == __builtin_popcount(m2)) {
					vector <int> x, y;
					for (int i = 0; i < p; i++) {
						if ((m1 >> i) & 1) {
							x.push_back(a[i]);
						}
						if ((m2 >> i) & 1) {
							y.push_back(b[i]);
						}
					}
					bool flag = true;
					for (int i = 0; i < x.size(); i++) {
						flag &= intersect({minvalid(ing[0], x[i]), maxvalid(ing[0], x[i])}, {minvalid(ing[1], y[i]), maxvalid(ing[1], y[i])});
					}
					if (flag) {
						ans = max(ans, __builtin_popcount(m1));
					}
				}
			}
		}
		cout << ans << endl;
	}
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int t;
	cin >> t;
	for (int i = 0; i < t; i++) {
		cout << "Case #" << i + 1 << ": ";
		sol();
	}

	fclose(stdin);
	fclose(stdout);
}