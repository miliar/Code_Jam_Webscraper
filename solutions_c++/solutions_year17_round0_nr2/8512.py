#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <algorithm>
using namespace std;

bool Check(int x)
{
	int last = 9;
	while (x > 0) {
		if (x % 10 > last) return false;
		last = x % 10; x /= 10;
	}
	return true;
}

int main()
{
	freopen("B-small-attempt0.in", "r", stdin);
	freopen("B-small-attempt0.out", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int cas = 1; cas <= T; cas++) {
		int n;
		scanf("%d", &n);
		for (int i = n; i >= 0; i--) 
			if (Check(i)) {
				printf("Case #%d: %d\n", cas, i);
				break;
			}
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}
