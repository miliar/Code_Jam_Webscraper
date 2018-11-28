#include <bits/stdc++.h>


#define puba push_back
#define ff first
#define ss second
#define pii pair <int, int>


using namespace std;


typedef long long LL;


LL overfill(LL val, int d, int times) {
	for (int i = 0; i < times; ++i) {
		val *= 10;
		val += d;		
	}
	return val;
}


string int_to_string(LL val) {
	if (val == 0) return "0";
	string ret;

	while (val > 0) {
		ret += '0' + val % 10;
		val /= 10;
	}
	reverse(ret.begin(), ret.end());
	return ret;
}

LL add(LL val, int d) {
	return val * 10 + d;
}


int main() {
	int t;
	cin >> t;
	for (int q = 1; q <= t; ++q) {
		cout << "Case #" << q << ": ";
		
		string s;
		LL val;
		cin >> val;
		s = int_to_string(val);

		int n = s.size();
		vector < int > num (n);
		for (int i = 0; i < n; ++i) num[i] = s[i] - '0';

		LL cur = 0;
		for (int i = 0; i < n; ++i) {
			int d = num[i];
			if (overfill(cur, d, n - i) > val) {
				cur = overfill(add(cur, d - 1), 9, n - i - 1);
				break;
			}
			else {
				cur = add(cur, d);
			}
		}

		cout << cur << endl;
	}

	
	return 0;
}