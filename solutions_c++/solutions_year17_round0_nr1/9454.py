#include <cstdio>
#include <cstring>
#include <iostream>
using namespace std;

void play() {
	string s;
	int sl;
	int k;
	
	cin >> s;
	scanf("%d",&k);
	sl = s.length();
	
	int cnt = 0;
	bool bisa = true;
	for (int i=0; i<sl; i++) {
		if (i+k > sl) {
			if (s[i] == '-') bisa = false;
		} else if (s[i] == '-') {
			cnt++;
			for (int j=0; j<k; j++) {
				if (s[i+j] == '-') s[i+j] = '+';
				else s[i+j] = '-';
			}
		}
	}
	if (bisa) {
		printf("%d\n",cnt);
	} else {
		printf("IMPOSSIBLE\n");
	}
	
}

int main() {
	int t;
	scanf("%d\n",&t);
	for (int i=1; i<=t; i++) {
		printf("Case #%d: ",i);
		play();
	}
}
