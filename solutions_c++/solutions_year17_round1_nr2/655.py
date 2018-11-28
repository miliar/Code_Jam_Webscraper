#include<bits/stdc++.h>
using namespace std;
long long ingr[51][51];
int cost[51];
int n,p;
int pp[51];
int main(){
	int t;
	scanf("%d",&t);
	for(int turn = 1; turn <= t; turn++){
		int ans = 0;
		scanf("%d%d",&n,&p);
		for(int i=0;i<n;i++){
			scanf("%d",&cost[i]);
		}
		for(int i=0;i<n;i++){
			for(int j=0;j<p;j++){
				scanf("%lld",&ingr[i][j]);
				ingr[i][j] *= 10;
			}
			pp[i] = 0;
			sort(ingr[i], ingr[i]+p);
		}
		while(1){
			long long mn = -1;
			long long mx = 2100000000;
			for(int i=0;i<n;i++){
				mn = max(mn, (ingr[i][pp[i]] + (11 * cost[i]) - 1) / (11 * cost[i]));
				mx = min(mx, (ingr[i][pp[i]] / (9 * cost[i])));
			}
			if(mn <= mx){
				ans++;
				int valid = true;
				for(int i=0;i<n;i++){
					pp[i]++;
					if(pp[i] == p) valid = false;
				}
				if(!valid) break;
			}else{
				int valid = true;
				for(int i=0;i<n;i++){
					if((ingr[i][pp[i]] / (9 * cost[i])) < mn){
						pp[i]++;
						if(pp[i] == p) valid = false;
					}
				}
				if(!valid) break;
			}
		}
		printf("Case #%d: %d\n", turn, ans);
	}
}
