#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<iostream>
#include<algorithm>
#include<vector>
#include<string>
using namespace std;

char flip(char c){
	return c == '-' ? '+' : '-';
}

void run() {
	string s;
	int k;
	cin >> s >> k;
	int res=0;
	for(int i=0;i+k<=s.size();++i) {
		if (s[i]=='-') {
			++ res;
			for(int j=0;j<k;++j) 
				s[i+j]=flip(s[i+j]);
		}
	}
	for(int i=0;i<s.size();++i)
		if (s[i]=='-') res=-1;
	if (res < 0)
		printf("IMPOSSIBLE\n");
	else
		printf("%d\n", res);
}

int main() {
	freopen("A-large.in","r",stdin);
	freopen("A.out","w",stdout);
	int T;
	cin >>T;
	for (int i=1;i<=T;++i) {
		printf("Case #%d: ", i);
		run();
	}
}
