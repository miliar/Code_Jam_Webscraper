#include <cstdio>
#include <algorithm>
#include <vector>
#include <cstring>
#define LL long long
#define fi(a, b, c) for(int a = (b); a < (c); a++)
#define FI(a, b, c) for(int a = (b); a <= (c); a++)
using namespace std;

int t, k;
char s[1005];

void solve(int tc){
	scanf("%s %d", s, &k);
	int n = strlen(s);
	int ans = 0;
	
	fi(i, 0, n - k + 1){
		if(s[i] == '-'){
			fi(j, i, i + k){
				if(s[j] == '-') s[j] = '+';
				else s[j] = '-';
			}
			ans++;
		}
	}
	
	fi(i, 0, n) if(s[i] == '-') ans = -1;
	
	printf("Case #%d: ", tc);
	if(ans < 0) puts("IMPOSSIBLE");
	else printf("%d\n", ans);
}

int main(){
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w+", stdout);
	scanf("%d", &t);
	FI(z, 1, t) solve(z);
}
