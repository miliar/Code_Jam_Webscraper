#include <bits/stdc++.h>

using namespace std;

#define ll long long

int main() {
	//freopen("CJ1-long.in", "r", stdin);
	//freopen("CJ1-long.out", "w", stdout);
	ios_base::sync_with_stdio(false);
	ll t;
	cin >> t;	
	ll casecount =0;
	while(t--){
		++casecount;
		ll count=0;
		string s;
		ll k;
		cin >> s>> k;
		ll i=0,j=0;
		size_t len = s.length();

		while(i<= (len-k)) {
			if(s[i] == '-'){
				++count;
				for(j=i ; j< (i+k); ++j) {
					if (s[j] == '-')
						s[j] = '+';
					else
						s[j] = '-';
				}
			}	// if
			++i;
		}
		bool flag = 1;
		for(j=i;j<len;++j){
			if (s[j] == '-'){
				flag = 0;
				cout <<"Case #"<<casecount<<": "<< "IMPOSSIBLE" <<endl;
				break;

			}
		}	//for
		if (flag)
		cout <<"Case #"<<casecount<<": "<<count<<endl;
	}	//t loop
}