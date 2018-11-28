#include <stdio.h>
#include <vector>
#include <set>
#include <queue>
#include <algorithm>
using namespace std;
#define ll longlong

int main(void) {
	int T;
	scanf("%i", &T);
	for (int i=0;i<T;i++) {
		int D,N;
		scanf("%i %i",&D, &N);
		int K[1000], S[1000];
		for (int j=0;j<N;j++) {
			scanf("%i %i",&K[j], &S[j]);
		}
		double cas, maxcas=0.000001;
		for (int j=0;j<N;j++) {
			cas = (double)(D-K[j])/(double)S[j];
			if (cas>maxcas)
				maxcas = cas;
		}
		double vysl = (double)D/maxcas;
		printf("Case #%i: %f\n",i+1,vysl);
	}
    return 0;
}
