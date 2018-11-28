#include <bits/stdc++.h>

using namespace std;

char in[25];

int main() {
	
	int T;
	scanf("%d ", &T);
	
	for(int tt = 1; tt <= T; tt++) {
		printf("Case #%d: ", tt);
		fgets(in, 25, stdin);
		int start = 0;
		int i = 0;
		char last = '0';
		while(in[i] >= '0' && in[i] <= '9') {
			if(in[i] < last) {
				i--;
				while(i > 0 && in[i] == last) i--;
				if(in[i] != last) i++;
				if(i == 0 && in[i] == '1') start = 1;
				in[i]--;
				i++;
				while(in[i] >= '0' && in[i] <= '9') {
					in[i] = '9';
					i++;
				}
				break;
			}
			last = in[i];
			i++;
		}
		printf("%s", in+start);
	}
	
	return 0;
}
