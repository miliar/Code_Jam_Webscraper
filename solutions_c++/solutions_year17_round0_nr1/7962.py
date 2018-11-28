#include <bits/stdc++.h>

using namespace std;

int T, k, ans;
string str;

bool ok(){
	for(int i = 0 ; i < str.size() ; ++i)
		if(str[i] == '-') return 0;
	return 1;
}

int main(){
	
	freopen("a.in", "r", stdin);
	freopen("a.res", "w", stdout);
	cin.sync_with_stdio(0);
	
	cin >> T;
	for(int t = 1 ; t <= T ; ++t){
		ans = 0;
		cin >> str >> k;
		for(int i = 0 ; i+k-1 < str.size() ; ++i){
			if(str[i] == '-'){
				for(int j = i ; j < i+k ; ++j){
					if(str[j] == '-') str[j] = '+';
					else str[j] = '-';
				}
				ans++;
			}
		}
		
		printf("Case #%d: ", t);
		if(ok()) printf("%d\n", ans);
		else printf("IMPOSSIBLE\n");
	}

	return 0;
}
