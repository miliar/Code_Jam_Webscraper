#include <iostream>
#include <string>

using namespace std;

int ans;

void solve(int i, string s, int n, int k){
	//cout << i << " " << s << endl;
	int j;
	for(j = 0; j < s.size(); ++j)
		if(s[j] == '-') break;
	if(j == s.size()){
		ans = (ans > n or ans == -1) ? n : ans;
		return; 
	}

	if(i == s.size()-k+1) return;

	solve(i+1,s, n, k);

	for(j = 0; j < k; ++j)
		s[i+j] = (s[i+j] == '-') ? '+' : '-';

	solve(i+1,s, n+1, k);

}


int main(){
	int T, k;
	string s;
	cin >> T;
	for(int i = 1; i <= T; ++i){
		ans = -1;
		cin >> s >> k;
		solve(0,s,0, k);
		cout << "Case #" << i << ": ";
		if(ans == -1)
			cout << "IMPOSSIBLE" << endl;
		else
			cout << ans << endl;
	}
}