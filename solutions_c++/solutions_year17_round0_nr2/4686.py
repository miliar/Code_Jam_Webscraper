#include <bits/stdc++.h>

using namespace std;

typedef long long int ll;
typedef pair<ll, ll> pii;


#define se second
#define fi first
#define pb push_back
#define mp make_pair

void print(int t) {
	cout<<"Case #"<<t<<": ";
}

void print(int t, int ans) {
	cout<<"Case #"<<t<<": "<<ans<<endl;
}



int main() {
    ios::sync_with_stdio(false);
    int t;
    cin>>t;
    for(int T = 1; T<=t; T++) {
    	string str;
    	cin>>str;
    	bool flag = false;
    	for(int i = 0; i+1 < str.size(); i++) {
    		if(str[i+1] < str[i]) {
    			str[i]--;
    			for(int j = i+1; j< str.size(); j++) {
    				str[j] = '9';
    			}
    			for(int j = i-1; j>=0; j--) {
    				if(str[j] <= str[j+1]) {
    					break;
    				} else {
    					str[j+1] = '9';
    					str[j]--;
    				}
    			}
    			break;
    		}
    	}
    	if(str[0] == '0') {
    		str = str.substr(1, str.size()-1);
    	}
    	print(T);
    	cout<<str<<endl;
    }
}