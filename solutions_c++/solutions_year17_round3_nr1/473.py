#include <cstdio>
#include <vector>
#include <algorithm>
#include <climits>
#include <cstdlib>
#include <queue>
#include <map>
#define ii pair<int,int>
#define ll long long
const long double PI=3.1415926535;

using namespace std;

long double r[1005],h[1005];

bool cmp(int a, int b) {
	return r[a]*h[a]>r[b]*h[b];
}

int main() {
	int t,n,k;
	FILE *in = fopen("input.txt", "r");
	FILE *out = fopen("output.txt","w");
	
	int ordinati[1005];
	int rtmp,htmp;
	long double massimo,corrente;
	fscanf(in,"%d", &t);
	for(int i=0; i<t; i++) {
		fscanf(in, "%d %d", &n, &k);
		for(int j=0; j<n; j++) {
			fscanf(in, "%d %d", &rtmp,&htmp);
			r[j] = rtmp;
			h[j] = htmp;
			ordinati[j] = j;
		}
		sort(ordinati,ordinati+n, cmp);
		massimo = 0;
		for(int r0 = 0; r0<n; r0++) {
			corrente = PI*r[r0]*r[r0]+2*PI*h[r0]*r[r0];
			int contatore = 1, ind = 0;
			while(contatore<k) {
				if(ordinati[ind]!=r0) {
					corrente += 2*PI*h[ordinati[ind]]*r[ordinati[ind]];
					contatore++;
				}
				ind++;
			}
			if(corrente>massimo)
				massimo = corrente;
		}
		fprintf(out,"Case #%d: %lf\n",i+1,(double) massimo);
		
	}
	return 0;
}
