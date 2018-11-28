#include<deque>
#include<queue>
#include<map>
#include<string>
#include<iostream>
#include<set>
#include<cmath>
#include<cstdio>
#include<vector>
#include<algorithm>
#include<functional>
//#define scanf scanf_s
#define fir first
#define sec second
#define mp make_pair
#define mt make_tuple
#define pub push_back
using namespace std;
typedef long long int llint;
const llint one = 1;
const llint big = (one<<30);
const llint mod=1000000007;


int main(void){
	int T;
	auto fi=fopen("GCJansB.txt","w");
	scanf("%d",&T);
	for(int ias=1;ias<=T;ias++){ fprintf(fi,"Case #%d: ",ias);
		llint N,P,i,j,a,ans=0,kosu=0,ok;
		vector<llint> R;
		vector<deque<llint>> Q;
		scanf("%lld %lld",&N,&P);
		Q.resize(N);
		for(i=0;i<N;i++){
			scanf("%lld",&a);
			R.pub(a);
		}
		for(i=0;i<N;i++){
			for(j=0;j<P;j++){
				scanf("%lld",&a);
				Q[i].pub(a);
			}
			Q[i].push_back(10000000000000);
			sort(Q[i].begin(),Q[i].end());
		}
		for(kosu=1;kosu<1000000;kosu++){
			ok=1;
			for(i=0;i<N;i++){
				if(Q[i].front()>1234567){ok=0;break;}
				if(kosu*R[i]*9>Q[i].front()*10){ Q[i].pop_front();i--;continue; }
				if(kosu*R[i]*11<Q[i].front()*10){ok=0;break;}
			}
			if(ok==1){
				ans++;
				for(i=0;i<N;i++){Q[i].pop_front();}
				kosu--;
			}
		}
		fprintf(fi,"%lld\n",ans);
	}
	return 0;
}
