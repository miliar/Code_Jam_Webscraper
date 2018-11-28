#include <iostream>
using namespace std;
int main() {
	int tt;
	cin>>tt;
	for(int i = 1; i <= tt; ++i) {
		cout<<"Case #"<<i<<": ";
		string s;
		cin>>s;
		int k;
		cin>>k;
		int q = 0;
		for(int j = 0; j+k-1 < s.size(); ++j) {
			if(s[j] == '-') {
				++q;
				for(int jj = 0; jj < k; ++jj) {
					if(s[j+jj] == '-') s[j+jj] = '+';
					else s[j+jj] = '-';
				}
			}
		}
		int ok = 1;
		for(int j = 0; j < s.size(); ++j) {
			if(s[j] == '-') ok = 0;
		}
		if(ok) {
			cout<<q<<'\n';
		}
		else {
			cout<<"IMPOSSIBLE\n";
		}
	}

}
