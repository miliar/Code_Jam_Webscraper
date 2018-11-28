#include <cstdio>
using namespace std;

/* run this program using the console pauser or add your own getch, system("pause") or input loop */

int main(int argc, char** argv) {
	FILE *in=fopen("C-large.in","r");
	FILE *out=fopen("C-large.out","w");
	int qw;
	fscanf(in,"%d",&qw);
	for(int qwe=1;qwe<=qw;qwe++)
	{
		long long n,k;
		fscanf(in,"%lld%lld",&n,&k);
		k--;
		fprintf(out,"Case #%d: ",qwe);
		long long pow=2;
		while(pow<k) pow*=2;
		long long k1;
		if(pow==k+1) k1=pow-1;
		else {k1=pow/2-1;pow/=2;}
		long long u=n-k1;
		long long x=u/pow;
		long long z=u%pow;
		k=k-k1;
		if(k<z) x++;
		if(x==1) fprintf(out,"0 0\n");
		if(x==2) fprintf(out,"1 0\n");
		if(x>2) fprintf(out,"%lld %lld\n",x/2,x%2?x/2:x/2-1);
	}
	return 0;
}
