#include <iostream>
#include <vector>
#include <map>
#include <string>
#include <algorithm>
#include <unordered_map>
using namespace std;

int main() {
	freopen("B-large.in.txt", "r", stdin);
	freopen("B-large.out.txt", "w", stdout);
	int cases;
	cin >> cases;
	for (int cas = 1; cas <= cases; cas++) {
		long long N;
		cin >> N;
		cout << "Case #"<<cas<<": ";
		string str = "";
		long long cur = N;
		while (cur) {
			str += cur % 10 + '0';
			cur /= 10;
		}
		reverse(str.begin(), str.end());

		for (int i = 0; i < str.length() - 1; i++) {
			if (str[i] > str[i + 1]) {
				//for (int j = i + 1; j < str.length(); j++) {
				//	str[i + 1] = '9';
				//}
				int j = i - 1;
				for (; j >= 0; j--) {
					if (str[j] == str[i]) continue;
					else break;
				}
				str[j + 1]--;
				for (int k = j + 2; k < str.length(); k++) {
					str[k] = '9';
				}
				break;
			}
		}
		long long ans = 0;
		for (int i = 0; i < str.length(); i++) {
			ans *= 10;
			ans += str[i] - '0';
		}
	//	cout << str << endl;
		cout << ans << endl;

	}

	return 0;
}