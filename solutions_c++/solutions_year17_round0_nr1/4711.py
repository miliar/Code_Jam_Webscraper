#include <bits/stdc++.h>

using namespace std;

typedef long long int ll;
typedef pair<ll, ll> pii;


#define se second
#define fi first
#define pb push_back
#define mp make_pair

char inv(char ch) {
	if(ch == '-') {
		return '+';
	}
	return '-';
}

int main() {
    ios::sync_with_stdio(false);
    int t;
    cin>>t;
    for(int T = 1; T<=t; T++) {
    	string str;
    	int k;
    	cin>>str>>k;
    	bool flag = false;
    	int ans = 0;
    	for(int i = 0; i < str.size(); i++) {
    		if(str[i] == '-') {
    			if(i+k > str.size()) {
    				flag = true;
    				break;
    			} else {
    				for(int j = i; j < i+k; j++) {
    					str[j] = inv(str[j]);
    				}
    				ans++;
    			}
    		}
    	}
    	if(flag) {
    		cout<<"Case #"<<T<<": IMPOSSIBLE\n";
    	} else {
    		cout<<"Case #"<<T<<": "<<ans<<endl;
    	}
    }
}