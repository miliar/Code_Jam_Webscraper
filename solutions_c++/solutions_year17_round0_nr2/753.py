#include<bits/stdc++.h>
using namespace std;
char st[999];
int main() {
	int tests;
	scanf("%d", &tests);
	for(int qq(1); qq <= tests; qq++) {
	
		scanf("%s", st);
		int len(strlen(st));
		for(;;) {
			bool flag(false);
			for(int i(0); i < len - 1; i++) {
				if(st[i] > st[i + 1]) {
					st[i]--;
					for(int j(i + 1); j < len; j++) {
						st[j] = '9';
					}
					flag = true;
					break;
				}
			}
			if(flag == false)
				break;
		}
		for(int i(0); i < len; i++) {
			if(st[i] != '0') {
				printf("Case #%d: ", qq);
				puts(st + i);
				break;
			}
		}
	}
}
