#include <iostream>
using namespace std;

int main(){
	int N; cin >> N;
	for (int i=1;i<=N;i++){
		string s; cin >> s;
		int k; cin >> k;
		int ans = 0;
		for (int j=0;j+k <= s.length();j++){
			if (s[j] == '+') continue;
			else {
				for (int l=0;l<k;l++){
					if (s[j+l] == '+') s[j+l] = '-'; else s[j+l] = '+';
				}
				ans++;
			}
		}
		bool pos = true;
		for (int j=0;j<s.length();j++){
			if (s[j] == '-') {
				cout << "Case #" << i << ": IMPOSSIBLE\n" ;
				pos = false;
				break;
			}
		}
		if (pos) cout << "Case #" << i << ": " << ans << endl;
	}
}
