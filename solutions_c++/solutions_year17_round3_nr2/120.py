#include <iostream>
#include <algorithm>
using namespace std;

int T;
int dp[721][721][2];
int main(){
	cin >> T;
	for (int t=1;t<=T;t++){
		for (int i=0;i<=720;i++)
			for (int j=0;j<=720;j++) dp[i][j][0] = dp[i][j][1]= 1440;
		bool C[1440], J[1440];
		for (int i=0;i<1440;i++) C[i] = J[i] = true;
		int Ac, Aj;
		cin >>Ac >>Aj;
		for (int i=0;i<Ac;i++){
			int l,r; cin >>l >> r;
			for (int j=l;j<r;j++) C[j] = false;
		}
		for (int i=0;i<Aj;i++){
			int l,r; cin >>l >> r;
			for (int j=l;j<r;j++) J[j] = false;
		}
		//assume C goes first
		int ans = 1440;
		if (C[0]){
			dp[1][0][0] = 0;
			for (int i=1;i<=720;i++){
				for (int j=0;j<=720;j++){
					if (i==1&&j==0)continue;
					if (C[i+j-1]){
						dp[i][j][0] = min(dp[i-1][j][0], dp[i-1][j][1] + 1);
					}
					if (J[i+j-1] && j>0){
						dp[i][j][1] = min(dp[i][j-1][0]+1, dp[i][j-1][1]);
					}
				}
			}
			
			ans = min(min(dp[720][720][0], dp[720][720][1]+1), ans);
		}
		if (J[0]){
		//assume J goes first
		for (int i=0;i<=720;i++)
			for (int j=0;j<=720;j++) dp[i][j][0] = dp[i][j][1]= 1440;
		
			dp[0][1][1] = 0;
			for (int i=0;i<=720;i++){
				for (int j=1;j<=720;j++){
					if (i==0&&j==1)continue;
					if (C[i+j-1] && i > 0){
						dp[i][j][0] = min(dp[i-1][j][0], dp[i-1][j][1] + 1);
					}
					if (J[i+j-1]){
						dp[i][j][1] = min(dp[i][j-1][0]+1, dp[i][j-1][1]);
					}
				}
			}
			ans = min(min(dp[720][720][0]+1, dp[720][720][1]), ans);
		}
		cout << "Case #" << t << ": " << ans << endl;
	}
}
