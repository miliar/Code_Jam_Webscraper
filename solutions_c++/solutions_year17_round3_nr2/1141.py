#include<bits/stdc++.h>

#define ll long long
#define ld double
#define ii pair<ll, ll>
using namespace std;
int v[1441];
int dp[1441][730][2];
int main(){
	int T;
	cin >> T;
	for(int k = 1; k <= T; k++){
		cout << "Case #" << k << ": ";
		memset(v, -1, sizeof(v));

		int Ac, Aj;
		cin >> Ac >> Aj;
		vector<int> beg;
		while(Ac--){
			int x, y;
			cin >> x >> y;
			beg.push_back(x);
			for(int i = x; i < y; i++){
				if(i == 24*60) i = 0;

				v[i] = 0;
			}
		}
		while(Aj--){
			int x, y;
			cin >> x >> y;
			beg.push_back(x);
			for(int i = x; i < y; i++){
				if(i == 24*60) i = 0;

				v[i] = 1;
			}
		}
		int ans = 1440;
		
		for(int l = 0;l < beg.size(); l++){
			for(int i = 0; i <= 24*60; i++) for(int j = 0; j <= 720; j++)
				dp[i][j][0] = dp[i][j][1] = 100000000;

			dp[0][0][1 - v[beg[l]]] = 0;
			for(int i = 1; i <= 24*60; i++)
				for(int tc = 0; tc <= 720; tc++){
					if(v[(beg[l] + i)%(24*60)] != 1) dp[i][tc][1] = min(dp[i-1][tc][1], (tc > 0 ? dp[i-1][tc-1][0] : 10000000)+ 1);
					if(v[(beg[l] + i)%(24*60)] != 0) dp[i][tc][0] = min((tc > 0 ? dp[i-1][tc-1][0] : 10000000), dp[i-1][tc][1] + 1);
				}
			ans = min(ans, min(dp[1440][720][0], dp[1440][720][1]));
		}
		cout << ans << endl;

	}

}