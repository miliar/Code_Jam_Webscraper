#include <cstdio>
#include <vector>
#include <set>
#include <unordered_map>
#include <map>
#include <algorithm>

using namespace std;

int dp[109][109][109];

void solve(){
	int n, p;
	scanf("%d %d", &n, &p);
	int cnt[4]={0,0,0,0};
	for(int i=0; i<n; i++){
		int x;
		scanf("%d", &x);
		x%=p;
		cnt[x]++;
	}
	int s=cnt[0];
	/*
	if(p==2){
		s+=(cnt[1]+1)/2;
		printf("%d\n", s);
	}
	if(p==3){
		s+=min(cnt[1], cnt[2]);
		int rem=max(cnt[1], cnt[2])-min(cnt[1], cnt[2]);
		s+=(rem+2)/3;
		printf("%d\n", s);
	}
	*/
	//if(p==4){
	
	for(int i=0; i<=cnt[1]; i++){
		for(int j=0; j<=cnt[2]; j++){
			for(int k=0; k<=cnt[3]; k++){
				dp[i][j][k]=0;
			}
		}
	}

	for(int i=0; i<=cnt[1]; i++){
		for(int j=0; j<=cnt[2]; j++){
			for(int k=0; k<=cnt[3]; k++){
				int leftovers=(p-(i+2*j+3*k)%p)%p;
				//printf("Lo = %d\n", leftovers);
				int cm=dp[i][j][k];
				if(leftovers==0){
					cm++;
				}
				if(i!=cnt[1]){
					dp[i+1][j][k]=max(dp[i+1][j][k], cm);
				}
				if(j!=cnt[2]){
					dp[i][j+1][k]=max(dp[i][j+1][k], cm);
				}
				if(k!=cnt[3]){
					dp[i][j][k+1]=max(dp[i][j][k+1], cm);
				}
			}
		}
	}
	for(int i=0; i<=cnt[1]; i++){
		for(int j=0; j<=cnt[2]; j++){
			for(int k=0; k<=cnt[3]; k++){
				//printf("%d,%d,%d: %d\n", i, j, k, dp[i][j][k]);
			}
		}
	}
	printf("%d\n", s+dp[cnt[1]][cnt[2]][cnt[3]]);

	//}
}

int main(){
	int t;
	scanf("%d", &t);
	for(int tc=0; tc<t; tc++){
		fprintf(stderr, "%d/%d\n", tc, t);
		printf("Case #%d: ", tc+1);
		solve();
	}
}
