#include <bits/stdc++.h>
#define M 1000

using namespace std;

char s[M+2];
bool a[M+1];
int n,k;

void input(void){
	scanf("%s %d",&s,&k);
	n=strlen(s);
}

void process(void){
	int i,j,cnt;
	for(i=0;i<n;i++)a[i]=0;

	for(i=cnt=0;i+k<=n;i++){
		if(s[i]=='-') a[i]=!a[i];
		if(a[i]){
			cnt++;
			for(j=0;j<k;j++) a[i+j]=!a[i+j];
		}
	}
	for(;i<n;i++) if(a[i] ^ (s[i]=='-')){
		printf("IMPOSSIBLE\n");
		return;
	}
	printf("%d\n",cnt);
}

int main(){
	freopen("input.txt","r",stdin);

	int t;
	scanf("%d",&t);
	for(int i=1;i<=t;i++){
		printf("Case #%d: ",i);
		input();
		process();
	}
	return 0;
}
