#include <bits/stdc++.h>

using namespace std;

int main()
{
	freopen("input2Large.txt", "r", stdin);
	freopen("small_aOutputLarge.txt", "a", stdout);
	int tc;
	cin >> tc;
	string s;
	int k;
	for(int i = 1; i <= tc; i++) {
		cin >> s >> k;
		int len = s.size();
		int count = 0;
		int moves = 0;
		int flag = 0;
		for(int j = 0; j < len; j++) {
			if(s[j] == '-') {
				moves++;
				for(int l = j; l < k + j && j + k <= len ; l++) {
					if(s[l] == '-')
						s[l] = '+';
					else if(s[l] == '+')
						s[l] = '-';
				}
			}
			else count++;
		}

		for(int j = 0; j < len; j++) {
			if(s[j] == '-'){
				flag++;
				break;
			}
		}
		if(flag != 0) {
			printf("Case #%d: IMPOSSIBLE\n", i);
		}
		else if(count == 0) {
			printf("Case #%d: 0\n", i);
		}
		else printf("Case #%d: %d\n", i, moves);
	}


	return 0;
}