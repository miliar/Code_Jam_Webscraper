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
char s[1005];
int main() {
	int t;
	scanf("%d", &t);
	for (int T = 1; T <= t; T++) {
		int flag = 1;
		int cnt = 0;
		int k;
		scanf("%s%d",s, &k);
		//for (int i = 0; i < s.length(); i++)vis[i] = 0;

		printf("Case #%d: ", T);
		int len = strlen(s);
		for (int i = 0; i < len; i++) {
			if (s[i] == '-') {
				cnt++;
				if (i + k - 1 >= len) { flag = 0; break; }
				for (int j = i; j <= i + k - 1; j++) {
					if (s[j] == '-')s[j] = '+'; else { s[j] = '-'; }
				}
			}
		}
		//cout << s << endl;
		if (flag == 0)printf( "IMPOSSIBLE\n");
		else {
			printf("%d\n", cnt);
		}


	}
}