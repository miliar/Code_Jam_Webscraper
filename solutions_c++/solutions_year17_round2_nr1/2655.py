#include <iostream>
#include <cstdio>
#include <string>
#include <cmath>
#include <cstring>
using namespace std; 
int K[1005],S[1005];
int main(){
	int T,D,N;
	double t;
	freopen("A-large.in.txt","r",stdin);
	freopen("A-large.out.txt","w",stdout);
	scanf("%d",&T);
	for (int cases=1;cases<=T;cases++){
		scanf("%d%d",&D,&N);
		t=0;
		for (int i=0;i<N;i++)
			scanf("%d%d",&K[i],&S[i]);
		for (int i=0;i<N;i++){
			double tmp=(D-K[i])*1.0/S[i]; 
			if (t<tmp) t=tmp;
		} 
		printf("Case #%d: %.6lf\n",cases,D/t); 
	}
	return 0;
}