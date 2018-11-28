#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef long double ld;
typedef vector<int> vi;
typedef vector<double> vd;





int main() {
	freopen("A-large.in", "r", stdin);
	freopen("Output.out", "w", stdout);
	string s;
	int t,n,c,f;
	cin>>t;
	for(int i=1 ; i<=t ; i++){
		c=f=0;
		cin>>s>>n;
		for (int j = 0; j <= s.size()-n; ++j) {
			if(s[j]=='-'){
				c++;
				for (int it = 0; it < n; ++it) {
					if(s[j+it]=='-')
						s[j+it]='+';
					else
						s[j+it]='-';
				}
			}
		}
		for (int j = 0; j < s.size(); ++j) {
			if(s[j]=='-'){
				f=1;
				break;
			}
		}
		cout<<"Case #"<<i<<": ";
		if(f) cout<<"IMPOSSIBLE";
		else cout<<c;
		cout<<endl;
	}
}

