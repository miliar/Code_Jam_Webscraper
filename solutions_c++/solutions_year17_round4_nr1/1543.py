#include <bits/stdc++.h>

using namespace std;

typedef unsigned long long llu;

int solve(){
	int N,P;
	cin>>N>>P;
	map<int,int> G;
	int g;
	for(int i=0;i<N;i++){
		cin>>g;
		g = g%P;
		if(G.find(g) == G.end()){
			G[g] = 1;
		}else{
			G[g]++;
		}
	}
	if(P == 2){
		return N- (G[1]/2 + (G[1]%2==0?0:G[1]%2-1));
	}else if(P == 3){
		if(G[1] >= G[2]){
			return N-( G[2] + ((G[1]-G[2])/3)*2 + ((G[1]-G[2])%3==0?0:(G[1]-G[2])%3-1));
		}else if(G[2] > G[1]){
			return N-(G[1] + ((G[2]-G[1])/3)*2 + ((G[2]-G[1])%3==0?0:(G[2]-G[1])%3-1));
		}
	}else if(P == 4){
		int res = 0;
		if(G[1] >= G[3]){
			res += G[3];
			G[1] = G[1]-G[3];
			G[3] = 0;
		}else{
			res += G[1];
			G[3] = G[3]-G[1];
			G[1] = 0;
		}
		res += G[2]/2;
		G[2] = G[2]%2;
		G[1] = max(G[1],G[3]);

		res += (G[1]/4)*3;
		G[1] = G[1]%4;

		if(G[2] != 0 && G[1]>=2){
			res += 2;
			G[2] = 0;
			G[1]-=2;
		}
		res += ((G[1]+G[2])==0?0:(G[1]+G[2])-1);
		return N-res;
	}
}

int main(){
	int T;
	scanf("%d\n",&T);
	for(int i=1;i<=T;i++){
		printf("Case #%d: %d\n",i,solve());
	}
}