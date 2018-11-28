#include <cassert>
#include <cstdio>
#include <algorithm>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <queue>
#define N 11
#define Q (1<<N)
#define oo (0xfffffffful)
#define BIT(k) (1ULL<<(k))
#define MASK(k) (BIT(k)-1ULL)
#include <vector>
using namespace std;

long long n;

int main() {
	int i,j,k,ts,cs = 0,m;
	for ( scanf("%d",&ts); ts-->0; ) {
		printf("Case #%d: ",++cs);
		scanf("%lld",&n);
		char s[0x400];
		sprintf(s,"%lld",n);
		m = strlen(s);
		for ( i = 0; i < m-1 && s[i] <= s[i+1]; ++i );
		if ( i == m-1 ) {
			printf("%lld\n",n);
			continue ;
		}
		for ( j = i; j >= 1 && s[j-1] == s[j]; --j );
		if ( s[i] == '1' ) {
			for ( i = 0; i < m-1; ++i )
				putchar('9');
			puts("");
		}
		else {
			for ( k = 0; k < j; ++k ) putchar(s[k]);
			for ( putchar(s[j]-1), k = j+1; k < m; ++k )
				putchar('9');
			puts("");
		}
	}
	return 0;
}

