#include <iostream>
#include <cstdio>
#include <string>
#include <queue>
#include <cstring>
using namespace std;
struct node
{
	int L,R;
	bool operator < (node a) const  {   
         if (R-L != a.R-a.L) return R-L < a.R-a.L;
         return L < a.L;
    }     
}; 
priority_queue<node> Q;
int main(){
	int T;
	freopen("C-small-2-attempt0.in.txt","r",stdin);
	freopen("C-small-2-attempt0.out.txt","w",stdout);
	scanf("%d",&T);
	for (int cases=1;cases<=T;cases++){ 
		int n,k,A,B;
		scanf("%d%d",&n,&k); 
		while (Q.size()) Q.pop();
		node n0;
		n0.L=0,n0.R=n+1;
		Q.push(n0);
		while (k--){
			node n1 = Q.top();
			Q.pop();
			int x=(n1.R+n1.L)/2;
			//printf("%d\n",x);
			int l=x-n1.L-1, r=n1.R-x-1;
			A=max(l,r);
			B=min(l,r);
			if (l!=0){
				node n2;
				n2.L=n1.L;
				n2.R=x;
				Q.push(n2);
			}
			if (r!=0){
				node n2;
				n2.L=x;
				n2.R=n1.R;
				Q.push(n2);
			}
		}
		printf("Case #%d: %d %d\n",cases,A,B); 
	}
	return 0;
}