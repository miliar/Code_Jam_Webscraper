#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

int main() {

    ll t, n, m, i, j, k, a, b, x, ans;
    cin>>t;
    string s;
    for (a = 1; a <= t; ++a) {
    	cin >> s;

    	cin>>k;

    	ans = 0;
    	bool flag = true;
    	for (i=0; i<s.length(); i++) {
    		if (s[i]=='+') {
    			continue;
    		}
    		else {
    			// cout<<i<<endl;
    			if ((i+k)<=s.length()) {
    				for (j=i; j<(i+k); j++) {
    					if (s[j]=='+') {
    						s[j] = '-';
    					}
    					else {
    						s[j] = '+';
    					}
    				}
    				ans++;
    			}
    			else {
    				flag = false;
    				break;
    			}
    		}
    	}


		cout << "Case #" << a << ": ";
		if (flag) {
			cout<<ans<<endl;
		}
		else {
			cout<<"IMPOSSIBLE"<<endl;
		}
	}


    return 0;

}