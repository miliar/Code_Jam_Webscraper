#include<cstdio>
#include<set>
#include<map>
#include<algorithm>
#include<vector>
#include<stack>
#include<queue>
#include<cstring>
#include<cmath>

using namespace std;

int g[105];
int rem[5];

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int T, N, P;
	scanf("%d", &T);
	int ans;
	for(int cases=1;cases<=T;cases++){
		scanf("%d %d", &N, &P);
		for(int i=0;i<N;i++) scanf("%d", &g[i]);
		memset(rem, 0, sizeof(rem));
		for(int i=0;i<N;i++){
			int tmp=g[i]%P;
			rem[tmp]++;
		}
		ans=rem[0]+1;
		if(P==2){
			ans+=(rem[1]/2);
			if(rem[1]%2==0) ans--;
		}
		else if(P==3){
			if(rem[1]<rem[2]){
				ans+=rem[1];
				rem[2]-=rem[1];
				ans+=(rem[2]/3);
				if(rem[2]%3==0) ans--;
			}
			else{
				ans+=rem[2];
				rem[1]-=rem[2];
				ans+=(rem[1]/3);
				if(rem[1]%3==0) ans--;
			}
		}
		else if(P==4){
			ans+=(rem[2]/2);
			rem[2]%=2;
			if(rem[1]<rem[3]){
				ans+=rem[1];
				rem[3]-=rem[1];
				rem[1]-=rem[1];
			}
			else{
				ans+=rem[3];
				rem[1]-=rem[3];
				rem[3]-=rem[3];
			}
			//only remain 1 or 3, and 2 less or equel than 1
			if(rem[2]>0&&rem[1]>=2){
				ans++;
				rem[2]--;
				rem[1]-=2;
			}
			if(rem[2]>0&&rem[3]>=2){
				ans++;
				rem[2]--;
				rem[3]-=2;
			}
			if(rem[1]>=4){
				ans+=(rem[1]/4);
				rem[1]%=4;
			}
			if(rem[3]>=4){
				ans+=(rem[3]/4);
				rem[3]%=4;
			}
			if(rem[2]==0&&rem[1]==0&&rem[3]==0) ans--;
		}
		printf("Case #%d: %d\n", cases, ans);
	}
	return 0;
}
