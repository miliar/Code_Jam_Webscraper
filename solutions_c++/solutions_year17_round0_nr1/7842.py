#include <iostream>

using namespace std;

bool check(string s) {
	int size = s.size();
	for (int i = 0; i < size; i++) {
		if (s[i] != '+') {
			return false;
		}
	}
	return true;
}
string flip(string s, int index, int k) {
	int size = s.length();
	if (index + k > size) return "";
	for (int i = index; i < index + k; i++) {
		if (s[i] == '+') {
			s[i] = '-';
		} else {
			s[i] = '+';
		}
	}
	return s;
}

int flip_num(string s, int k) {
	int size = s.size();
	int ret = 0;
	int i;
	for (i = 0; i < size; i++) {
		if (s[i] == '-') {
			ret++;
			s = flip(s, i, k);
			if (s == "") return -1;
		}	
	}
	return ret;
		
}

int main(int argc, char *argv[]) {
	int t, k;
	string s;
	cin >> t;
	for (int i = 1; i <= t; i++) {
		cin >> s;
		cin >> k;
		string ret_s;
		int ret = flip_num(s,k);
		if (ret == -1) {
			ret_s = "IMPOSSIBLE";
		} else {
			ret_s = to_string(ret);
		}
		cout << "Case #" << i << ": " << ret_s << endl;
	}
}