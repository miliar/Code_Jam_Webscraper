#include <iostream>
#include <vector>

using namespace std;

string solve() {
	string s;
	vector<int> a;
	cin >> s;
	
	for (int i = 0; i < s.size(); i++)
		a.push_back(s[i] - '0');
	int pos = 0, flag = 0;
	for (int i = 1; i < a.size(); i++) {
		if (a[i] > a[i - 1]) pos = i;
		if (a[i] < a[i - 1]) {
			flag = 1;
			break;
		}
	}
	if (flag == 0) {
		return s;
	}else {
	   s[pos] -= 1;
	   for (int i = pos + 1; i < s.size(); i++)
		   s[i] = '9';
	   if (s[0] != '0') return s;
	   else return s.substr(1);
	}
		
}

int main() {
	int T;
	cin >> T;
	for (int i = 1; i <= T; i++) {
		cout << "Case #" << i << ": " << solve() << endl;
	}
	return 0;
}
