#include <iostream>
#include <sstream>
#include <string>
typedef long long int ll;
using namespace std;

ll ones(int n){
	ll ans = 1;
	for(int i = 1; i < n; i++){
		ans *= 10;
		ans += 1;
	}
	return ans;
}
ll nines(int n){
	ll ans = 9;
	for(int i = 1; i < n; i++){
		ans *= 10;
		ans += 9;
	}
	return ans;
}

int main(){
	int t;
	cin >> t;
	for(int T = 1; T <= t; T++){
		cout << "Case #" << T << ": ";
		string s;
		ll n;
		cin >> s;
		stringstream sstr(s);
		sstr >> n;
		int l = s.size();

		if(l == 1) {
			cout << s;
		}
		else if(n < ones(l)){
			cout << nines(l-1);
		} else {
			int v = 0;
			for(int i = 1; i < l ; i++) {
				if(s[i] < s[i-1]) {
					v = i;
					break;
				}
			}

			if(v > 0){
				for(int i = v; i < l; i++) s[i] = '9';
				int i;
				for(i = v-1; i >= 0; i--){
					if(i > 0 && s[i] == s[i-1]) s[i] = '9';
					else break;
				}
				s[i]--;

			}
			cout << s;
		}
		cout << "\n";

	}

}
