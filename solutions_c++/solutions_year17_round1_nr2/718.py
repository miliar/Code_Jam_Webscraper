#include<iostream>
#include<cstdio>
#include<cstring>
#include<fstream>
#include<vector>
#include<algorithm>
#include<cmath>
using namespace std;
int n[100];
int a[100];
int v[100][100];
const double eps = 1e-6;
bool f() {
	return true;
}
int main() {
	int T, N, P;
	ofstream out("answer.txt");
	cin >> T;
	int i, j, k, t, x;
	int kase = 0, ans;
	bool ok, fin;
	double temp;
	while (T--) {
		t = 0;
		cin >> N >> P;
		for (i = 0; i < N; i++)
			cin >> n[i];
		for (i = 0; i < N; i++) {
			for (j = 0; j < P; j++) {
				cin >> v[i][j];
			}
			sort(v[i], v[i] + P);
		}
		out << "Case #" << (++kase) << ": ";
		ans = 0;
		fin = true;
		memset(a, 0, sizeof(a));
		for (x = 1; x < 2000000 && fin;) {
			ok = true;
			//cout << x << endl;
			for (i = 0; i < N; i++) {
				j = a[i];
				temp = n[i] * x * 0.9;
				while (temp > v[i][j] && fabs(temp - v[i][j]) > eps) {
					j++;
					if (j >= P) {
						fin = false;
						break;
					}
				}
				if (!fin)
					break;
				a[i] = j;
				temp = n[i] * x * 1.1;
				if (temp < v[i][j] && fabs(temp - v[i][j]) > eps) {
					ok = false;
				}
			}
			if (fin && ok) {
				ans++;
				for (i = 0; i < N; i++) {
					a[i]++;
					if (a[i] >= P)
						fin = false;
				}
			} else
				x++;
		}
		out << ans << endl;
	}
	out.close();
	return 0;
}
