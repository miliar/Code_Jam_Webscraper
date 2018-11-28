#include<bits/stdc++.h>
using namespace std;
typedef long long li;
int t;
unsigned long long int no;
string str;
li len;
void solve() {
	int i, j;
	for (i = 0 ; i < len - 1 ; i++) {
		if (str[i] <= str[i + 1]) {
			//cout << "feas ";
			continue;
		}
		else {

			j = i;
			while (str[j] == str[j - 1]) {
				j -= 1;
				if (j == 0)
					break;
				}
			str[j] = str[j] - 1;

		}
		i = j + 1;
		while (i <= len - 1) {
			str[i] = '9';
			i += 1;
		}
	}
}
int main() {
	ios_base::sync_with_stdio(false), cin.tie(0), cout.tie(0);
// #ifndef ONLINE_JUDGEb
// 	freopen("input.txt", "r", stdin);
// 	freopen("output.txt", "w", stdout);
// #endif
	cin >> t;
	for (int i = 1 ; i <= t ; i++)
	{	cin >> no;
		if (no % 10 == 0) {
			str = to_string(no - 1);
		}
		else str = to_string(no);
		len = str.length();
		solve();
		cout << "Case #" << i << ": " ;
		for (int i = 0 ; i < len ; i++) {
			if (str[i] != '0') {
				cout << str[i];
			}
		}
		cout << endl;
	}
	return 0;
}