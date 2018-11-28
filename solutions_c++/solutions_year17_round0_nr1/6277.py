#include<iostream>


using namespace std;

int main(){
	int T, n, ans;
	string ss;
	cin >> T;
	
	for(int t = 1; t <= T; t++){
		cin >> ss >> n;
		
		int len = ss.length();
		ans = 0;
		
		for(int i = 0; i <= len - n; i++){
			if(ss[i] == '+') continue;
			ans++;
			for(int j = 0; j < n; j++){
				ss[i+j] = ss[i+j] == '+' ? '-' : '+';
			}
		}
		bool ch = 1;
		for(int i = 0; i < len; i++){
			if(ss[i] == '-'){
				ch = 0;
				break;
			}
		}
		if(ch) cout << "Case #" << t << ": " << ans << endl;
		else cout << "Case #" << t << ": " << "IMPOSSIBLE" << endl;
	}
	
	
}