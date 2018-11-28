#include <bits/stdc++.h>
using namespace std;

char str[1050];
int c[1050];
int n, k;

int lowbit(int x){
	return x&(-x);
}

void update(int x){
	while(x<=n){
		c[x]^=1;
		x+=lowbit(x);
	}
}

int query(int x){
	int ans=0;
	while(x){
		ans^=c[x];
		x-=lowbit(x);
	}
	return ans;
}

int main()
{
	int T;
	scanf("%d", &T);
	for(int t=1;t<=T;t++){
		scanf("%s%d", str+1, &k);
		n=strlen(str+1);
		memset(c, 0, sizeof(c));
		for(int i=1;i<=n;i++){
			if(str[i]=='+'){
				update(i);
				update(i+1);
			}
		}
		int ans=0;
		bool ok=true;
		for(int i=1;i<=n-k+1;i++){
			if(!query(i)){
				ans++;
				update(i);
				update(i+k);
			}
		}
		for(int i=n-k+2;i<=n;i++){
			if(!query(i))ok=false;
		}
		printf("Case #%d: ", t);
		if(ok)printf("%d\n", ans);
		else printf("IMPOSSIBLE\n");
	}
}

