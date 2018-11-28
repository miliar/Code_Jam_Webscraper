#define _CRT_SECURE_NO_WARNINGS

#include <cstdio>
#include <cstring>

int T;

char A[1010];
int n, k;
int ans;

int main ()
{
	freopen ("input.txt", "r", stdin);
	freopen ("output.txt", "w", stdout);

	scanf("%d", &T);

	int TT, i, j;
	for(TT=1; TT<=T; TT++){
		scanf("%s", A);
		n = strlen ( A );

		for(;;){
			for(i=0; i<n-1; i++){
				if ( A[i] > A[i+1] ){
					A[i] --;
					for(j=i+1; j<n; j++) A[j] = '9';
					break;
				}
			}

			if ( i == n-1 ) break;
		}

		printf("Case #%d: ", TT);
		for(i=0; i<n; i++) if ( A[i] != '0' ) printf("%c", A[i]);
		printf("\n");
	}

	return 0;
}