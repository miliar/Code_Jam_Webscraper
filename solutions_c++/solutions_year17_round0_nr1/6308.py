#include <cstdio>
#include <cstring>
using namespace std;

int main() {
	int j,i,len,t,k, Case = 1, ans;
	bool happy;
	char a[1001];
	scanf("%d",&t);
	while(Case <= t) {
		scanf("%s%d", a, &k);
		happy = true;
		len = strlen(a);
		ans = 0;
		for(i = 0; i + k <= len ; i++) {
			if(a[i] == '+') continue;
			else {
				ans++;
				for(j = i ; j - i < k ; j++) 
					if(a[j] == '+') a[j] = '-';
					else a[j] = '+';
			}
		}
		for(i=0; i < len; i++ ) 
			if(a[i] == '-') {
				happy = false;
				break;
			}
		printf("Case #%d: ", Case++);
		if(happy) printf("%d\n", ans);
		else printf("IMPOSSIBLE\n");
	}
	return 0;
}
