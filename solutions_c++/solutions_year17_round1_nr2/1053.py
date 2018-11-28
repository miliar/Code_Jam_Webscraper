#include <cstdio>
#include <cstdlib>

int T,N,P;
int Rs[99];
int minv[99][99];
int maxv[99][99];
int list[99][99];
int list_size[99];
typedef struct {
	int tm;
	int tp;
	int dg;
	int pk;
}events;
events event[2999];
int cmp(const void *ka,const void *kb) {
	events *a=(events *)ka;
	events *b=(events *)kb;
	if(a->tm!=b->tm) return a->tm-b->tm;
	if(a->tp!=b->tp) return a->tp-b->tp;
	return a->dg-b->dg;
}
void del(int dg,int pk) {
	for(int i=0;i<list_size[dg];i++) {
		if(list[dg][i]==pk) {
			list[dg][i]=list[dg][list_size[dg]-1];
			list_size[dg]--;
		}
	}
}
void add(int dg,int pk) {
	list[dg][list_size[dg]++]=pk;
}
void gen_kit(void) {
	for(int i=0;i<N;i++) {
		int next=list[i][0];
		for(int j=1;j<list_size[i];j++) {
			if(maxv[i][next]>maxv[i][list[i][j]]) next=list[i][j];
		}
		del(i,next);
	}
}

int main() {
	scanf("%d",&T);
	for(int cases=1;cases<=T;cases++) {
		scanf("%d%d",&N,&P);
		for(int i=0;i<N;i++) scanf("%d",&Rs[i]);
		int eveall=0;
		for(int i=0;i<N;i++) for(int j=0;j<P;j++)  {
			int Q;
			scanf("%d",&Q);
			Q*=10;
			int min_unit=Rs[i]*9;
			int max_unit=Rs[i]*11;
			minv[i][j]=Q/max_unit;
			if(Q%max_unit) minv[i][j]++;
			maxv[i][j]=Q/min_unit;
			if(minv[i][j]<=maxv[i][j]) {
				event[eveall].tm=minv[i][j];
				event[eveall].tp=1;
				event[eveall].dg=i;
				event[eveall++].pk=j;
				event[eveall].tm=maxv[i][j]+1;
				event[eveall].tp=0;
				event[eveall].dg=i;
				event[eveall++].pk=j;
			}
		}
		qsort(event,eveall,sizeof(events),cmp);
		int sol=0;
		for(int i=0;i<N;i++) list_size[i]=0;
		for(int ev=0;ev<eveall;ev++) {
			if(event[ev].tp==0) {
				del(event[ev].dg,event[ev].pk);
			} else {
				add(event[ev].dg,event[ev].pk);
				int ok=1;
				for(int i=0;i<N;i++) if(list_size[i]==0) ok=0;
				if(ok) {
					sol++;
					gen_kit();
				}
				
			}
		}
		printf("Case #%d: %d\n",cases,sol);
	}
	return 0;
}
