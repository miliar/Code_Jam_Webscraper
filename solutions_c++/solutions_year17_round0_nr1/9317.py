#include<iostream>
#include<string>
using namespace std;

int main(){
	int n;
	cin >> n;
	for (int i = 1; i <= n; ++i) {
		string s;
		int k,j= 0, count = 0;
		bool flag = true;
		cin >> s;
		cin >> k;
		for (; j <= (int)s.size() - k; ++j){
			if (s[j] == '+') continue;
			count++;
			for (int p = 0; p < k; ++p) {
				s[p + j] = s[p + j] == '+' ? '-' : '+';
			}
		}
		for (; j < s.size(); ++j) {
			if (s[j] == '-') {
				flag = false;
				break;
			}
		}
		if (flag) {
			cout << "Case #" << i << ": " << count << endl;
		}
		else {
			cout << "Case #" << i << ": " << "impossible" << endl;
		}
	}
	return 0;
}