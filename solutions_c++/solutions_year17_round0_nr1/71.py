#include<stdio.h>
#include<string.h>

char st[1010]; int N, K;

void test(int tn){
	scanf("\n%s %d", st, &K); N=strlen(st);
	printf("Case #%d: ", tn);
	int cnt=0;
	for(int i=0; i<N; i++){
		if(st[i]=='+')continue;
		if(i+K > N){ puts("IMPOSSIBLE"); return; }
		cnt++;
		for(int j=i; j<i+K; j++)st[j] = '+'+'-'-st[j];
	}
	printf("%d\n", cnt);
}

int main(){
	int t;
	freopen("A-large.in", "r", stdin), freopen("output.txt","w",stdout);
	scanf("%d", &t);
	for(int i=1; i<=t; i++)test(i);
	return 0;
}
