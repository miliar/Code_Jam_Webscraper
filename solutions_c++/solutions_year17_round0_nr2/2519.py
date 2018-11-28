#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
int main() {
	int tt;
	cin>>tt;
	for(int xx = 1; xx <= tt; ++xx) {
		cout<<"Case #"<<xx<<": ";
		string s;
		cin>>s;;
		for(int i = 0; i+1 < s.size(); ++i) {
			if(s[i] > s[i+1]) {
				for(int j = i; j > 0; --j) {
					if(s[j] > s[j-1]) {
						--s[j];
						for(int k = j+1; k < s.size(); ++k) {
							s[k] = '9';
						}
						cout<<s<<'\n';
						goto ohi;
					}
				}
				if(s[0] == '1') {
					for(int j = 0; j < s.size()-1; ++j) cout<<'9';
					cout<<endl;
					goto ohi;
				}
				--s[0];
				for(int j = 1; j < s.size(); ++j) s[j] = '9';
				cout<<s<<'\n';
				goto ohi;

			}
		}
		cout<<s<<'\n';
		ohi:;

	}
}
