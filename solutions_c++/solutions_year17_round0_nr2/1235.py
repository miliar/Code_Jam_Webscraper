# include <cstdio>
# include <cstring>
using namespace std;

char a[1200];
int main(){ 
	int T, cas = 0; scanf("%d", &T);
	while(T--) {
		scanf("%s", a);
		printf("Case #%d: ", ++cas);
		int n = strlen(a);
		int r = 0;
		for(int i = 1; i < n; ++i) 
			if(a[i] >= a[i - 1]) ++r;
		if(r == n - 1) { puts(a); continue; }
		int last = -1;
		for(int i = 1; i < n; ++i) {
			if(a[i] > a[i-1]) last = i;
			if(a[i] < a[i-1]) break;
		}
		if(last == -1) {
			if(a[0] == '1') {
				n -= 1;
				for(int i = 0; i < n; ++i) putchar('9'); puts("");
			} else {
				a[0] -= 1;
				for(int i = 1; i < n; ++i) a[i] = '9';
				puts(a);
			}
		} else {
			a[last] -= 1;
			for(int i = last + 1; i < n; ++i) a[i] = '9';
			puts(a);
		}
	}
	return 0;
}

