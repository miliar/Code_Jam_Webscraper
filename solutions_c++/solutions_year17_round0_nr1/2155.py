#include<iostream>
#include<string>
using namespace std;

int main() {
	int T;
	string s;
	int k;
	cin>>T;
	for(int t=1;t<=T;t++){
		cin>>s>>k;
		size_t idx = s.find('-');
		int ans=0;
		while( (idx != string::npos) && ((idx+k) <= s.size())) {
			for(int i = idx; i<idx+k;i++){
				if(s[i]=='-')
					s[i] = '+';
				else
					s[i] = '-';
			}
			ans++;
			idx = s.find('-',idx+1);
		}
		idx = s.find('-');
		if(idx != string::npos)
			cout<<"Case #"<<t<<": "<<"IMPOSSIBLE"<<endl;
		else
			cout<<"Case #"<<t<<": "<<ans<<endl;
	}

	return 0;
}
