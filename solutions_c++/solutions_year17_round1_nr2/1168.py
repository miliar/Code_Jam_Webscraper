#include <cstdio>
#include <cstring>
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

bool ok;
int N, P, ans;
int R[55], Q[55][55], idx[55];
double low[55], high[55];
int main(){
    freopen("B-small-attempt0.in","r",stdin);
    freopen("output.txt","w",stdout);
    int T;
	scanf("%d",&T);
    for(int cases=1; cases<=T; cases++){
    	printf("Case #%d: ",cases);
    	ans = 0;
    	scanf("%d %d",&N,&P);
 
    	
    	for(int i=1; i<=N; i++){
    		scanf("%d",&R[i]);
    		low[i] = R[i]*0.9;
    		high[i] = R[i]*1.1;
		}
    	for(int i=1; i<=N; i++){
    		for(int j=1; j<=P; j++) scanf("%d",&Q[i][j]);
    		sort(Q[i]+1, Q[i]+1+P);
		}
		int cur=1;
		
		for(int i=1; i<=N; i++) idx[i] = 1;
		
		while(idx[1] <= P){
			if(Q[1][idx[1]] >= low[1]*cur && Q[1][idx[1]] <= high[1]*cur){
				ok = 1;
				for(int i=2; i<=N; i++){
					while(Q[i][idx[i]] < low[i] * cur && idx[i] <= P) idx[i]++;
					if(Q[i][idx[i]] > high[i] * cur || idx[i] > P){
						cur++;
						ok=0;
						break;
					}
					if(!ok) break;
				}
				if(!ok) continue;
				ans++;
				idx[1]++;
			}
			else if(Q[1][idx[1]] < low[1]*cur){
				while(Q[1][idx[1]] < low[1]*cur) idx[1]++;
			}
			else while(Q[1][idx[1]] > high[1] * cur) cur++;
		}
		printf("%d\n",ans);
		
	}
    return 0;
}
