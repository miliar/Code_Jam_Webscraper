#include <cstdio>
#include <cstring>
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
#define F(i,n) for(int i=1; i<=n; i++)

int N, K;
double U, P[55], tmp, ans;
int main(){
    freopen("C-small-1-attempt0.in","r",stdin);
    freopen("output.txt","w",stdout);
    int T;
	scanf("%d",&T);
    for(int cases=1; cases<=T; cases++){
    	ans = 1;
    	printf("Case #%d: ",cases);
    	scanf("%d %d %lf",&N,&K,&U);
    	F(i, N) scanf("%lf",&P[i]);
    	sort(P+1, P+1+N);
    	P[N+1] = 1;
    	int top = 1;
    	while(top <= N && U > 0){
    		tmp = top * (P[top+1]-P[top]);
    		if(U >= tmp){
    			U-=tmp;
    			F(i, top) P[i]+=P[top+1]-P[top];
			}
			else {
				F(i, top) P[i]+=U/top;
				U=0;
			}
			top++;
		}
		
		F(i, N) ans*=P[i];
		printf("%.6lf\n",ans);
		
	}
    return 0;
}
