#include<bits/stdc++.h>

#define pb push_back
#define f(x) (x&(-x))
#define lld long long
#define mod 1000000007

using namespace std;

int N,M,ans;
int a[102];

void process(){
	scanf("%d %d",&N,&M);
	int t[4] = {0,0,0,0};
	for(int i=1; i<=N; i++){
		scanf("%d",&a[i]);
		t[a[i]%M]++;
	}
	if(M == 2){
		ans = t[0]+(t[1]+1)/2;
	}else if(M == 3){
		ans = t[0]+min(t[1],t[2])+(max(t[1],t[2])-min(t[1],t[2])+2)/3;
	}
	printf("%d\n",ans);
}

int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	int T;
	scanf("%d",&T);
	for(int i=1; i<=T; i++){
		printf("Case #%d: ",i);
		process();
	}

	return 0;
}
