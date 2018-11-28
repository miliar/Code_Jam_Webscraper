#include <cstdio>
#include <cstring>
#include <vector>
#include <algorithm>
using namespace std;

const int N=100;
char s[N][N];

int main() {
	int i, j, k, r, c, ncase, icase;
	scanf("%d", &ncase);
	for(icase=1; icase<=ncase; icase++) {
		scanf("%d%d", &r, &c);
		for(i=0; i<r; i++) scanf("%s", s[i]);
		for(i=0; i<r; i++) for(j=0; j<c; j++) if(s[i][j]!='?') {
			char ch=s[i][j];
			for(k=j-1; k>=0 && s[i][k]=='?'; k--) s[i][k]=ch;
			for(k=j+1; k<c && s[i][k]=='?'; k++) s[i][k]=ch;
		}
		for(i=0; i<r; i++) if(s[i][0]=='?') {
			for(j=i; j<r && s[j][0]=='?'; j++);
			if(j==r) {
				for(j=i; j>=0 && s[j][0]=='?'; j--);
			}
			strcpy(s[i], s[j]);
		}
		printf("Case #%d:\n", icase);
		for(i=0; i<r; i++) printf("%s\n", s[i]);
	}
	return 0;
}