#include <iostream>
#include <string>
using namespace std;

string s;
int k;
int ans;
int T;
void solve(){
	int len = s.length();
	ans = 0;
	for (int i = 0; i <= len - k; i++){
		if (s[i] == '-') {
			ans++;
			for (int j = i; j <= i + k -1; j++)
				if (s[j] == '+')
					s[j] = '-';
				else if (s[j] == '-')
					s[j] = '+';
		}
	}

	for (int i = len-k+1; i < len; i++)
		if (s[i] == '-'){
			ans = -1;
			break;
		}
}

int main(){
	cin >> T;
	for (int kase = 1; kase <= T; kase++) {		
		cin >> s >> k;
		solve();

		cout << "Case #" << kase << ": ";
		if (ans == -1)
			cout << "IMPOSSIBLE" << endl;
		else cout << ans << endl;
	}
	return 0;
}