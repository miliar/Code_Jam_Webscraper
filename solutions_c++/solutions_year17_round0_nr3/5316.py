#include <stdio.h>
#include <vector>
#include <string>
using namespace std;
FILE *in,*out;
int main() {
	in = fopen("in.txt","r");
	out = fopen("out.txt","w");
	int t;
	long long int n,k;
	fscanf(in,"%d",&t);
	for(int i=1;i<=t;i++) {
		fscanf(in,"%lld%lld",&n,&k);
		long long int z(1);
		long long int m(0);
		while (k > z) {
			k -= z;
			if (n%2 == 0) m += z;
			z *= 2;
			n = (n - 1) / 2;
		}
		//fprintf(out,"Case #%d: n%lld m%lld k%lld z%lld\n",i,n,m,k,z);
		long long int r = n;
		if (k <= m) r++;
		fprintf(out,"Case #%d: %lld %lld\n",i,r/2,(r-1)-r/2);
	}
	fclose(in);
	fclose(out);
	return 0;
}

