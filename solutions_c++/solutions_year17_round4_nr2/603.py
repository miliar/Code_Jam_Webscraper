#include<stdio.h>
#include<memory.h>
using namespace std;

int N, M, C;
int ba[1010][1010], cnt;

void test(int tn){
	scanf("%d%d%d", &N, &C, &M);
	memset(ba,0,sizeof(ba)); cnt=0;
	for(int i=0; i<M; i++){
		int a, b;
		scanf("%d%d", &a, &b);
		ba[b][a]++;
	}
	int mx=0, chk=1, rmx=0;
	for(int j=1; j<=C; j++) mx += ba[j][1];
	for(int j=1; j<=C; j++){
		int sum=0;
		for(int i=1; i<=N; i++) sum += ba[j][i];
		if(mx<sum) mx=sum, chk=0;
	}
	for(int i=1; i<=N; i++){
		int sum=0;
		for(int j=1; j<=C; j++) sum += ba[j][i];
		if(rmx<sum-mx) rmx=sum-mx;
	}
	printf("Case #%d: %d %d\n", tn, mx, rmx);
}

int main(){
	freopen("B-small-attempt0.in","r",stdin),freopen("output.txt","w",stdout);
	int t, i;
	scanf("%d", &t);
	for(int i=1; i<=t; i++) test(i);
	return 0;
}
