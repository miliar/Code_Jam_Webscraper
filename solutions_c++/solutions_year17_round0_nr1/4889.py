#include<iostream>
using namespace std;

void flip(string &s, int pos, int k) {
	for(int i=pos;i<pos+k;i++) {
		s[i] = s[i]=='+'?'-':'+';
	}
}

int calc(string &s, int k) {
	int res = 0;
	int len = s.length();
	for(int i=0;i<len;i++) {
		if (s[i] == '-') {
			if (i+k>len) {
				return -1;
			}
			res++;
			flip(s, i, k);
		}
	}
	return res;
}

int main() {
	int T;
	cin>>T;
	for(int t=1;t<=T;t++) {
		string s;
		int k;
		cin>>s>>k;
		int res = calc(s, k);
		cout<<"Case #"<<t<<": ";
		if (res == -1) {
			cout<<"IMPOSSIBLE"<<endl;
		} else {
			cout<<res<<endl;
		}
	}
	return 0;
}
