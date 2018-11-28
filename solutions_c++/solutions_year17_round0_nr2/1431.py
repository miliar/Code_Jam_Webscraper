#include <iostream>
#include <string>
using namespace std;

bool possible(string s, string cand) {
	cand+=string(s.size()-cand.size(),cand[cand.size()-1]);
	for(int i=0;i<s.size();i++) if(cand[i]<s[i]) return true;
	else if(cand[i]>s[i]) return false;
	return true;
}

void solve(int tc) {
	string s;
	cin>>s;
	string ret;
	for(int i=0;i<s.size();i++) {
		char low='0';
		if(i>0) low=ret[i-1];
		for(char j='9';j>=low;j--) {
			string cand=ret;
			cand+=j;
			if(possible(s, cand)) {
				ret+=j;
				break;
			}
		}
	}
	int idx=0;
	while(idx+1<ret.size()&&ret[idx]=='0') idx++;
	cout<<"Case #"<<tc<<": "<<ret.substr(idx,ret.size()-idx)<<endl;

}

int main() {
	int t;
	cin>>t;
	for(int i=1;i<=t;i++) solve(i);
}
