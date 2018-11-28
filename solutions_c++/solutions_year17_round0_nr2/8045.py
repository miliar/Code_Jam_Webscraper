#include <bits/stdc++.h>
using namespace std;
// types
typedef long long int ll;

bool nondesc(ll x){
	//cout << "check nondesc x: " << x << endl;
	int last = 10;
	while(x != 0){
		if(x%10 > last){
			return false;
		}
		last = x%10;
		x/=10;
	}
	return true;
}

int main(){
	cin.tie(0);
	ios_base::sync_with_stdio(false);

	ll T;cin >> T;
	for(int tests = 0; tests < T; tests++){
		cout << "Case #"<<tests+1 << ": ";
		string s;
		cin >> s;
		/*while(!nondesc(x)){
			x--;
		}*/
		int n = s.size();
		int si = 0;
		int beg = 0;
		bool diff = false;
		// finde umbruch
		for(int i=1;i<n;i++){
			if((s[i]-'0') > (s[beg]-'0')){
				beg = i;
			}
			else if((s[i]-'0') < (s[beg]-'0')){
				diff = true;
				break;
			}
		}
		if(!diff){
			cout << s << "\n";continue;
		}
		// gehe solange zurück wie gleich gross
		for(int i=0;i<beg;i++){
			cout << s[i];
		}
		int k = (s[beg]-'0')-1;
		if(beg == 0 && s[beg] == '1'){}else{cout << k;}
		for(int i=beg+1;i<n;i++){
			cout << "9";
		}
		// fülle rest mit 9

		cout << "\n";
	}

	return 0;
}
