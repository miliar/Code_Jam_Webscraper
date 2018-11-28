/* In The Name Of God */
#include <bits/stdc++.h>

# define xx first
# define yy second
# define pb push_back
# define pp pop_back
# define eps 1e-9

using namespace std;
typedef long long ll;
typedef pair<int,int> pii;
typedef vector<int> vint;
int dp[1010][1010][2][2];
int ac,aj;
bool canC[60*25],canJ[60*25];
int main(){
	ios_base::sync_with_stdio (0);
	freopen("b.in","r",stdin);
	freopen("out.txt","w",stdout);
	int T;cin>>T;
	for(int tc=1; tc<=T ; tc++){
		memset(canC,true,sizeof canC);
		memset(canJ,true,sizeof canJ);
		memset(dp,63,sizeof dp);
		cin>>ac>>aj;
		while(ac--){
			int L,R;cin>>L>>R;
			while(L<R){
				canC[L] = false;
				L++;
			}
		}
		while(aj--){
			int L,R;cin>>L>>R;
			while(L<R){
				canJ[L] = false;
				L++;
			}
		}
		if(canC[1])
			dp[1][0][0][0] = 0;
		if(canJ[1])
			dp[0][1][1][1] = 0;
		for(int i=0 ; i<=720 ; i++)
			for(int j=0 ; j<=720 ; j++){
				if( canC[i+j] ){
					if(i>0){
						dp[i][j][0][0] = min(dp[i][j][0][0] , dp[i-1][j][0][0]);
						dp[i][j][0][1] = min(dp[i][j][0][1] , dp[i-1][j][0][1]);
					}
					if(j>0){
						dp[i][j][0][0] = min(dp[i][j][0][0] , dp[i][j-1][1][0] + 1);
						dp[i][j][0][1] = min(dp[i][j][0][1] , dp[i][j-1][1][1] + 1);
					}
				}
				if( canJ[i+j] ){
					if(i>0){
						dp[i][j][1][0] = min(dp[i][j][1][0] , dp[i-1][j][0][0] + 1);
						dp[i][j][1][1] = min(dp[i][j][1][1] , dp[i-1][j][0][1] + 1);
					}
					if(j>0){
						dp[i][j][1][0] = min(dp[i][j][1][0] , dp[i][j-1][1][0] );
						dp[i][j][1][1] = min(dp[i][j][1][1] , dp[i][j-1][1][1] );
					}
				}
			}
		cout<<"Case #"<<tc<<": ";
		cout<<min( min(dp[720][720][0][0],dp[720][720][1][1]) , min(dp[720][720][0][1],dp[720][720][1][0])+1 )<<endl;
	}
	return 0;
}

