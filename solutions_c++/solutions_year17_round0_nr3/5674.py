#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int, int> ii;

#define fastio ios_base::sync_with_stdio(false);
#define fi first
#define se second

int T, n, k, x, mx, mn;

int main(){
	scanf("%d", &T);
	priority_queue<int> pq;
	
	for(int t = 1; t <= T; ++t){
		scanf("%d%d", &n, &k);
		
		printf("Case #%d: ", t);
		
		if(n == k) 
			printf("0 0\n");
		else{			
			while(!pq.empty()) pq.pop();
			pq.push(n);
			mx = 0, mn = INT_MAX;
		
			while(k--){
				x = pq.top();
				pq.pop();
				
				if(k == 0){
					if(x % 2 == 0 && x != 0){
						mn = min(mn, x/2 - 1);
						mx = max(mx, x/2);
					}		
					else{
						mn = min(mn, x/2);
						mx = max(mx, x/2);
					}	
				}
				
				if(x % 2 == 0){
					pq.push(x/2);
					pq.push(x/2 - 1);
				}
				else{
					pq.push(x/2);
					pq.push(x/2);
				}
			}
			
			printf("%d %d\n", mx, mn);
		}
	}
}
