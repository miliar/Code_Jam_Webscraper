#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;
 
void fhihi (){
	int i, N, D, k, s;
	double ans;
	scanf ("%d %d", &D, &N);
	for (i=0; i<N; i++){
		scanf ("%d %d", &k, &s);
		if (i==0) ans = (double)D/((D-k)/s);
		if ((double)D/((D-k)/s) < ans) ans = (double)D/((D-k)/s);
	}
	printf ("%lf\n", ans);

}
 
int main() {
	int n, N, i, j, k;
	char s[1001];
	scanf ("%d", &n);
	for (i=1; i<=n; i++){
		printf ("Case #%d: ", i);
		//scanf ("%d\n", &N);
		//for (j=0; j<N; j++) scanf ("%c", &s[j]);
		//scanf ("%s", &s);
		//scanf ("%d", &k);
		//fhihi(i, strlen(s), s, k);
		fhihi();
	}
 
	return 0;
}
