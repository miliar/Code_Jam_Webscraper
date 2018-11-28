#include <stdio.h>
#include <string.h>
#include <algorithm>

using namespace std;

typedef long long lli;

lli d[2][10][20];
char s[20];
int l;

lli f(int hf, int pre, int k) {
	if(k==l) return 1;
	if(d[hf][pre][k]>=0) return d[hf][pre][k];
	lli res=0;
	for(int i=pre;i<=9;i++) {
		if(hf==0 && s[k]-'0'<i) continue;
		int nf=hf;
		if(s[k]-'0'>i) nf=1;
		res+=f(nf,i,k+1);
	}
	return d[hf][pre][k]=res;
}

lli cnt(lli n) {
	l=0;
	while(n) {
		s[l++]=n%10+'0';
		n/=10;
	}
	reverse(s,s+l);
	memset(d,-1,sizeof(d));
	return f(0,0,0);
}

int main() {
	FILE* in=fopen("B-large.in","rt");
	FILE* out=fopen("Bout.txt","wt");
	int t;
	fscanf(in,"%d",&t);
	for(int tc=1;tc<=t;tc++) {
		fprintf(out,"Case #%d: ",tc);
		lli n;
		fscanf(in,"%lld",&n);
		if(n==1) fprintf(out,"1\n");
		else {
			lli lo=1, hi=n;
			lli c=cnt(n);
			while(lo+1<hi) {
				lli mid=(lo+hi)/2;
				if(cnt(mid)!=c) lo=mid;
				else hi=mid;
			}
			fprintf(out,"%lld\n",hi);
		}
	}
	return 0;
}
