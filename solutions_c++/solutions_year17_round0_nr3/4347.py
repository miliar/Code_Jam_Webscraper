#include<bits/stdc++.h>
using namespace std;
struct stall{
	int S,L;
};
bool cmp(stall a, stall b){
	return tie(a.S,a.L)>tie(b.S,b.L);
}
queue<stall> que;
stall ary[1000100];
main(){
	int T,k,i;
	freopen("C-small-2-attempt0.in","r",stdin);
	freopen("outputC2.out","w",stdout);
	scanf("%d",&T);
	for(k=1;k<=T;k++){
		int N,K;
		stall tmp, now;
		scanf("%d%d",&N,&K);
		if(N%2) tmp.S=tmp.L=N/2;
		else{
			tmp.S=N/2-1;
			tmp.L=N/2;
		}
		que.push(tmp);
		int c=0;
		while(!que.empty()){
			now=que.front();
			que.pop();
			ary[c]=now;
			c++;
			if(now.S>0){
				if(now.S%2) tmp.S=tmp.L=now.S/2;
				else{
					tmp.S=now.S/2-1;
					tmp.L=now.S/2;
				}
				que.push(tmp);
			}
			if(now.L>0){
				if(now.L%2) tmp.S=tmp.L=now.L/2;
				else{
					tmp.S=now.L/2-1;
					tmp.L=now.L/2;
				}
				que.push(tmp);
			}
		}
		sort(ary, ary+c, cmp);
		printf("Case #%d: %d %d\n",k,ary[K-1].L,ary[K-1].S);
	}
}
