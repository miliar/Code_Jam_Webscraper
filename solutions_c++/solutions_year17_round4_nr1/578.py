#include <bits/stdc++.h>
#define fr(a, b, c) for(int a = b, __ = c; a < __; ++a)
#define dbg(x) cerr << ">>>> " << x << endl;
#define _ << " , " <<

using namespace std;
typedef long long ll;

int g[111];
int c[10];
int main(){
	ios::sync_with_stdio(0);
	int t, cas= 1;
	cin >> t;
	while(t--){
		memset(c, 0, sizeof c);
		int n, p, ans = 0;
		cin >> n >> p;
		fr(i, 0, n){
			cin >> g[i];
			g[i] %= p;		
			if(g[i] == 0)
				ans++;
			c[g[i]]++;
		}
		if(p == 2){
			ans += (n - ans + 1)/2;
		}
		else if(p == 3){
			int o = min(c[1], c[2]);
			c[1] -= o;
			c[2] -= o;
			ans += o;
			ans += (c[1] + c[2] + 2) / 3;
		}
		else{
			int o = min(c[1], c[3]);
			c[1] -= o;
			c[3] -= o;
			ans += o;
			ans += c[2]/2;
			
			c[2] %= 2;
			int s = c[1] + c[3];
			ans += s/4;
			s %= 4;
			if(s + c[2])
				++ans;
		}
		cout << "Case #" << cas++ << ": " << ans << endl;
	}
	return 0;
}
