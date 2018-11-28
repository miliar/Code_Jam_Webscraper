//#define _CRT_SECURE_NO_WARNINGS

#include <cstdio>
#include <cstring>

int T;

char A[1010];
int n, k;
int ans;

int main ()
{
//	freopen ("input.txt", "r", stdin);
//	freopen ("output.txt", "w", stdout);

	scanf("%d", &T);

	int TT;
	for(TT=1; TT<=T; TT++){
		scanf("%s", A);
		scanf("%d", &k);
		ans = 0;

		n = strlen ( A );

		int i, j;
		for(i=0; i<n-k+1; i++){
			if ( A[i] == '-' ){
				ans ++;
				for(j=0; j<k; j++){
					if ( A[i+j] == '+' ) A[i+j] = '-';
					else A[i+j] = '+';
				}
			}
		}

		for(i=0; i<n; i++){
			if ( A[i] == '-' ){
				printf("Case #%d: IMPOSSIBLE\n", TT);
				break;
			}
		} if ( i == n ) printf("Case #%d: %d\n", TT, ans);

	}

	return 0;
}