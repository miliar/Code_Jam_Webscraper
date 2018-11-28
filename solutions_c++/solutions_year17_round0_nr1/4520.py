#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
#include <cmath>
#include <set>
#include <queue>
#include <stack>
#include <cstring>

//const long long MAXN = 1e7;

using namespace std;
string s;
int k;

int main() {
	int T;
	cin >> T;

	for(int t = 1; t<=T ; t++){
		cout << "Case #" << t << ": ";
		cin >> s;
		cin >> k;
		int len = s.length();

		int ans = 0;
		for(int i=0 ; i<len ; i++){
			if(s[i] == '-' && (i+k-1) < len){
				s[i] = '+';
				for(int j=1;j<k;j++){
					if(s[i+j] == '+') s[i+j] = '-';
					else s[i+j] = '+';
				}
				ans ++;
			}
		}
		bool possible = true;
		for(int i=0; i<len; i++){
			if(s[i] == '-'){
				possible = false;
				break;
			}
		}
		if(!possible) cout << "IMPOSSIBLE\n";
		else cout << ans << "\n";
	} 
    return 0;
}