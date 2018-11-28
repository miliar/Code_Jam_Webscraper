#include<iostream>
#include<string>
#include<algorithm>
using namespace std;
bool complete_set(string str) {
	for (int i = 0; i < str.length() - 1; i++) {
		if (str[i] > str[i + 1]) return false;
	}
	return true;
}
string tidy(long long a) {
	string str = to_string(a), res;
	if (str.length() == 1) return str;
	if (complete_set(str)) return str;
	int max_val = 0;
	int idx = 0;
	for (int i = 0; i < str.length() - 1; i++) {
		if (max_val < str[i] - '0') {
			max_val = str[i] - '0';
			idx = i;
		}
	}
	if (max_val == 1) {
		for (int i = 0; i < str.length() - 1; i++)
			res = res + '9';
	}
	else {
		for (int i = 0; i < idx; i++) {
			res = res + str[i];
		}
		res = res + to_string(str[idx] - '0' - 1);
		for (int i = idx + 1; i < str.length(); i++)
			res = res + '9';
	}
	return res;
}

int main()
{
	ios::sync_with_stdio(false); cin.tie(0);
	int tc; cin >> tc;
	for (int i = 1; i <= tc; i++) {
		long long n; cin >> n;
		cout << "Case #" << i << ": " << tidy(n) << '\n';
	}
	return 0;

}
