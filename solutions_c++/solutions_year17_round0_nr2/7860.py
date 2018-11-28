#include <bits/stdc++.h>
using namespace std;

string fun() {
	string s;
	cin >> s;
	string ans = "";
	int len = s.length();
	vector<int> v(len);
	for(int i=0;i<len;i++) {
		v[i] = s[i]-'0';
	}
	for(int i=1;i<len;i++) {
		if(v[i] < v[i-1]) {
			for(int j=i;j<len;j++) {
				v[j] = 9;
			}
			int j;
			for(j=i-1;(j>0) && (v[j]==v[j-1]);j--) {
				v[j] = 9;
			}
			v[j]--;
			break;
		}
	}
	if(v[0])
		ans += to_string(v[0]);
	for(int i=1;i<len;i++) {
		ans += to_string(v[i]);
	}
	return ans;
}

int main() {
	int n;
	cin >> n;
	for(int i=1;i<=n;i++) {
		cout << "Case #" << i << ": " << fun() << endl;
	}
	return 0;
}