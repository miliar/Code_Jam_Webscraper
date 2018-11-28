#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <stack>
#include <queue>
#include <map>
#include <set>
#define PB push_back
#define MP make_pair
#define X first
#define Y second
#define lc (k<<1)
#define rc ((k<<1)|1)
#define mi ((l+r)>>1)
#define fk puts("fuck!")
using namespace std;
typedef long long ll;
typedef unsigned long long ull;

int k;
char str[1007];

int main()
{
	int T; scanf("%d",&T);
	for(int cas=1; cas<=T; ++cas) {
		scanf("%s %d", str+1, &k);
		int ans = 0, len = strlen(str+1);
		for(int i=1; i<=len; i++) {
			if(str[i]=='+') continue;
			if(str[i]=='-') {
				if(i > len-k+1) {
					ans = -1;
					break;
				} else {
					ans++;
					for(int j=0; j<k; j++) {
						if(str[i+j] == '+')
							str[i+j] = '-';
						else str[i+j] = '+';
					}
				}
			}
		}
		printf("Case #%d: ", cas);
		if(ans == -1) puts("IMPOSSIBLE");
		else printf("%d\n", ans);
	}
	return 0;
}





