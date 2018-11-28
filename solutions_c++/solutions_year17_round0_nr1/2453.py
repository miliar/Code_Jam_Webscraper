#include <iostream>
#include <algorithm>
#include <vector>
#include <cstring>
#include <map>
#include <set>
#include <cstdio>
using namespace std;
typedef long long LL;

int T,k,n,ans;
char s[1005];

void filp(char &c) {
	if(c=='+') c='-';
	else c='+';
}

bool check() {
	for(int i=0;i<n;i++)
		if(s[i]=='-') return 0;
	return 1;
}

int main() {
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	scanf("%d",&T);
	for(int t=1;t<=T;t++) {
		scanf("%s %d",s,&k);
		n=strlen(s);
		ans=0;
		for(int i=0;i+k<=n;i++) {
			if(s[i]=='+') continue;
			for(int j=i;j<i+k;j++) filp(s[j]);
			ans++;
		}
		printf("Case #%d: ",t);
		if(!check())
			printf("IMPOSSIBLE\n");
		else
			printf("%d\n",ans);
	}
}