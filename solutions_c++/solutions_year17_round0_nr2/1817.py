#include<bits/stdc++.h>
#define x first
#define y second
using namespace std;
int t;
long long n,ans;
char s[105];
int main(){
	freopen("B-large.in","r",stdin);
	freopen("BL.out","w",stdout);
	scanf("%d",&t);
	for(int _=1;_<=t;++_){
		scanf("%lld",&n);
		sprintf(s,"%lld9",n);
		int len=strlen(s);
		int find=-1;
		for(int i=0;i<len-1;++i){
			if(s[i]>s[i+1]){
				find=i;
				break;
			}
		}
		if(~find){
			while(find&&s[find]==s[find-1])--find;
			--s[find++];
			for(;find<len;++find)s[find]='9';
		}
		char *g=s;
		if(n)while(*g=='0')++g;
		s[len-1]=0;
		printf("Case #%d: %s\n",_,g);
	}
	return 0;
}

