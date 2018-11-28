



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
int solve(void){
	int N,M,i,j,P,ans=0,q,a,b,c;
	int group[4]={0};
	scanf("%d %d",&N,&P);
	for(i=0;i<N;i++){
		scanf("%d",&q);
		group[q%P]++;
	}
	if(P==2){
		ans+=group[0];
		ans+=(group[1]+1)/2;
	}
	if(P==3){
		ans+=group[0];
		a=min(group[1],group[2]);
		ans+=a;
		group[1]-=a;
		group[2]-=a;
		ans+=(group[1]+group[2]+2)/3;
	}
	if(P==4){
		ans+=group[0];
		a=min(group[1],group[3]);
		ans+=a;
		b=max(group[1],group[3])-a;
		ans+=group[2]/2;
		b+=(group[2]%2)*2;
		ans+=(b+3)/4;
	}
	return ans;
}
int main(void){
	int T;
	FILE *fin;
	fin=fopen("R2GCJAans.txt","w");
	scanf("%d",&T);
	for(int i=1;i<=T;i++){
		fprintf(fin,"Case #%d: %d\n",i,solve());
	}
	return 0;
}