#include<iostream>
#include<string>
#include<algorithm>
using namespace std;
int front_check(string str, int k) {
	int res = 0;
	for (int i = 0; i < str.length() - k + 1; i++) {
		if (str[i] == '1') continue;
		else if (str[i] == '0') {
			res++;
			str[i] = '1';
			// switch
			for (int j = 1; j < k; j++) {
				if (str[i + j] == '1') str[i + j] = '0';
				else str[i + j] = '1';
			}
		}
	}
	for (int i = 0; i < str.length(); i++) {
		if (str[i] == '0') {
			res = -1; 
			break;
		}
	}
	return res;
}
int back_check(string str, int k) {
	int res = 0;
	for (int i = str.length() - 1; i >= k-1; i--) {
		if (str[i] == '1') continue;
		else if (str[i] == '0') {
			res++;
			str[i] = '1';
			// switch
			for (int j = 1; j < k; j++) {
				if (str[i - j] == '1') str[i - j] = '0';
				else str[i - j] = '1';
			}
		}
	}
	for (int i = 0; i < str.length(); i++) {
		if (str[i] == '0') {
			res = -1;
			break;
		}
	}
	return res;
}
string pancake(string str, int k) {
	int cnt_front = 0, cnt_back = 0, res;

	cnt_front = front_check(str, k);
	cnt_back = back_check(str, k);

	res = min(cnt_front, cnt_back);
	if (res == -1) return "IMPOSSIBLE";
	else return to_string(res);
}
int main()
{
	ios::sync_with_stdio(false); cin.tie(0);
	int tc; cin >> tc;
	for (int i = 1; i <= tc; i++) {
		string init, val;
		int k;
		cin >> init >> k;
		for (int i = 0; i < init.length(); i++) {
			if (init[i] == '-') init[i] = '0';
			else if (init[i] == '+') init[i] = '1';
		}
		val = pancake(init, k);
		cout << "Case #" << i << ": " << val << '\n';
	}
	return 0;
}