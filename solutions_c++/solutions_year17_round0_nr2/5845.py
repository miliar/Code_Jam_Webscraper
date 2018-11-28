#include <iostream>
#include <cmath>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <map>
#include <set>

using namespace std;

string run(string s) {
	for(int i = 0;i<s.size()-1;i++) {
		if(s[i]>s[i+1]){
			s[i]--;
			for(int j = i+1;j<s.size();j++)s[j] = '9';
			i = -1;
			continue;
		}
	}
	if(s[0] == '0' && s.size() >1)s = s.substr(1,s.size()-1);
	return s;
}

int main () {

	int t;
	cin>>t;
	for(int c = 1;c<=t;c++){
		printf("Case #%d: ", c);
		string s;
		cin>>s;
		cout<<run(s)<<endl;

	}

	return 0;
}