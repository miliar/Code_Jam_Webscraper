#include <stdio.h>
#include <vector>
#include <set>
#include <queue>
#include <algorithm>
using namespace std;
#define ll longlong

int E[1000], S[1000];
int N,Q;
int D[1000];
double cache[1000][1000];
double cas(int w, int k);


int main(void) {
	int T;
	scanf("%i", &T);
	for (int i=0;i<T;i++) {
		scanf("%i %i",&N, &Q);
		for (int j=0;j<N;j++) {
			scanf("%i %i",&E[j],&S[j]);
		}
		int x;
		for (int j=0;j<N;j++) {
			for (int k=0;k<N;k++) {
			scanf("%i",&x);
			if (k==j+1)
				D[j]=x;
			}
		}
		int U,V;
		for (int j=0;j<Q;j++) {
			scanf("%i %i",&U,&V);
		}
		for (int j=0;j<1000;j++) {
			 for (int k=0;k<1000;k++)
				 cache[j][k]=-1;
		}
		double vysl=cas(0,0);
		printf("Case #%i: %.9f\n",i+1,vysl);
	}
    return 0;
}

double cas(int w, int k) {
	if (w>=N-1)
		return 0;
	else if (cache[w][k]!=-1)
		return cache[w][k];
	int urazil=0;
	for (int j=k;j<w;j++)
		urazil=urazil+D[j];
	int distance=E[k]-urazil;
	if (D[w]>distance)
		return cache[w][k]=cas(w+1,w)+(double)D[w]/(double)S[w];
	else
		return cache[w][k]=min(cas(w+1,w)+(double)D[w]/(double)S[w],cas(w+1,k)+(double)D[w]/(double)S[k]);
}
