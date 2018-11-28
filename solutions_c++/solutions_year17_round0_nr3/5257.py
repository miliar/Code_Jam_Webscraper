
#include<bits/stdc++.h>
#define all(x) x.begin(), x.end()
#define pb(x) push_back(x)
#define cout2(x, y) cout << x << " " << y << endl
#define N 1003

using namespace std;


int main(){

	int tc = 0, caso = 1;
	scanf("%d", &tc);
	
	while(tc--){
		
		long long n, k;
		scanf("%lld%lld", &n, &k);
		
		priority_queue<int>Q;
		Q.push(n);
		
		int best, mid;
		for(int i = 0; i < k - 1; i++){
			
			best = Q.top();
			Q.pop();
			
			best--;
			mid = best/2;
			
			if(mid > 0)Q.push(mid);
			if(best - mid > 0)Q.push(best - mid);
		}
		
		best = Q.top();
		best--;
		//cout2(best, "best");
		printf("Case #%d: %d %d\n", caso++, best - best/2, best/2);
	}
}

