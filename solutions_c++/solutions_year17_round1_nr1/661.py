/* [theMighty] Deathsurgeon
* Rupesh Maity
* Final Year
* IIIT Allahabad
* In search of my ikigai
* Youtube Channel: https://www.youtube.com/channel/UCn1VDq6nXGUGdHVyxU2zFSw
*/

#include <bits/stdc++.h>

#define sd(x) scanf("%d", &x)
#define pb push_back
#define pii pair<int, int>
#define ll long long

#define MAX 1000001
#define MOD 1000000007
#define PI 3.141592653589793

using namespace std;

int main() {
	int t;
	cin >> t;

	for (int cas = 1; cas <= t; cas++) {
		cout << "Case #" << cas << ": " << endl;

		int R, C;
		cin >> R >> C;

		string str[R];

		for (int i = 0; i < R; i++) {
			cin >> str[i];
		}

		int l = -1;

		for (int i = 0; i < R; i++) {
			bool f = false;
			int last = -1;

			for (int j = 0; j < C; j++) {
				if (str[i][j] != '?') {
					for (int a = l + 1; a <= i; a++) {
						for (int b = last + 1; b <= j; b++) {
							str[a][b] = str[i][j];
						}
					}
					f = true;
					last = j;
				}
			}

			if (last != -1 && last != C - 1) {
				for (int a = l + 1; a <= i; a++) {
					for (int b = last + 1; b < C; b++) {
						str[a][b] = str[i][last];
					}
				}
			}

			if (f) {
				l = i;
			}
		}

		for (int i = l + 1; i < R; i++) {
			for (int j = 0; j < C; j++) {
				str[i][j] = str[l][j];
			}
		}

		for (int i = 0; i < R; i++) {
			cout << str[i] << endl;
		}
	}


	return 0;
}