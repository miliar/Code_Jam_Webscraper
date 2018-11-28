
// (C) Alvaro Salmador 2017

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
//typedef unsigned long long ull;


int N=0,D=0;

int S[10000], K[10000];


bool get_input()
{
	static int T = -1;
	
	if (T<0)
		scanf("%d", &T);
	
	if (T>0)
	{
		--T;

		if (scanf("%d %d", &D, &N)!=2)
			return false;

		int i, ki, si;
		FOR(i, 0, N) {
			scanf("%d %d", &K[i], &S[i]);
		}

		//while(fgetc(stdin)!='\n') ;

		/*int i;
		for(i=0; i<N; ++i)
		{
			fgets(buffer, 199, stdin);

		}*/

		return true;
	}
	else
		return false;
}


int main()
{
//	freopen("A.txt","r",stdin);
	//freopen("A-small-attempt0.in","r",stdin);freopen("A-small-attempt0.out","w",stdout);
//	freopen("A-small-attempt1.in","r",stdin);freopen("A-small-attempt1.out","w",stdout);
	freopen("A-large.in","r",stdin);freopen("A-large.out","w",stdout);

	for(int ncase=1; get_input(); ++ncase)
	{
		//fprintf(stderr, "\nCase #%d\n", ncase); fflush(stderr);
		printf("Case #%d: ", ncase);

		int i;
		double maxt=0.f;
		FOR(i, 0, N) {
			double t = (D-K[i])/(double)S[i];
			if (t>maxt) maxt=t;
		}
		printf("%f\n", (double)D/maxt);

	}

	return 0;
}