#include <bits/stdc++.h>
using namespace std;

#define pb         push_back

typedef long long ll;
const ll INF = 1000000000000000000ll;
const ll MOD = 1000000007ll;
const double EPS = 1e-8;

int main(void) {
	//ios_base::sync_with_stdio(false);
	//cin.tie(0);
	
	int t;
	cin >> t;

	for(int l=1; l<=t; l++){
		string s;
		cin >> s;
		int k;
		cin >> k;
		int ans = 0;

		for(int i=0; i<=s.size() - k; i++){
			if(s[i] == '-'){
				ans++;
				for(int j=0; j<k; j++){
					if(s[i+j] == '-') s[i+j] = '+';
					else if(s[i+j] == '+') s[i+j] = '-';
				}
			}
		}

		//cout << s << endl;

		bool f = true;
		for(int i=0; i<s.size(); i++){
			if(s[i] != '+'){
				f =false;
				break;
			}
		}

		if(f){
			printf("Case #%d: %d\n", l, ans);
		}else{
			printf("Case #%d: IMPOSSIBLE\n", l);
		}
	}

	
	return 0;
}
