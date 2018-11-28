#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define ld double
#define vi vector<int>
#define pb push_back
#define mp make_pair
#define F first
#define S second
#define pii pair<int,int>
#define vll vector<ll >
#define rep(i, begin, end) for (__typeof(end) i = (begin) - ((begin) > (end)); i != (end) - ((begin) > (end)); i += 1)
#define all(a) (a).begin(), (a).end()
#define print(s) cerr<<#s<<" : ";for(auto i:(s))cerr<<i<<" ";cerr<<"\n";
#define sd(t) scanf("%d",&(t))
#define pd(t) printf("%d\n",(t))
#define endl "\n"
int main(){
	int t = 1, n;
	sd(t);
	for(int tt = 1; tt <= t; tt++){
		sd(n);
		int R, O, Y, G, B, V;
		sd(R), sd(O), sd(Y), sd(G), sd(B), sd(V);
		//O = R, Y
		// G = Y, B
		// V = R, B
		string ans;
		for(int i = 0; i < n; i++) ans += "0";
		if(O == 0 && G == 0 && V == 0){
			// R, Y, B only.
			if(2 * R > n || 2 * Y > n || 2 * B > n){
				printf("Case #%d: %s\n", tt, "IMPOSSIBLE");
				continue;
			}
			vector<pair<int, int> > vec = {{R, 'R'}, {B, 'B'}, {Y, 'Y'}};
			sort(vec.begin(), vec.end());
			int cnt = 0;
			for(int i = 0; i < vec[0].F; i++) ans[2 * i] = vec[0].S;
			for(int j = 2 * vec[0].F; j < n; j += 2) ans[j] = vec[1].S, cnt++;
			for(int j = 1; cnt < vec[1].F; j += 2, cnt++) ans[j] = vec[1].S;
			for(int j = 0; j < n; j++) if(ans[j] != vec[0].S && ans[j] != vec[1].S) ans[j] = vec[2].S;
			cout << "Case #" << tt << ": " << ans << "\n";
			continue;	
		}
	}
}