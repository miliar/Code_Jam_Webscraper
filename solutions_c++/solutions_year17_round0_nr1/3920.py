#include <algorithm>
#include <vector>
#include <limits.h> 
#include <string.h>
#include <stdio.h>
#include <iostream>
#include <unordered_map>
#include <queue>
#include <sstream>


using namespace std;
#define ll long long


void slove(int t, string &s, ll k) {
	int n = s.size();
	int res = 0;
	for(int i=0;i<=n-k;i++) {
		if(s[i] == '-') {
			for(int j=i;j<i+k;j++) {
				if(s[j] == '-') s[j] = '+';
				else s[j] = '-';
			}
			res += 1;
		}
	}
	bool f = true;
	for(int i=0;i<n;i++) {
		if(s[i] == '-') f = false;
	}
	if(f) {
		cout<<"Case #"<<t<<": "<<res<<endl;
	}else {
		cout<<"Case #"<<t<<": "<<"IMPOSSIBLE"<<endl;
	}
}

int main(int argc, char *argv[]) {
	if(argc >= 2) {
        freopen(argv[1], "r", stdin);
    }else{
        freopen("A.in", "r", stdin);    
    }
	int t;
	cin>>t;
	for(int i=0;i<t;i++) {
		string s;
		ll k;
		cin>>s>>k;
		slove(i+1,s,k);
	}
	return 0;
}