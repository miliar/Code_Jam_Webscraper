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

int main() {
	int t,n,k;
	FILE *in = fopen("input.txt", "r");
	FILE *out = fopen("output.txt","w");
	
	double p[55],u;
	fscanf(in,"%d", &t);
	for(int i=0; i<t; i++) {
		fscanf(in,"%d %d", &n, &k);
		fscanf(in,"%lf",&u);
		for(int j=0; j<n; j++) {
			fscanf(in,"%lf",p+j);
		}
		p[n++] = 1; // attenzione
		sort(p,p+n);
		int ind = 0;
		double cur = 0;
		for(; ind<n; ind++) {
			if((p[ind]-cur)*ind<=u) {
				u -= (p[ind]-cur)*ind;
				cur = p[ind];
			} else {
				cur += u/ind;
				break;
			}
		}
		double prodotto = 1;
		for(int j=0; j<ind; j++)
			prodotto *= cur;
		for(int j=ind; j<n; j++)
			prodotto *= p[j];
		fprintf(out,"Case #%d: %lf\n",i+1,prodotto);
	}
	return 0;
}
