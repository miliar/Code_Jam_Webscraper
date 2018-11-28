#include<stdio.h>
#include<iostream>
#include<string.h>
#include<algorithm>
#include<queue>
#include<string>
#include<vector>
#include<set>
#include<math.h>
#include<map>
#define ull unsigned long long
#define ll long long
#define mp map
#define FOR(a,b) for(int i=a;i<=b;i++)
using namespace std;
#define maxn 101010

char s[100];
int main() {
	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; t++) {
		scanf("%s", s);
		printf("Case #%d: ", t);
	
		int printtt = 0;
		for (int i = 1; i < strlen(s); i++) {
			if (s[i] < s[i - 1]) {												//s[i]<s[i-1]
				if (s[i - 1] != '1') {											//·Ç1110Àà
					for (int x = i - 1; x >= 0; x--) {							
						if (x >= 1 && s[x] - 1 >= s[x - 1]) { s[x] = s[x] - 1; break; }
						else if (x == 0) { s[x] = s[x] - 1; }
						else {
							s[x] = '9';
						}
					}
				}
				else {
					printtt = 1;
					for (int z = 1; z < strlen(s); z++) {
						printf("9");
					}
					break;
				}
				for (int j = i; j < strlen(s); j++) {
					s[j] = '9';
				}
			}
		}
		
		int flag = 0;
		if (!printtt) {
			for (int i = 0; i < strlen(s); i++) {
				if (s[i] != '0' || flag) { flag = 1; printf("%c", s[i]); }
			}
		}
		puts("");

	}
	puts("");
}