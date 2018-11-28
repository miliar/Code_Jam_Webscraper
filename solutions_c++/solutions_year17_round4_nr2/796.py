#include<string>
#include<iostream>
#include<cstdio>
#include<vector>
#include<algorithm>
#include<functional>
using namespace std;
typedef long long int llint;

#define pub push_back
#define mp make_pair
#define fir first
#define sec second
#define res resize
#define mt make_tuple
const int big=((int)1<<30);
pair<int,int> solve(void){
	int ans,N,C,M,i,j,q,w,emp,pro;
	bool can;
	int bgen,bmax=1005,bmin=0;
	vector<int> ticket;
	vector<int> hito;
	scanf("%d %d %d",&N,&C,&M);
	hito.resize(C+1);
	ticket.resize(N+1);
	for(i=0;i<M;i++){
		scanf("%d %d",&q,&w);
		ticket[q]++;
		hito[w]++;
	}
	for(i=1;i<=C;i++){
		bmin=max(hito[i]-1,bmin);
	}
	while(bmax-bmin!=1){
		bgen=(bmax+bmin)/2;
		emp=0;pro=0;
		can=true;
		for(i=1;i<=N;i++){
			emp+=bgen;
			emp-=ticket[i];
			if(emp<0){ can=false;break; }
			if(ticket[i]>bgen){ pro+=ticket[i]-bgen; }
		}
		if(can){bmax=bgen;}
		else{ bmin=bgen; }
	}
	ans=bmax;
	
	return mp(ans,pro);
}
int main(void){
	int T;
	pair<int,int> p;
	FILE *fin;
	fin=fopen("R2GCJBans.txt","w");
	scanf("%d",&T);
	for(int i=1;i<=T;i++){
		p=solve();
		fprintf(fin,"Case #%d: %d %d\n",i,p.first,p.second);
	}
	return 0;
}