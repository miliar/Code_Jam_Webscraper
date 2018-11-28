
// (c) Alvaro Salmador 2017

#pragma warning(disable : 4996)
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <algorithm>
/*#include <string>
#include <list>
#include <vector>
#include <map>*/

using namespace std;

#define FOR(__fvar,__fini,__fend) for(__fvar=__fini; __fvar<__fend; ++__fvar)
#define REP(__repi,__repn) for(__repi=0; __repi<__repn; ++__repi)

#undef M_PI
#define M_PI 3.14159265358979323846  
const double SQRT2 = sqrt(2.0);
const double Pi = M_PI;
//typedef long long ll;
typedef unsigned long long ull;


ull N=0;
int T = -1;


bool get_input()
{	
	if (T<0)
		scanf("%d", &T);
	
	if (T>0)
	{
		--T;

		if (scanf("%llu", &N)==1)
			return true;
	}
	return false;
}

bool istidy(ull r) 
{
	char b[20];
	b[0]=0;
	int i=0;

	while(r>0) {
		b[i++] = r % 10;
		r /= 10;
	}
	if (i>0) --i;

	if (i==0) return true;
	char d=0;
	for(; i>=0; --i) {
		if (d>b[i])
			return false;
		d=b[i];
	}
	return true; 
}

ull solve() {
	ull r;
	for(r=N; r>19; --r)
		if (istidy(r)) break;
	return r;
}

ull solve2() {
	ull r=N;
	char b[20];
	b[0]=0;
	int i=0;

	while(r>0) {
		b[i++] = r % 10;
		r /= 10;
	}
	if (i>0) --i;

	// 119911 => 118999
	// 777711 => 699999
	// 1454 => 1449
	// 14554 => 14499
	if (i==0) return N;

	char d=0;
	for(int j=i; j>=0; --j) {
		if (d>b[j]) {
			do { 
				j++; 
			} while (j<=i && b[j]==d);
			j--;
			_ASSERT(b[j]==d);
			b[j]--;
			for(j--; j>=0; --j) 
				b[j]=9;
			break;
		}
		d=b[j];
	}

/*printf("%llu: solve2=",r);
for(int j=i; j>=0; --j)
	printf("%d", b[j]);
printf("\n");*/
	ull k=1;
	r=0;
	for(int j=0; j<=i; ++j) {
		r += b[j]*k;
		k *= 10;
	}

	return r; 
}

int main()
{
	for(int ncase=1; get_input(); ++ncase)
	{
		//fprintf(stderr, "\nCase #%d\n", ncase); fflush(stderr);
		
		//printf("Case #%d: N=%llu r=%llu\n", ncase, N, solve2());
		printf("Case #%d: %llu\n", ncase, solve2());
	}

	return 0;
}

