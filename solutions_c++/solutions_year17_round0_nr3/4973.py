/*input
12
50 1
50 2
50 3
50 4
50 5
50 6
50 7
50 8
50 9
50 10
50 11
50 12
*/
#include <bits/stdc++.h>
#define endl '\n'
#define fo(i,n) for(i=0;i<n;++i)
#define forr(i,n) for(i=n-1;i>=0;--i)
using namespace std;
typedef long long int ll;
typedef pair<int,int> ii;
typedef vector<ii> vii;
typedef vector<int> vi;

int main(){
	ios_base::sync_with_stdio(0);
	cin.tie(NULL);
	cout.tie(NULL);
	
	ifstream cin("C-small-2-attempt1.in");
	ofstream cout("c_small_2_attempt1.txt");

	int t, i;
	ll level, minus, same;
	cin>>t;
	for(int te=1;te<=t;te++){
		cout<<"Case #"<<te<<": ";
		ll n, k;
		ll dp[62][4];
		cin>>n>>k;
		if(n&1){
			//odd
			dp[0][0] = n/2;
			dp[0][1] = dp[0][0];
			dp[0][2] = 1;
			dp[0][3] = 1;
			for(i=1;i<62;i++){
				if(dp[i-1][2]>1e17 || dp[i-1][3]>1e17){
					continue;
				}
				if(dp[i-1][0]&1 && dp[i-1][1]&1){
					dp[i][0] = dp[i-1][0]/2;
					dp[i][1] = dp[i-1][1]/2;
					dp[i][2] = dp[i-1][2] + dp[i-1][3];
					dp[i][3] = dp[i-1][2] + dp[i-1][3];
					continue;
				}
				dp[i][0] = dp[i-1][0]/2;
				if(dp[i][0]==0)
					dp[i][1] = 0;
				else
					dp[i][1] = dp[i][0] - 1;
				if(dp[i-1][0]==dp[i-1][1]){
					dp[i][2] = dp[i-1][2] + dp[i-1][2];
					dp[i][3] = dp[i-1][2] + dp[i-1][3];
				}
				else if(dp[i-1][1]&1){
					//dp[i-1][0] is even
					dp[i][2] = dp[i-1][2];
					dp[i][3] = dp[i-1][2] + 2*dp[i-1][3];
				}
				else{
					//dp[i-1][0] is odd
					dp[i][2] = 2*dp[i-1][2] + dp[i-1][3];
					dp[i][3] = dp[i-1][3];
				}
			}
			level = (int)log2(k);
			if(level==0)
				minus = 0;
			else	
				minus = (1ll<<(level))-1;
			// for(i=0;i<10;i++){
			// 	cout<<dp[i][0]<<" "<<dp[i][1]<<" "<<dp[i][2]<<" "<<dp[i][3]<<endl;
			// }
			if(dp[level][2] > dp[level][3]){
				same = (dp[level][2] - dp[level][3])/2;
				if((k-minus) <= same){
					cout<<dp[level][0]<<" "<<dp[level][0]<<endl;
				}
				else{
					cout<<dp[level][0]<<" "<<dp[level][1]<<endl;
				}
			}	
			else if(dp[level][2] < dp[level][3]){
				same = (dp[level][3] - dp[level][2])/2;
				same = (1<<level) - same;
				if((k-minus) <= same){
					cout<<dp[level][0]<<" "<<dp[level][1]<<endl;
				}
				else{
					cout<<dp[level][1]<<" "<<dp[level][1]<<endl;
				}
			}
			else{
				cout<<dp[level][0]<<" "<<dp[level][1]<<endl;
			}
		}
		else{
			//even
			dp[0][0] = n/2;
			dp[0][1] = dp[0][0] - 1;
			dp[0][2] = 1;
			dp[0][3] = 1;
			for(i=1;i<62;i++){
				if(dp[i-1][2]>1e17 || dp[i-1][3]>1e17){
					continue;
				}
				dp[i][0] = dp[i-1][0]/2;
				if(dp[i][0]==0)
					dp[i][1] = 0;
				else
					dp[i][1] = dp[i][0] - 1;
				if(dp[i-1][1]&1){
					//dp[i-1][0] is even
					dp[i][2] = dp[i-1][2];
					dp[i][3] = dp[i-1][2] + 2*dp[i-1][3];
				}
				else{
					//dp[i-1][0] is odd
					dp[i][2] = 2*dp[i-1][2] + dp[i-1][3];
					dp[i][3] = dp[i-1][3];
				}
			}
			level = (int)log2(k);
			if(level==0)
				minus = 0;
			else
				minus = (1ll<<(level))-1;
			// cout<<level<<" "<<minus<<" "<<k<<" ";
			// for(i=0;i<10;i++){
			// 	cout<<dp[i][0]<<" "<<dp[i][1]<<" "<<dp[i][2]<<" "<<dp[i][3]<<endl;
			// }
			if(dp[level][2] > dp[level][3]){
				same = (dp[level][2] - dp[level][3])/2;
				if((k-minus) <= same){
					cout<<dp[level][0]<<" "<<dp[level][0]<<endl;
				}
				else{
					cout<<dp[level][0]<<" "<<dp[level][1]<<endl;
				}
			}	
			else if(dp[level][2] < dp[level][3]){
				same = (dp[level][3] - dp[level][2])/2;
				same = (1<<level) - same;
				if((k-minus) <= same){
					cout<<dp[level][0]<<" "<<dp[level][1]<<endl;
				}
				else{
					cout<<dp[level][1]<<" "<<dp[level][1]<<endl;
				}
			}
			else{
				cout<<dp[level][0]<<" "<<dp[level][1]<<endl;
			}	
		}
	}
	return 0;
}
