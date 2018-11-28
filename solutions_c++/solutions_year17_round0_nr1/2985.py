#include <bits/stdc++.h>
using namespace std;
string s;
int T, record;
int n;
int main(){
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	cin >> T;
	record = T;
	while(T--){
		bool flag = 0;
		int ans = 0;
		cin >> s >> n;
		cout << "Case #" << record - T << ": "; 
		for(int i = 0; i < s.size() - n + 1; i++){
			if(s[i] == '-'){
				for(int j = i; j <= i + n - 1; j++){
					s[j] = (s[j] == '+') ? '-' : '+';
				}
				ans++;
			}
		}
		for(int i = s.size() - n + 1; i < s.size(); i++){
			if(s[i] == '-'){
				cout << "IMPOSSIBLE" << endl;
				flag = 1;
				break;
			}
		}
		if(!flag){
			cout << ans << endl;
		}
	}
return 0;
}

