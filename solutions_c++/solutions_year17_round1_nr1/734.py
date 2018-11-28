#include<bits/stdc++.h>
#define ms(x, y) memset(x, y, sizeof(x))
#define rep(i, a, b) for(int i = a; i <= b; i++)
#define ll long long 
using namespace std;


char s[30][30];
int r, c;

bool notall(int i) {
	rep(j, 1, c) {
		if(s[i][j] != '?')
			return true;
	}
	return false;
}

void doline(int i) {
	char firstchar = 0;
	rep(j, 1, c)
		if (s[i][j] != '?') {
			firstchar = s[i][j];
			break;
		}
	rep(j, 1, c) {
		if(s[i][j] == '?')
			s[i][j] = firstchar;
		else 
			firstchar = s[i][j];
	}
}

int main () {
	freopen("A.in", "r", stdin);
	freopen("A.out", "w", stdout);

	int tc;
	cin >> tc;
	rep(tt, 1, tc) {
		cin >> r >> c;
		rep(i, 1, r) {
			scanf("%s", s[i] + 1);
		}
		rep(i, 1, r) {
			if(notall(i))
				doline(i);
		}

		int firstline = 0;
		rep(i, 1, r) {
			if(notall(i)) {
				firstline = i;
				break;
			}
		}

		rep(i, 1, r) {
			if(!notall(i)) {
				strcpy(s[i]+1, s[firstline]+1);
			}
			else
				firstline = i;
		}
		printf("Case #%d:\n", tt);
		rep(i, 1, r) {
			rep(j, 1, c)
				printf("%c", s[i][j]);
			printf("\n");
		}
	}
	return 0;
}