#include<iostream>
#include<cstdio>
#include<string>
using namespace std;
int T;
string S;

int main()
{
	freopen("B-small-attempt1.in", "r", stdin);
	freopen("B-small-attempt1.out", "w", stdout);
	cin >> T;
	for (int now_case = 1;now_case <= T;++now_case) {
		cin >> S;
		int len = S.size();
		int index;
		for (index = 1;index < len;++index) {
			if (S[index] < S[index - 1]) {
				for (int i = index;i < len;++i)
					S[i] = '9';
				break;
			}
		}
		if (index < len) {
			for (--index;index > 0 && S[index] == S[index - 1];--index) {
				S[index] = '9';
			}
			if (--S[index] == '0') {
				for (;index > 0;--index) {
					S[index] = '9';
				}
				S[0] = '0';
			}
		}
		cout << "Case #" << now_case << ": ";
		if (S[0] != '0') cout << S;
		else if (len > 1) cout << S.substr(1);
		else cout << 0;
		cout << '\n';
	}
	return 0;
}