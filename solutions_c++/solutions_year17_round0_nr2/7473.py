#include <iostream>

using namespace std;

int testcase = 0;

string s;

void ltrim(){
	string ans = "";
	int len = s.size();
	int i = 0;
	while(s[i]=='0') i++;
	while(i<len){
		ans += s[i];
		i++;
	}
	s = ans;
}

bool f(){
	int len = s.size();
	int i = 0;
	while(i<len-1 && s[i]<=s[i+1]) i++;
	if(i<len-1){
		s[i]--;
		i++;
		while(i<len){
			s[i] = '9';
			i++;
		}
		return true;
	}
	return false;
}

void solve(){
	testcase++;
	cin>>s;
	while(f());
	ltrim();
	cout << "Case #"<<testcase<<": "<<s<<endl;
}

int main(){
	int t;
	cin>>t;
	while(t--) solve();
	return 0;
}