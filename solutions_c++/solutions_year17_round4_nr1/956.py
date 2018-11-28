#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;

int N, P;
int A[109],F[109][109][109][4];

int DP(int g1,int g2,int g3,int r){
	if(g1+g2+g3==0) return 0;
	if(F[g1][g2][g3][r]>=0) return F[g1][g2][g3][r];
	
	if(r==0) F[g1][g2][g3][r]=1;
	else F[g1][g2][g3][r]=0;
	
	int tmp=0;
	if(g1>0) tmp=max(DP(g1-1,g2,g3,(r+1)%4),tmp);
	if(g2>0) tmp=max(DP(g1,g2-1,g3,(r+2)%4),tmp);
	if(g3>0) tmp=max(DP(g1,g2,g3-1,(r+3)%4),tmp);
	F[g1][g2][g3][r] += tmp;
	
	return F[g1][g2][g3][r];
}

void Solve(){
	memset(A,0,sizeof(A));
	cin>>N>>P;
	for(int i=0;i<N;i++){
		int x; cin>> x;
		A[x%P]++;
	}
	if(P==2) cout<<A[0]+(A[1]+1)/2<<"\n";
	else if(P==3){
		int t=min(A[1],A[2]); A[1]-=t; A[2]-=t;
		cout<<A[0]+t+(A[1]+A[2]+2)/3<<"\n";
	}else cout<<A[0]+DP(A[1],A[2],A[3],0)<<"\n";
}


int main(){
	memset(F,0xff,sizeof(F));
	int Test; cin>>Test;
	for(int i=1;i<=Test;i++){
		cout<<"Case #"<<i<<": ";
		Solve();
	}
}