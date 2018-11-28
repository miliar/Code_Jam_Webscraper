#include <bits/stdc++.h>

using namespace std;
typedef long long LL;

const int MAXL = 20;

char str[MAXL];
bool test(int idx, int L, int num) {
	for (int i = idx; i < L; i++) {
		if (str[i] - '0' > num) {
			return true;
		} else if (str[i] - '0' < num) {
			return false;
		}
	}
	return true;
}

int main() {
  freopen("input", "r", stdin);
  freopen("output", "w", stdout);
  int T; cin >> T;
  for (int kase = 1; kase <= T; kase++) {
  	memset(str, 0, sizeof str);
  	cin >> str;
  	int L = strlen(str);

  	string ret = "";
  	for (int i = 0; i < L; i++) {
  		int current = str[i] - '0';
  		if (!test(i + 1, L, current)) {
  			ret = (ret + (char)(str[i] - 1));
  			for (int j = i + 1; j < L; j++) {
  				ret = ret + "9";
  			}
  			break;
  		} else {
  			ret = ret + str[i];
  		}
  	}
  	cout << "Case #" << kase << ": ";
  	bool leading = true;
  	for (int i = 0; i < L; i++) {
  		if (leading) {
  			if (ret[i] != '0') {
  				leading = false;
  				cout << ret[i];
  			}
  		} else {
  			cout << ret[i];
  		}
  	}
  	cout << endl;
  }
  return 0;
}
