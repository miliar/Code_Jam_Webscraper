#include <bits/stdc++.h>
using namespace std;

#define FOR(i,l,r) for(int i = (int) (l);i < (int) (r);i++)
template<typename T> bool chmax(T& a,const T& b){ return a < b ? (a = b,true) : false; }
template<typename T> bool chmin(T& a,const T& b){ return b < a ? (a = b,true) : false; }
typedef long long ll;

int TC,N,M,C;

int main()
{
	scanf("%d",&TC);
	FOR(tc,1,TC + 1){
		scanf("%d%d%d",&N,&C,&M);
		vector<int> P(M),B(M);
		FOR(i,0,M){
			scanf("%d%d",&P [i],&B [i]);
		}
		if(C != 2) continue;
		map<int,int> mp1,mp2;
		FOR(i,0,M){
			if(B [i] == 1){
				mp1 [P [i]]++;
			}
			else{
				mp2 [P [i]]++;
			}
		}
		int p = max(int(count(B.begin(),B.end(),1)),int(count(B.begin(),B.end(),2)));
		for(int i = p;i <= M;i++){
			bool ok = true;
			int q = 0;
			for(int j = 1;j <= N;j++){
				int x = mp1 [j],y = mp2 [j];
				while(x + y > i && (x > 0 || y > 0) && j > 1){
					if(x > 0) x--;
					else y--;
					q++;
				}
				if(x + y > i){
					ok = false;
					break;
				}
			}
			if(ok){
				printf("Case #%d: %d %d\n",tc,i,q);
				break;
			}
		}
	}

	return 0;
}
