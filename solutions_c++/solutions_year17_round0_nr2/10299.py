#include <bits/stdc++.h>
using namespace std;

vector<int> v;

void solve(int x){
	while(x){
		v.push_back(x%10);
		x = x/10;
	}
}

int main(){
	int n, t, caso = 1;
	
	cin >> t;
	while(t--){
		cin >> n;
		int ans;
		for(int i = 1; i <= n; i++){
			bool flag = true;
			v.clear();
			solve(i);
			for(int j = 0; j < v.size()-1 and flag; j++)
				if(v[j] < v[j+1])
					flag = false;
			if(flag)
				ans = i;
		}
		cout << "Case #" << caso++ << ": " << ans << '\n';
	}
	
	
	return 0;
}