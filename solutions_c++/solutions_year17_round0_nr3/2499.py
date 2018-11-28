#include<cstdio>
#include<iostream>

using namespace std;

typedef long long lld;

lld path[1000];
int pathLen;

int main()
{
	int T;
	cin >> T;
	lld N,K;
	for(int tc=1;tc<=T;tc++)
	{
		cin>>N>>K;
		
		lld L,R;
		lld nL,nR,nX;

		pathLen = 0;
		lld x = K;
		while(x>1)
		{
			path[pathLen++] = x;
			x/=2;
		}
		//for(int i=0;i<pathLen;i++) printf("%d ", path[i]);
		/*if(N%2==1)
		{
			L=N/2;
			nL=2;
			R=L-1;
			nR=0;
			nX=0;
		}
		else
		{
			L=N/2;
			nL=1;
			R=L-1;
			nR=1;
			nX=1;
		}*/
		L=N;
		nL=1;
		R=L-1;
		nR=0;
		x=1;
		while(x<=K)
		{
			lld tempL = L;
			lld tempnL = nL;
			lld tempR = R;
			lld tempnR = nR;
			lld tempnX = nX;
			if(tempL%2==1)
			{
				L=tempL/2;
				nL=tempnL*2;
				R=L-1;
				nR=0;
				
				nL+=tempnR;
				nR+=tempnR;
				nX=tempnR;
			}
			else
			{
				L=tempL/2;
				nL=tempnL;
				R=L-1;
				nR=nL;
				
				nR+=tempnR*2;
				nX=tempnL;
			}
			x*=2;
		}
		x/=2;
		lld tempnL=(nL-nX)/2;
		lld tempnR=(nR-nX)/2;
		//printf("%lld %lld\n",tempnL,tempnR);
		lld dif=K-x;
		if(dif<tempnL) printf("Case #%d: %lld %lld\n", tc, L, L);
		else if(dif<tempnL+nX) printf("Case #%d: %lld %lld\n", tc, L, R);
		else printf("Case #%d: %lld %lld\n", tc, R, R);
	}

	return 0;
}
