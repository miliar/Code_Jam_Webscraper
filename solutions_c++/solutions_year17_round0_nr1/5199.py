#include <bits/stdc++.h>
using namespace std;
void solve(){
	int k;string s;
	cin >> s >> k;
	int n = s.size(), cnt = 0;
	for(int i=0;i<n;i++){
		if(s[i] == '-' && i+k <= n) {
			cnt++;
			for(int j=i;j<i+k;j++){
				if( s[j] == '-' ) s[j] = '+';
				else if( s[j] == '+' ) s[j] = '-';
			}
		}
	}
	bool ok = true;
	for(int i=0;i<n;i++){
		if(s[i] == '-') ok = false;
	}
	if(ok){
		cout << cnt;
	}else{
		cout << "IMPOSSIBLE";
	}
}
int main(void){
	int T;
	cin >> T;

	for(int i=0;i<T;i++){
		cout << "Case #" << i+1 << ": ";
		solve();
		cout << endl;
	}

	return 0;
}