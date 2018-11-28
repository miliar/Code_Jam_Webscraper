

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


int K=0;
char S[1010];

bool get_input()
{
	static int T = -1;

	if (T<0)
		scanf("%d", &T);
	
	if (T>0)
	{
		--T;
		scanf("%s %d", S, &K);
		return true;
	}
	else
		return false;
}

void flipK(int i) {
	int j;
	for(j=i; j<i+K; ++j)
		if (S[j]=='-') S[j]='+'; else S[j]='-';
}

int solve() {
	int n=0;
	int i=0, j=0, len=strlen(S);

	for(i=0; S[i]!=0; ++i) {
		if (S[i]=='-') {
			if (i>len-K)
				return -1;
			flipK(i);
			n++;
		}
	}
	return n;
}

int main()
{

	for(int ncase=1; get_input(); ++ncase)
	{
		//fprintf(stderr, "\nCase #%d\n", ncase); fflush(stderr);
		printf("Case #%d: ", ncase);

		//printf("S=%s, K=%d => ", S, K); //
		int r=solve();
		if (r>=0)
			printf("%d\n", r);
		else
			printf("IMPOSSIBLE\n");
	}

	return 0;
}