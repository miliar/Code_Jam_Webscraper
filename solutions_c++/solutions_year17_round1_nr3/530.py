#include <bits/stdc++.h>
using namespace std;
int Hd, Hk, Ad, Ak, B, D;
queue<pair<pair<int, int>, pair<int, int> > > q;
int dp[152][152][152][152], tt[152][152][152][152];
int main(){
	int t;
	scanf("%d", &t); 
	int cs = 0;
	while(t--){
		while(!q.empty()) q.pop();
  		++cs;
  		scanf("%d%d%d%d%d%d", &Hd, &Ad, &Hk, &Ak, &B, &D);
		int ans = -1;
		dp[Hd][Hk][Ad][Ak] = 0;
		tt[Hd][Hk][Ad][Ak] = cs;
		q.push({{Hd, Hk}, {Ad, Ak}});
		while(!q.empty()){
			int cHd = q.front().first.first;
			int cHk = q.front().first.second;
			int cAd = q.front().second.first;
			int cAk = q.front().second.second;
			int turns = dp[cHd][cHk][cAd][cAk]; 

			// cout << cHd << ' ' << cHk << ' ' << cAd << ' ' << cAk << ' ' << turns << endl;

			q.pop();
			if(cHk <= 0){
				ans = dp[cHd][cHk][cAd][cAk];
				break;
			}
			else if(cHd <= 0) continue;

			int ccHd, ccHk, ccAd, ccAk;

			// 1
			ccHd = cHd;
			ccHk = cHk - cAd;
			ccAd = cAd;
			ccAk = cAk;
			if(ccHk <= 0){
				ans = turns + 1;
				break;
			}
			else{
				ccHd = ccHd - ccAk;
				ccHk = ccHk;
				ccAd = ccAd;
				ccAk = ccAk;
				if(ccHd > 0){
					if(tt[ccHd][ccHk][ccAd][ccAk] < cs){
						tt[ccHd][ccHk][ccAd][ccAk] = cs;
						dp[ccHd][ccHk][ccAd][ccAk] = turns + 1;
						q.push({{ccHd, ccHk}, {ccAd, ccAk}});
					}
				}				
			}


			// 2
			ccHd = cHd - cAk;
			ccHk = cHk;
			ccAd = cAd + B;
			ccAk = cAk;
			if(ccHd > 0){

				if(tt[ccHd][ccHk][ccAd][ccAk] < cs){
					tt[ccHd][ccHk][ccAd][ccAk] = cs;
					dp[ccHd][ccHk][ccAd][ccAk] = turns + 1;
					q.push({{ccHd, ccHk}, {ccAd, ccAk}});
				}
			}

			// 3
			ccHd = Hd - cAk;
			ccHk = cHk;
			ccAd = cAd;
			ccAk = cAk;
			if(ccHd > 0){
				if(tt[ccHd][ccHk][ccAd][ccAk] < cs){
					tt[ccHd][ccHk][ccAd][ccAk] = cs;
					dp[ccHd][ccHk][ccAd][ccAk] = turns + 1;
					q.push({{ccHd, ccHk}, {ccAd, ccAk}});
				}
			}
			

			// 4
			ccAk = max(cAk - D, 0);
			ccHd = cHd - ccAk;
			ccHk = cHk;
			ccAd = cAd;
			if(ccHd > 0){
				if(tt[ccHd][ccHk][ccAd][ccAk] < cs){
					tt[ccHd][ccHk][ccAd][ccAk] = cs;
					dp[ccHd][ccHk][ccAd][ccAk] = turns + 1;
					q.push({{ccHd, ccHk}, {ccAd, ccAk}});
				}
			}
		}

  		printf("Case #%d: ", cs);
		if(ans == -1) printf("IMPOSSIBLE\n");
		else printf("%d\n", ans);
		// if(ans == -1) cout << "IMPOSSIBLE\n";
		// else cout << ans << endl;

	}
}