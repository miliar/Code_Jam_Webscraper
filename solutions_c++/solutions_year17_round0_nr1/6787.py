#include <bits/stdc++.h>
using namespace std;

void flip(string &s) {
	for(int i=0; i<s.size(); i++) {
		if(s[i] == '-') s[i] = '+';
		else s[i] = '-';
	}
}

int main() {
	int T;
	cin>>T;
	for(int i=1; i<=T; i++) {
		string s;
		int k;
		cin>>s>>k;
		int len = s.size();
		map<string, int> m1, m2;
		string s1 = s.substr(0, k);
		m1[s1] = 0;
		flip(s1);
		m1[s1] = 1;
		for(int j=k; j<len; j++) {
			for(auto iter = m1.begin(); iter!=m1.end(); iter++) {
				if(iter->first[0] == '-') continue;
				string s2 = iter->first.substr(1, k-1);
				//cout<<s2<<endl;
				s2 += s[j];
				m2[s2] = iter->second;
				flip(s2);
				m2[s2] = iter->second+1;
			}
			swap(m1, m2);
			m2.clear();
		}
		string s3 = "";
		for(int h=0; h<k; h++) s3+='+';
		auto iter2 = m1.find(s3);
		if(iter2 == m1.end()) cout<<"Case #"<<i<<": IMPOSSIBLE"<<endl;
		else {
			cout<<"Case #"<<i<<": "<<iter2->second<<endl;
		}
	}
	return 0;
}