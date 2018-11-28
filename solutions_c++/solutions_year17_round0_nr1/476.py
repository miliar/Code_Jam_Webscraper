#include <cstdio>
#include <cstring>

int solve(const char* s, int len, int k)
{
	int cnt = 0;
	bool* b = new bool[len];
	for( int i = 0; i < len; i++ ) {
		b[i] = (s[i] == '+');
	}
	for( int i = 0; i <= len - k; i++ ) {
		if( !b[i] ) {
			for( int j = i; j < i + k; j++ ) {
				b[j] = !b[j];
			}
			cnt++;
		}
	}
	for( int i = len - k; i < len; i++ ) {
		if( !b[i] ) {
			return -1;
		}
	}
	delete[] b;
	return cnt;	
}


int main() {
	int t; // test_cases
	char s[1001]; // pancake + happy up, - blank up
	int k; // pancake flipper size
	scanf("%d", &t);
	for( int i = 1; i <= t; i++ ) {
		scanf( "%s %d", s, &k );
		while( getchar() != '\n' );
		int len = strlen(s);
		printf("Case #%d: ", i);
		int result = solve(s, len, k);
		result < 0 ? printf("IMPOSSIBLE") : printf("%d", result);
		printf("\n");
	}
	return 0;
}