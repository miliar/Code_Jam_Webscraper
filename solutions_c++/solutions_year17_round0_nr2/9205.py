#include"bits/stdc++.h"
using namespace std;

bool istidy(string &s, int &p) {
	int i;
	for (i = 1; i < s.size(); i++) {
		if (s[i - 1] - 48 > s[i] - 48) {
			p = i - 1;
			break;
		}
	}
	if (i >= s.size())
		return true;
	else {
		while (p > 0 && s[p - 1] == s[p])
			p--;
		return false;
	}
}

int main(int argc, char const *argv[]) {
#ifndef ONLINE_JUDGE
	freopen("in.txt", "r", stdin);
	freopen("op.txt","w",stdout);
#endif

	int t , c =1;
	cin >> t;

	while (c<=t) {
		string n;
		cin >> n;
		int p;
		cout << "Case #" << c<< ": ";
		if (istidy(n, p)) {
			cout << n << endl;
		} else {
			for (int i = 0; i <p; i++)
				cout << n[i];
			if (n[p] - 1 != '0')
				cout <<char( n[p]-1);
			for (int i = p + 1; i < n.size(); i++)
				cout << 9;
			cout << endl;
		}
		c++;
	}
	return 0;
}
