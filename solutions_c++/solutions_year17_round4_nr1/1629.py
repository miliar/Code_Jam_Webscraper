#include<bits/stdc++.h>
using namespace std;

int main(){
	ios::sync_with_stdio(0);
	cin.tie(0);
	int T;
	cin >> T;
	for(int I = 1; I <= T; ++I){
		cout << "Case #" << I <<": ";
		int n,p;
		cin >> n >> p;
		vector<int> v(p,0);
		for(int i = 0; i < n; ++i){
			int x;
			cin >> x;
			v[x%p]++;
		}
		int ans = v[0];
		if(p == 2) ans += (v[1]+1)/2;
		if(p == 3) {
			int t = min(v[1], v[2]);
			v[1] -= t;
			v[2] -= t;
			t += (v[1]+2)/3;
			t += (v[2]+2)/3;
			ans += t;
		}
		if(p == 4){
			int t = v[2]/2;
			t += min(v[1], v[3]);
			v[1] -= t;
			v[3] -= t;
			t += (v[1]+3)/4;
			t += (v[3]+3)/4;
			ans += t;
		}
		cout << ans << endl;
	}

}
