#include <cstdio>
#include <algorithm>
#include <vector>
#include <cmath>
#include <cstring>
#include <string>
#include <map>
#include <queue>
#include <set>

#define LL long long int
#define FOR(i, s, e) for (int i=(s); i<(e); i++)
#define FOE(i, s, e) for (int i=(s); i<=(e); i++)
#define CLR(x, a) memset(x, a, sizeof(x))

using namespace std;

int test, n, k, ret, fail;
char s[1005];

void solve(int test) {
	scanf("%s%d", s, &k);
	n = strlen(s);
	ret = fail = 0;
	FOR(i, 0, n - k + 1)
		if (s[i] == '-') {
			ret++;
			FOR(j, 0, k)
				s[i + j] = (s[i + j] == '-') ? '+' : '-'; 
		}
	FOR(i, n - k + 1, n) if (s[i] == '-') fail = 1;
	
	printf("Case #%d: ", test); 
	if (fail) printf("IMPOSSIBLE\n");
	else printf("%d\n", ret);
}

int main(){
	scanf("%d", &test);
	FOE(i, 1, test) solve(i);
	return 0;
}
