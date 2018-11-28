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
	ios_base::sync_with_stdio(false);
	cin.tie(0);

	int t;
	cin >> t;

	for (int cas = 1; cas <= t; cas++) {
		cout << "Case #" << cas << ": ";

		int cnt = 0;

		string str;
		int k;
		cin >> str >> k;

		for (int i = 0; i < str.size() - k + 1; i++) {
			if (str[i] == '-') {
				++cnt;
				for (int j = 0; j < k; j++) {
					if (str[i + j] == '-') {
						str[i + j] = '+';
					} else {
						str[i + j] = '-';
					}
				}
			}
		}

		bool f = true;
		for (int i = str.size() - k + 1; i < str.size(); i++) {
			if (str[i] == '-') {
				f = false;
			}
		}

		if (f) {
			cout << cnt << endl;
		} else {
			puts("IMPOSSIBLE");
		}
	}

	return 0;
}