#include <cstdio>
#include <set>

using namespace std;

typedef long long int lld;

lld lim, ans = 0;
void gen(int i = 0, int last = 0, lld num = 0ll) {
	if(num && num <= lim && num > ans) ans = num;
	if(i == 18) return;
	for(int j = last; j <= 9; ++j)
		gen(i+1, j, 10*num + j);
}

int main() {
	int t;
	scanf("%d", &t);
	for(int cas = 1; cas <= t; ++cas) {
		scanf("%lld", &lim);
		ans = 0;
		gen();
		printf("Case #%d: %lld\n", cas, ans);
	}
	return 0;
}