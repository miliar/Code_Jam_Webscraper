#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <cstring>
#include <string>
using namespace std;

int main(void) {
	int T, N, len, count, i, j;
	cin >> T;
	char x[1024];
	for (int t=1; t<=T; t++) {
		string s;
		cin >> s >> N;
		len = s.size();
		//printf("%s %d %d\n", s.c_str(), N, len);
		for (i=0; i<len; i++) x[i] = (s[i]=='+') ? 0 : 1;
		//for (int i=0; i<len; i++) printf("%d", x[i]); printf("\n");
		count = 0;
		for (i=0; i<len-N+1; i++) {
			if (x[i]) {
				count++;
				for (j=0; j<N; j++) x[i+j] ^= 1;
			}
		}
		for (i=len-N+1; i<len; i++) {
			if (x[i]) {
				count = -1;
				break;
			}
		}
		printf("Case #%d: ", t);
		if (count == -1) printf("IMPOSSIBLE\n");
		else printf("%d\n", count);
	}
	
	return 0;
}