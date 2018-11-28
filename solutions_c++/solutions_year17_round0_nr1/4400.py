#include <iostream>
#include <algorithm>
#include <vector>
#include <string>

using namespace std;

int main() {
	int T,K,count = 0,i=1,j,l;
	vector<int> v;
	string s;
	cin>>T;
	while(i<=T) {
		count = 0;
		cin>>s>>K;
		for(j=0;j<s.size();j++) {
			if(s[j] == '-') {
				if(s.size()-j<K) {
					cout<<"Case #"<<i<<": IMPOSSIBLE\n";
					count = -1;
					break;
				}
				else {
					for(l=0;l<K;l++) {
						if(s[l+j] == '-') s[l+j] = '+';
						else s[l+j] = '-';
					}
					count++;
				}
			}
		}
		if(count>=0) cout<<"Case #"<<i<<": "<<count<<"\n";
		i++;
	}
	return 0;
}