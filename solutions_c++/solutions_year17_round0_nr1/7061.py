#include <iostream>
#include <vector>
#include <map>
#include <string>
#include <algorithm>
#include <unordered_map>
using namespace std;

int main() {
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int cases;
	cin >> cases;
	for (int cas = 1; cas <= cases; cas++) {
		string S;
		cin >> S;
		int k;
		cin >> k;
		cout << "Case #"<<cas<<": ";
		string ed = string(S.length() , '+');
		if (S == ed) {
			cout << "0" <<endl;
			continue;
		}
		int ans = 0;
		for (int i = 0; i + k <= S.length(); i++) {
			if (S[i] == '-') {
				for (int j = 0; j < k; j++) {
					if (S[i + j] == '+') {
						S[i + j] = '-';
					}
					else S[i + j] = '+';
				}
				ans ++;
			}
		}
		if (S == ed) {
			cout << ans << endl;
		}
		else cout <<"IMPOSSIBLE"<<endl;

	}

	return 0;
}