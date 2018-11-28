#include <stdio.h>
#include <map>
using namespace std;

int main()
{
	freopen ("input.txt","r",stdin);
	freopen ("output.txt","w",stdout);

	int Test; scanf ("%d",&Test); for (int Case=1;Case<=Test;Case++){
		printf ("Case #%d: ",Case);

		long long N,K;
		scanf ("%lld %lld",&N,&K);

		map<long long, long long> chk;
		chk[N] = 1;
		while (!chk.empty()){
			auto I = chk.end().operator--();
			long long n = I->first, c = I->second;
			chk.erase(I);
			long long l = (n - 1) / 2, r = n - 1 - l;
			if (K <= c){
				printf ("%lld %lld\n",r,l);
				break;
			}
			K -= c;
			if (l) chk[l] += c;
			if (r) chk[r] += c;
		}
	}

	return 0;
}