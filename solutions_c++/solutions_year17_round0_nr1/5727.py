#include <bits/stdc++.h>

using namespace std;
#define F first
#define S second

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("out", "w", stdout);
	int t;
	scanf("%d",&t);
	for(int j = 1 ; j <= t ; ++j){
		string s;
		int k;
		int ans = 0;
		int b = 0;
		cin >> s >> k;
		for(int i = 0 ; i < s.size() ; ++i){
			if(s[i] == '-'){
				++ans;
				//cout << i << " ";
				string sub = s.substr(i,k);
				if(sub.size() != k){
					b=-1;
					break;
				}
				for(int d = i ; d < i+k && d < s.size() ; ++d){
					if(s[d]=='-')s[d]='+';
					else s[d]='-';
				}
			}
		}
		cout << "Case #"<<j<<": ";
		for(int d = 0 ; d < s.size() ; ++d){
			if(s[d]=='-'){
				b=-1;
			}
		}
		if(b == -1)cout << "IMPOSSIBLE" <<endl;
		else cout << ans << endl;

	}
	return 0;
}
