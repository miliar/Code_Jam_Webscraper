#include<iostream>
#include<vector>
using namespace std;
int main() {
	int t;
	cin>>t;
	int casenum = 0, ans;
	while(t--) {
		casenum++;
		string s;
		int k;
		cin>>s>>k;
		int temp = 0;
		int len = s.length();
		vector<int> v;
		for(int i = 0; i < len; i++) {
			if(s[i] == '+') v.push_back(0);
			else v.push_back(1);
		}
		for(int i = 0; i < len - k + 1; i++) {
			for(int j = 1; j < k; j++) {
				v[i+j] ^= v[i];
			}
		}
		
		int flag = 1;
		for(int i = len - k + 1; i < len; i++) {
			if(v[i] == 1) {
				cout<<"Case #"<<casenum<<": "<<"IMPOSSIBLE"<<endl;
				flag = 0;
				break;
			}
		}
		if(flag == 1) {
			ans = 0;
			for(int i = 0; i < len; i++) {
				if(v[i] == 1) ans++;
			}
			cout<<"Case #"<<casenum<<": "<<ans<<endl;
		}
	}
}
