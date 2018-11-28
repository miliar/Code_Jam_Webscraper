#include <bits/stdc++.h>

using namespace std;

struct par{
	int x1, x2, dist;
	par(){}
	par(int xx1, int xx2){
		x1=xx1;
		x2=xx2;
		dist=x2-x1;
	}
	bool operator < (par otro) const{
		return dist<otro.dist || dist==otro.dist && x1>otro.x1;
	}
};

int n, k, mini, maxi;

void solve(){
	priority_queue<par> cola;
	cola.push(par(0,n-1));
	par p;
	int left, right, l, r, x1, x2, x;
	for(int i=0; i<k; i++){
		p=cola.top();
		cola.pop();
		x1=p.x1;
		x2=p.x2;
		//printf("%d %d\n", x1, x2);
		x=(x1+x2)/2;
		l=x-x1;
		r=x2-x;
		mini=min(l, r);
		maxi=max(l, r);
		left=x+1;
		right=x-1;
		if(x1<=right){
			cola.push(par(x1, right));
		}
		if(left<=x2){
			cola.push(par(left, x2));
		}
	}

}

int main(){
	int u, v, test;
	freopen("c2.in", "r", stdin);
	freopen("c2_out.txt", "w", stdout);
	scanf("%d", &test);
	for(int tt=1; tt<=test; tt++){
		scanf("%d %d", &n, &k);
		solve();
		printf("Case #%d: %d %d\n", tt, maxi, mini);
	}
	return 0;
}
