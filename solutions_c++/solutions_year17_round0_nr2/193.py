#include <bits/stdc++.h>

using namespace std;

const int MAXL = 1E3 + 10;

char s[MAXL];

int main(){
	int cas;
	scanf("%d", &cas);
	for (int casi = 1; casi <= cas; ++casi){
		printf("Case #%d: ", casi);

		scanf("%s", s);
		int n = strlen(s);
		int r = 1;
		for (; r < n && s[r - 1] <= s[r]; ++r);
		if (r < n){
			for (int i = n - 1; i >= r; --i)
				s[i] = '9';				
			for (--r; r > 0 && s[r - 1] == s[r]; --r)
				s[r] = '9';
			--s[r];
		}
		puts(s[0] == '0' ? s + 1 : s);
	}
	return 0;
}
