
#include <cstdio>
#include <algorithm>
#include <cstring>
using namespace std;

typedef long long i8;
char buf[255];

void solve() {
	i8 n, fix;
	scanf("%lld", &n);

	while (1) {
		sprintf(buf, "%lld", n);
		int bad=-1;
		for (int i=1; buf[i]; i++)
			if (buf[i]<buf[i-1]) {
				bad=i;
				break;
			}
		if (bad<0) break;
		sscanf(buf+bad, "%lld", &fix);
		n-=fix+1;
	}
	
	printf("%lld\n", n);
}

main() {
	int ccnt;
	scanf("%d", &ccnt);
	for (int cs=1; cs<=ccnt; cs++) {
		printf("Case #%d: ", cs);
		solve();
	}
}
