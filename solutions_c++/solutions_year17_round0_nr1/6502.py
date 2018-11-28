#include <bits/stdc++.h>
using namespace std;
#define FOR(i,n) for(int i=0;i<(n);i++)

const int N = 1100;
char s[N];
int tmp[N], a[N];
int b;
int len;

void flip(int x){
	assert(x+b<=len);
	for(int i=x;i<x+b;i++){
		a[i] = 1-a[i];
	}
}

bool check(){
	int sum=0;
	FOR(i,len) sum += a[i];
	return (sum==len) || (sum==0);
}

int solve(){
	bool res = false;
	int count = 0, ans = 1<<30;
	FOR(i,len) a[i] = tmp[i];
	FOR(i,len-b+1) {
		if(a[i] == 0) {flip(i);count++;}
	}
	if(check()) {
		res = true;
		ans = min(ans, count);
	}
	count = 0;
	FOR(i,len) a[i] = tmp[i];
	FOR(i,len-b+1) {
		if(a[i] == 1) {flip(i);count++;}
	}
	if(check()) {
		res = true;
		ans = min(ans, count);
	}
	if(!res) ans = -1;
	return ans;
}

int main(){
	int T, t=0;
	scanf("%d",&T);
	while(t<T){
		t++;
		printf("Case #%d: ", t);
		scanf("%s %d", s, &b);
		len = strlen(s);
		//puts(s);
		FOR(i,len){
			if(s[i] == '+') tmp[i] = 1;
			else tmp[i] = 0;
		}
		int res = solve();
		if(res == -1) puts("IMPOSSIBLE");
		else printf("%d\n", res);
	}
}

