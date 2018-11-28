#include<iostream>
#include<cstdio>
#include<string>

using namespace std;

int t,k;
string s;

void flip(int j) {
	for(int i=j; i<j+k; i++) {
		if(s[i]=='-') s[i]='+';
		else s[i]='-';
	}
}

int main() {
	cin >> t;
	for(int numcase=1; numcase<=t; numcase++) {
		int count=0;
		cin >> s >> k;
		int it=0;
		while( it<=s.size()-k ) {
			if(s[it]=='-') {
				flip(it);
				count++;
			}
			it++;
		}
		bool temp=true;
		while(it<s.size()) {
			if(s[it]=='-') {
				temp=false;
				break;
			}
			it++;
		}
		printf("Case #%d: ", numcase);
		if(temp) printf("%d", count);
		else printf("IMPOSSIBLE");
		cout << endl;
	}
	
	return 0;
}
