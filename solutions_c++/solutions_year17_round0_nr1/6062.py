#include <bits/stdc++.h>
using namespace std;
int tcs, n, k, a1, a2;
char buf[1005], bufs[1005];
int main(){
	scanf("%i", &tcs);
	for(int tc=1;tc<=tcs;tc++){
		scanf("%s%i", buf, &k);
		a1 = 0; a2 = 0;
		//strcpy(bufs, buf);
		//it should be the same from either direction
		for(int i=0;i<=strlen(buf)-k;i++){
			if(buf[i] == '+') continue;
			a1++;
			for(int j=0;j<k;j++){
				if(buf[i+j] == '+') buf[i+j] = '-';
				else buf[i+j] = '+';
			}
		}
		for(int i=0;i<strlen(buf);i++){
			if(buf[i] == '+') continue;
			a1 = -1;
			break;
		}
		
		if(a1 == -1) printf("Case #%i: IMPOSSIBLE\n", tc);
		else printf("Case #%i: %i\n", tc, a1);
	}
}