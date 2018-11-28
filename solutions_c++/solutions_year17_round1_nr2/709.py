#include <iostream>
#include <cstdio>
#include <cstring>
#include <vector>
#include <algorithm>
using namespace std;

const int MAXN=59;

int N,M,ans,id[MAXN],C[MAXN],cnt[MAXN];
vector<int> Q[MAXN];
vector<int> L[MAXN],R[MAXN];

void Init(){
	cin>>N>>M;
	for(int i=0;i<N;i++) cin>>C[i];
	for(int i=0;i<N;i++){
		Q[i].resize(M);
		L[i].resize(M);
		R[i].resize(M);
		for(int j=0;j<M;j++)
			cin>>Q[i][j];
		sort(Q[i].begin(),Q[i].end());
		for(int j=0;j<M;j++){
			L[i][j]=(int)((double)Q[i][j]/1.1/C[i]-1e-8)+1;
			R[i][j]=(int)((double)Q[i][j]/0.9/C[i]+1e-8);
		}
		cnt[i]=0;
		for(int j=0;j<M;j++){
			if(L[i][j]<=R[i][j]){
				L[i][cnt[i]]=L[i][j];
				R[i][cnt[i]]=R[i][j];
				cnt[i]++;
			}
		}
		//for(int j=0;j<cnt[i];j++) cerr<<"["<<L[i][j]<<","<<R[i][j]<<"] "; cerr<<"\n";
	}
}

void Solve(){
	for(int i=0;i<N;i++) id[i]=0;
	ans=0;
	for(;;){
		bool fin=false;
		for(int i=0;i<N;i++) if(id[i]==cnt[i]) fin=true;
		if(fin) break;
		int minx=L[0][id[0]],maxx=R[0][id[0]];
		for(int i=0;i<N;i++){
			minx=max(minx,L[i][id[i]]);
			maxx=min(maxx,R[i][id[i]]);
		}
		if(minx<=maxx){
			ans++;
			for(int i=0;i<N;i++) id[i]++;
		}else{
			int imin=0;
			for(int i=0;i<N;i++)
				if(L[i][id[i]]<L[imin][id[imin]])
					imin=i;
			id[imin]++;
		}
	}
}

int main(){
	int Test; cin>>Test;
	for(int i=1;i<=Test;i++){
		Init();
		Solve();
		cout<<"Case #"<<i<<": "<<ans<<"\n";
	}
}