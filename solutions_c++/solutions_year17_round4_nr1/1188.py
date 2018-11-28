#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define mp make_pair
#define pb push_back
#define fst first
#define snd second
const ll MODP = 1000000007;

int n, p, g[128];

void solve(void){
	cin >> n >> p;
	for(int i=0;i<n;i++) cin >> g[i];
	int c[p] = {0};
	for(int i=0;i<n;i++) c[g[i]%p]++;
	int ans = 0;
	if (p==2){
		ans = c[0] + (c[1]+1)/2;
	}else if (p==3){
		ans = c[0] + min(c[1], c[2]);
		int d = abs(c[1] - c[2]);
		ans += (d+2)/3;
	}else if (p==4){
		ans = c[0];
		if (c[2]%2){
			ans += c[2]/2;
			ans += min(c[1], c[3]);
			int d = abs(c[1] - c[3]);
			ans += (d+5)/4;
		}else{
			ans += c[2]/2;
			ans += min(c[1], c[3]);
			int d = abs(c[1] - c[3]);
			ans += (d+3)/4;
		}
	}
	cout << ans;
	return;
}

int main(void){
	int T;
	cin >> T;
	for(int tcnt=1;tcnt<=T;tcnt++){
		cout << "Case #" << tcnt << ": ";
		solve();
		cout << endl;
	}
	return 0;
}