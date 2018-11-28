#include<cstdio>
#include<cstring>
#include<algorithm>
#include<iomanip>
#include<sstream>
#include<iostream>
#include<string>
#include<vector>
#include<queue>
#include<set>
#include<map>
#include<bitset>
#define fou(i,j,k) for (int i=j;i<=k;i++)
#define fod(i,j,k) for (int i=j;i>=k;i--)
using namespace std;

typedef long long LL;
typedef unsigned long long ULL;
typedef pair<int, int> Pii;

const int maxn=1010;
const int inf=0x3f3f3f3f;
const LL infLL=0x3f3f3f3f3f3f3f3fLL;

int n,K,a[maxn];
char s[maxn];

void init(){
	scanf("%s%d",s+1,&K);
}

int check(int flag){
	int cnt=0;
	fou(i,1,n)
		if ((a[i]^1)==flag){
			if (i+K-1>n) return inf;
			fou(j,i,i+K-1) a[j]^=1;
			cnt++;
		}
	return cnt;
}

void solve(){
	int ans;
	n=strlen(s+1);
	fou(i,1,n)
		if (s[i]=='+') a[i]=1; else a[i]=0;
	ans=check(1);
	if (ans==inf) printf("IMPOSSIBLE\n");
	else printf("%d\n",ans);
}

int main(){
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	
	int T;
	scanf("%d",&T);
	fou(i,1,T){
		printf("Case #%d: ",i);
		init();
		solve();
	}
	return 0;
}
