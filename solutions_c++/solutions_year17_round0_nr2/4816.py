#include <bits/stdc++.h>

#define ll long long
using namespace std;

const int MAXN = 200005;
const int MOD = 1000000007;

int main(){
	ios_base::sync_with_stdio(false);
	int T; cin >> T;
	for(int tc = 1; tc <= T; tc++){
		cout << "Case #" << tc << ": ";
		string s;
		cin >> s;
		int k = s.length();
		int f = 0;
		for(int i=0;i<k-1;i++){
			if(s[i] > s[i+1]){
				if(s[i] == '1'){
					f = 1; break;
				}
				s[i] = s[i]-1;
				int ff = 0;
				for(int j=i-1;j>=0;j--){
					if(s[j] <= s[j+1]) {
						ff = 1; break;
					}
					s[j] = s[j+1];
				}
				if(!ff) 
					for(int j=1;j<=i;j++) s[j] = '9';
				for(int j=i+1;j<k;j++) s[j] = '9';
				break;
			}
		}
		if(f){
			for(int i=0;i<k-1;i++) cout << '9';
		}
		else 
			for(int i=0;i<k;i++) cout << s[i];
		cout << '\n';
	}
	return 0;
}

