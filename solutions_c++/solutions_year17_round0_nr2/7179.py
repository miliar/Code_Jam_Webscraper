#include <bits/stdc++.h>

using namespace std;

#define ll long long

int main() {
	//freopen("CJ2.in", "r", stdin);
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	ios_base::sync_with_stdio(false);
	ll t;
	cin >> t;	
	ll casecount =0;
	while(t--){
		++casecount;
		string s;
		cin >> s;
		size_t len = s.length();
		ll i, k;
		for (i = len-1; i>0 ; --i ){
			//cout << s <<" "<<endl;
			if (s[i] < s[i-1]){
				s[i-1] = (char)( (int)s[i-1] - 1);

				for(k=i;k<len;++k)
					s[k] = '9';
				if (s[i] == '0' && i!=len-1)
					s[i+1]= '9';
				s[i] = '9';
			}
			if (s[i] == '0') {
				s[i] = '9';
				//s[i-1] = '9';
			}
		}

		if (s[0] == '0'){
			cout <<"Case #"<<casecount<<": ";
			for( i=1 ;i <len; ++i)
				cout <<s[i];

			cout<<endl;

		}
		else
			cout<<"Case #"<<casecount<<": "<<s<<endl;

	}	//t
}