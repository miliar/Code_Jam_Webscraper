#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <iostream>

using namespace std;
int T;
int main() {
	cin >> T;
	for(int cas = 1; cas <= T; ++cas) {
		string s;
		cin >> s;
		printf("case #%d: ",cas);
		int lastpos = 0;
		bool flag = true;
		for(int i = 0; i < s.size(); ++i) {
			if(i == 0 || s[i] > s[i - 1]) {
				lastpos = i;
			}
			if(i < s.size() - 1 && s[i] > s[i + 1]) {
				for(int j = 0; j < lastpos; ++j) {
					putchar(s[j]);
				}
				if(s[lastpos] > '1') 
					putchar(s[lastpos] - 1);
				for(int j = lastpos + 1; j < s.size(); ++j)
					putchar('9');
				flag = false;
				break;
			}
		}
		if(flag)
			cout << s;
		printf("\n");
	}
	return 0;
}