#include <iostream>
#include <algorithm>
#include <vector>
#include <cstring>
#include <map>
#include <set>
#include <cstdio>
using namespace std;
typedef long long LL;

int T,n,pos;
char s[30];

int main() {
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	scanf("%d",&T);
	for(int t=1;t<=T;t++) {
		scanf("%s",s);
		n=strlen(s);
		pos=n;
		for(int i=0;i<n-1;i++)
			if(s[i]>s[i+1]) { pos=i;break;} //56781 56779   ....10  ....09
		while(pos+1<n&&pos>=0&&s[pos]>s[pos+1]) {
			s[pos]--;
			pos--;
		}
		for(int i=pos+2;i<n;i++) s[i]='9';
		pos=n;
		for(int i=0;i<n;i++)
			if(s[i]!='0') { pos=i;break;}
		printf("Case #%d: ",t);
		if(pos<n) printf("%s\n",s+pos);
		else printf("%d\n",0);
	}
}