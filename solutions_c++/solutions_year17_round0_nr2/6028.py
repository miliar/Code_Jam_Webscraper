#include <bits/stdc++.h>
using namespace std;
int tcs, li, si, len;
char buf[500];
bool f = false, cf;

int main(){
	scanf("%i", &tcs);
	for(int tc=1;tc<=tcs;tc++){
		scanf("%s", buf);
		int len = strlen(buf);
		f = false;
		for(int i=0;i<len;i++){
			if(!i) continue;
			if(buf[i] >= buf[i-1]) continue;
			f = true;
			li = i;
			break;
		}
		if(f){
			printf("Case #%i: ", tc);
			si = 0;
			buf[li - 1]--; //it should never be 0
			for(int i=li-1;i>=0;i--){
				if(buf[i] == '0' && !i) {si = 1; break; }
				if(buf[i] >= buf[i-1]) break; //done
				buf[i-1]--;
				buf[i] = '9';
			}
			buf[li] = 0;
			printf("%s", buf + si);
			for(int i=li;i<len;i++) printf("9");
			puts("");
		} else {
			printf("Case #%i: %s\n", tc, buf);
		}
	}
}