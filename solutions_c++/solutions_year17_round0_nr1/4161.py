#include <stdio.h>
#include <string.h>

int main(void) {

	int t;
	scanf("%d", &t);
	for( int cnt=0; cnt<t; cnt++ ) {

		printf("Case #%d: ", cnt+1);

		int ans = 0, k;
		bool arr[1000];
		char s[1000];
		scanf("%s%d", s, &k);

		int size = strlen(s);
		for( int i=0; i<size; i++) {
			if( s[i] == '+' ) arr[i] = 1;
			else arr[i] = 0;
		}

		for( int i=0; i<=size-k; i++ ) {
			if( arr[i] ) continue;
			ans++;
			for( int j=0; j<k; j++ )
				arr[i+j] = !arr[i+j];
		}

		// check illegal
		bool imp = false;
		for( int i=size-k; i<size; i++ )
			if( !arr[i] ) {
				imp = true;
				break;
			}
		
		if( imp ) printf("IMPOSSIBLE\n");
		else printf("%d\n", ans);

	}

	return 0;
}