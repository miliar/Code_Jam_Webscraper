#include <bits/stdc++.h>

using namespace std;

typedef long long LL;

#define IOS ios_base::sync_with_stdio(0);cin.tie(0);
#define MP make_pair
#define PB push_back
#define FF first
#define SS second

int main() {
	IOS;
	freopen("A-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	int t, kase = 0;
	cin >> t;
	while (t--) {
		int r, c;
		cin >> r >> c;
		string ma[30];
		for (int i = 0; i < r; i++) cin >> ma[i];
		for (int i = 0; i < r; i++) {
			for (int j = 0; j < c; j++) {
				if (ma[i][j] != '?')
					for (int k = j - 1; k >= 0; k--)
						if (ma[i][k] == '?') ma[i][k] = ma[i][j];
			}
		}
		for (int i = 0; i < r; i++) {
			for (int j = c - 1; j >= 0; j--) {
				if (ma[i][j] != '?')
					for (int k = j + 1; k < c; k++)
						if (ma[i][k] == '?') ma[i][k] = ma[i][j];
			}
		}
		for (int i = 0; i < r; i++) {
			if (ma[i][0] != '?') {
				for (int j = i - 1; j >= 0; j--) {
					if(ma[j][0] == '?') ma[j] = ma[i];
					else break;
				}
			}
		}
		for (int i = r - 1; i >= 0; i--) {
			if (ma[i][0] != '?') {
				for (int j = i + 1; j < r; j++) {
					if(ma[j][0] == '?') ma[j] = ma[i];
					else break;
				}
			}
		}
		cout << "Case #" << ++kase << ": \n";
		for (int i = 0; i < r; i++) {
			cout << ma[i] << "\n";
		}
	}
}
