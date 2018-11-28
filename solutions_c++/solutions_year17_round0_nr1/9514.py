#include<iostream>
#include<cstdio>
#include<algorithm>
#include<cmath>
#include<cstdlib>
#include<map>
#include<set>
#include<cctype>
#include<vector>
#include<string>
#include<cstring>
using namespace std;

char s[2000];
int T, k;
int main()
{
	scanf("%d",&T);
	for (int t=1; t<=T; t++) {
		scanf("%s", s);
		scanf("%d", &k);
		int ans = 0;
		int l = strlen(s);
		for (int i=0; s[i]; i++) {
			if (s[i] == '-') {
				for (int j=0; j<k; j++) {
					if (i+j >= l) {
						ans = -0x7ffffff;
						break;
					}
					s[i+j] = (s[i+j]=='+')?'-':'+';
				}
				ans += 1;
			}
			if (ans < 0)
				break;
		}
		if (ans >= 0) {
			printf("Case #%d: %d\n", t, ans);
		} else {
			printf("Case #%d: IMPOSSIBLE\n", t);
		}
	}
	return 0;
}
