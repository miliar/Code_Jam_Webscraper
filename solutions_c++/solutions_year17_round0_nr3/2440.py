//Franciszek Budrowski

#include<bits/stdc++.h>
#define FOR(i,s,e) for(int i=(s);i<=(e);i++)
#define FORD(i,s,e) for(int i=(s);i>=(e);i--)
#define ALL(k) (k).begin(),(k).end()
#define e1 first
#define e2 second
#define mp make_pair
#define pb push_back
#define eb emplace_back

using namespace std;
typedef long long LL;
typedef long double LD;
typedef pair<int,int> PII;
typedef pair<LL,LL> PLL;
typedef vector<int> VI;

const bool print=false;


main(){
	int test;scanf("%d",&test);
	FOR(casenr,1,test){
		LL n,k;scanf("%lld%lld",&n,&k);
		printf("Case #%d: ",casenr);
		LL zl=0;
		map<LL,LL> M;
		M[n]=1;
		priority_queue<LL> PQ;
		PQ.push(n);
		//puts("");
		while(!PQ.empty()){
			//printf("WEJ %lld\n",PQ.top());
			LL x=PQ.top();PQ.pop();
			LL z1=(x-1LL)/2LL+(x-1LL)%2LL;
			LL z2=(x-1LL)/2LL;
			LL zl0=M[x];
			zl+=zl0;
			//printf("%lld %lld %lld-> %lld %lld\n",x,zl0,zl,z1,z2);
			if(zl>=k){
				printf("%lld %lld\n",z1,z2);
				break;
			}
			if(M.find(z1)==M.end())
				M[z1]=zl0,PQ.push(z1);
			else M[z1]+=zl0;
			if(M.find(z2)==M.end())
				M[z2]=zl0,PQ.push(z2);
			else M[z2]+=zl0;
		}
	}
}
		

