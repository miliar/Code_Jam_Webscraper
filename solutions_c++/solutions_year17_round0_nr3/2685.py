#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
using namespace std;

#define pb push_back
#define ri(x) scanf("%d",&x)
#define rii(x,y) ri(x),ri(y)
#define rl(x) scanf("%lld",&x)
#define rll(x,y) rl(x),rl(y)
#define ms(obj,val) memset(obj,val,sizeof(obj))
#define ms2(obj,val,sz) memset(obj,val,sizeof(obj[0])*sz)
#define FOR(i,f,t) for(int i=f;i<(int)t;i++)
#define FORR(i,f,t) for(int i=f;i>(int)t;i--)

typedef long long ll;
typedef vector<int> vi;

const int MAXN=0;

int T;
ll N,K,k,prevN;
ll cntMin,cntMax,newCntMin,newCntMax;

int main() {
	ri(T); FOR(t,1,T+1) {
		rll(N,K);
		k=1;
		cntMin=1;
		cntMax=0;
		while(k<=K) {
			K-=k;
			k*=2;
			if((N-1)%2==0) {
				newCntMin=cntMin*2+cntMax;
				newCntMax=cntMax;
			} else {
				newCntMin=cntMin;
				newCntMax=cntMin+cntMax*2;
			}
			cntMin=newCntMin;
			cntMax=newCntMax;
			prevN=N;
			N=(N-1)/2;
		}
		if(K==0) {
			if((prevN-1)%2==0) printf("Case #%d: %lld %lld\n",t,N,N);
			else printf("Case #%d: %lld %lld\n",t,N+1,N);
		}
		else if(K<=cntMax) printf("Case #%d: %lld %lld\n",t,(N+1)/2,N/2);
		else printf("Case #%d: %lld %lld\n",t,N/2,(N-1)/2);
	}
}