#include <bits/stdc++.h>

using namespace std;
#define int long long
int ac[1719];
int dp1[1719][1219][2],dp2[1719][1219][2];
#undef int
int main(){
	#define int long long
	int tc,tci=1;cin>>tc;
	while(tc-->0){
		int ans=0x3f3f3f3f3f3fLL;
		memset(ac,0,sizeof(ac));
		int an,jn;cin>>an>>jn;
		for(int i=0;i<an;i++){
			int l,r;cin>>l>>r;
			for(int j=l;j<r;j++){
				ac[j]=1;
			}
		}
		for(int i=0;i<jn;i++){
			int l,r;cin>>l>>r;
			for(int j=l;j<r;j++){
				ac[j]=2;
			}
		}
		memset(dp1,0x3f,sizeof(dp1));//last day ends at 1
		memset(dp2,0x3f,sizeof(dp2));//last day ends at 2
		if(ac[0]==0){
			dp1[0][719][0]=0;
			dp1[0][720][1]=1;
		}else if(ac[0]==1)dp1[0][720][1]=1;
		else dp1[0][719][0]=0;
		for(int i=1;i<=1439;i++){
			for(int j=0;j<=720;j++){
				if(j-1>=0&&ac[i]!=1)dp1[i][j-1][0]=min(dp1[i][j-1][0],dp1[i-1][j][1]+1);
				if(j-1>=0&&ac[i]!=1)dp1[i][j-1][0]=min(dp1[i][j-1][0],dp1[i-1][j][0]+0);
				if(ac[i]!=2)dp1[i][j][1]=min(dp1[i][j][1],dp1[i-1][j][1]+0);
				if(ac[i]!=2)dp1[i][j][1]=min(dp1[i][j][1],dp1[i-1][j][0]+1);
			}
		}
		ans=min(ans,dp1[1439][0][0]);
		if(ac[0]==0){
			dp2[0][719][0]=1;
			dp2[0][720][1]=0;
		}else if(ac[0]==1)dp2[0][720][1]=0;
		else dp2[0][719][0]=1;
		for(int i=1;i<=1439;i++){
			for(int j=0;j<=720;j++){
				if(j-1>=0&&ac[i]!=1)dp2[i][j-1][0]=min(dp2[i][j-1][0],dp2[i-1][j][1]+1);
				if(j-1>=0&&ac[i]!=1)dp2[i][j-1][0]=min(dp2[i][j-1][0],dp2[i-1][j][0]+0);
				if(ac[i]!=2)dp2[i][j][1]=min(dp2[i][j][1],dp2[i-1][j][1]+0);
				if(ac[i]!=2)dp2[i][j][1]=min(dp2[i][j][1],dp2[i-1][j][0]+1);
			}
		}
		ans=min(ans,dp2[1439][0][1]);
		cout<<"Case #"<<tci++<<": "<<ans<<endl;
	}
	return 0;
}
