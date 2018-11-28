#include<cstdio>
#include<cstring>

int k, s;
char in[1001];

int solve(){
	int ret = 0;
	for(int i=0; i<=s-k; ++i){
		if(in[i]=='-'){
			for(int j=0; j<k; ++j)
				in[i+j] = (in[i+j]=='+') ? '-' : '+';
			ret++;
		}
	}
	for(int i=s-k; i<s; ++i)
		if(in[i]=='-')
			return -1;
	return ret;
}

int main(){
	int t; scanf("%d", &t);
	for(int tt=1; tt<=t; ++tt){
		scanf("%s%d", in, &k);
		s = strlen(in);

		int ans = solve();
		printf("Case #%d: ", tt);
		if(ans>=0) printf("%d\n", ans);
		else puts("IMPOSSIBLE");
	}
}