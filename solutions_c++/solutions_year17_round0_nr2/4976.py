#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef long double ld;
typedef vector<int> vi;
typedef vector<double> vd;





int main() {
freopen("B-large.in","r", stdin);
freopen("Output.out", "w", stdout);
	string s;
	int t;
	cin>>t;
	for(int i=1 ; i<=t ; i++){
		cin>>s;
		for (int j = 0; j < s.size()-1; ++j) {
			if(s[j]>s[j+1]){
				s[j]--;
				for (int it = j+1; it < s.size(); ++it) {
					s[it]='9';
				}
				for (int it = j; it > 0; --it) {
					if(s[it-1]>s[it]){
						s[it]='9';
						s[it-1]--;
					}else
						break;
				}
				break;
			}
		}
		if(s[0]=='0')
			s=s.substr(1);


		cout<<"Case #"<<i<<": "<<s<<endl;
	}
}
