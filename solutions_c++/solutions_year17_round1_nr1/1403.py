#include <bits/stdc++.h>
#define fr(x) scanf("%d", &x)
using namespace std;

char s[32][32];

int main(){
	int t, r, c;
	fr(t);
	for(int t1=1; t1<=t ;++t1){
		fr(r);
		fr(c);
		for(int i=1; i<=r; ++i) {
			scanf(" %s", &s[i][1]);
		}
		for(int i=2; i<=r; ++i) {
			bool all=1;
			for(int j=1;j<=c;++j){
				if(s[i][j]!='?'){
					all=0;
				}
			}
			if(all){
				for(int j=1;j<=c;++j){
					s[i][j]=s[i-1][j];
				}
			}
		}
		for(int i=r-1; i>=1; --i) {
			bool all=1;
			for(int j=1;j<=c;++j){
				if(s[i][j]!='?'){
					all=0;
				}
			}
			if(all){
				for(int j=1;j<=c;++j){
					s[i][j]=s[i+1][j];
				}
			}
		}
		for(int i=1; i<=r; ++i) {
			for(int j=2;j<=c;++j){
				if(s[i][j]=='?'){
					s[i][j]=s[i][j-1];
				}
			}
		}
		for(int i=1; i<=r; ++i) {
			for(int j=c-1;j>=1;--j){
				if(s[i][j]=='?'){
					s[i][j]=s[i][j+1];
				}
			}
		}
		printf("Case #%d:\n", t1);
		for(int i=1; i<=r; ++i) {
			printf("%s\n", &s[i][1]);
		}
	}
	return 0;
}