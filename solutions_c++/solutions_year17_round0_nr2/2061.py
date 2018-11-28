#include<bits/stdc++.h>
#define rep(i, a, b) for(int i = a; i <= b; i++)
#define ll long long
#define ms(x, y) memset(x, y ,sizeof(x))
using namespace std;


char s[20];

int main () {
	freopen("A.in", "r", stdin);
	freopen("A.out", "w", stdout);
	int tc;
	cin >> tc;
	rep(tt, 1, tc) {
		scanf("%s", s + 1);
		int n = strlen(s + 1);
		for(int i = n; i >= 2; i--) {
			if(s[i] < s[i-1]) {
				s[i-1] = s[i-1] - 1;
				for(int j = i; j <= n; j++)
					s[j] = '9';
			}
		}
		printf("Case #%d: ", tt);
		rep(i, 1, n) {
			if(i == 1 && s[i] == '0')
				continue;
			printf("%c", s[i]);
		}
		cout << endl;
	}
	return 0;
}