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

char s[maxn];

void init(){
	scanf("%s",s+1);
}

void solve(){
	int n,st=1;
	bool flag=true;
	n=strlen(s+1);
	while (flag){
		flag=false;
		fou(i,st+1,n)
			if (s[i-1]>s[i]){
				flag=true;
				s[i-1]--;
				fou(j,i,n) s[j]='9';
			}
		while (st<n && s[st]=='0') st++;
	}
	fou(i,st,n) printf("%c",s[i]);
	printf("\n");
}

int main(){
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	
	int T;
	scanf("%d",&T);
	fou(i,1,T){
		printf("Case #%d: ",i);
		init();
		solve();
	}
	return 0;
}
