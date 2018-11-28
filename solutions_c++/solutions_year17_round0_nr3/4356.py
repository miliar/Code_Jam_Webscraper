#include <stdio.h>
#include <queue>
#include <algorithm>
using namespace std;


typedef long long LL;
int main(int argc, char const *argv[])
{
	int T;
	scanf("%d",&T);
	for (int t = 0; t < T; ++t)
	{
		printf("Case #%d: ", t+1);

		LL N,K;
		priority_queue<LL> PQ;
		scanf("%lld %lld",&N,&K);
		LL L=(N-1)/2;
		LL R=N/2;
		if(L)
		PQ.push(L);
		if(R)
		PQ.push(R);
		K--;
		//printf("L= %d    R = %d\n", L, R);
		while(!PQ.empty() && K)
		{
			LL top = PQ.top();
			PQ.pop();
			L = (top-1)/2;
			R = top/2;
			//printf(">>>L= %lld    R = %lld\n", L, R);
			if(!L&&!R)break;
			if(L)
			PQ.push(L);
			if(R)
			PQ.push(R);
			--K;
		}
		printf("%lld %lld\n",max(L,R),min(L,R) );
	}
	return 0;
}