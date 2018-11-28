#include <cstdio>

int T;
long long N,rem;
int qst,qls;
long long len[1999999];
long long num[1999999];
void add(long long addlen,long long addnum) {
	for(int i=qst;i<qls;i++) if(addlen==len[i]) {
		num[i]+=addnum;
		return;
	}
	len[qls]=addlen;
	num[qls++]=addnum;
}
int main() {
	scanf("%d",&T);
	for(int cases=1;cases<=T;cases++) {
		scanf("%lld%lld",&N,&rem);
		qst=0; qls=0;
		add(N,1);
		while(1) {
			if(rem>num[qst]) {
				rem-=num[qst];
				if(len[qst]/2) add(len[qst]/2,num[qst]);
				if((len[qst]-1)/2) add((len[qst]-1)/2,num[qst]);
				qst++;
			} else {
				printf("Case #%d: %lld %lld\n",cases,len[qst]/2,(len[qst]-1)/2);
				break;
			}
		}
	}
	return 0;
}
