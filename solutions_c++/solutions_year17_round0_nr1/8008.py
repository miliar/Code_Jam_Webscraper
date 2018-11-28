#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;

void fhihi (int ind, int N, char s[], int k){
	int i, ans=0, j;
	bool solved = 1;
	for (i=0; i<N-k+1; i++) {
		if (s[i] == '-'){
			for (j=i; j<i+k; j++) {
				if (s[j] == '-') s[j] = '+';
				else s[j] = '-';
			}
			ans++;
		}
	}
	for (i=0; i<N; i++) if (s[i] == '-') solved = 0;
	if (solved) printf ("Case #%d: %d\n", ind, ans);
	else printf ("Case #%d: IMPOSSIBLE\n", ind);
}

int main() {
	int n, N, i, j, k;
	char s[1001];
	scanf ("%d", &n);
	for (i=1; i<=n; i++){
		//scanf ("%d\n", &N);
		//for (j=0; j<N; j++) scanf ("%c", &s[j]);
		scanf ("%s", &s);
		scanf ("%d", &k);
		fhihi(i, strlen(s), s, k);
	}

	return 0;
}