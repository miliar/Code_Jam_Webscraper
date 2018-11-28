#include <stdio.h>
long long ds[10];
long long dsk[10];
int sz;
void ins(long long K, long long V){
    int i = 0;
    bool incs = true;
    while (i < sz){
		if (ds[i] == K){
			dsk[i] += V;
			incs = false;
			break;
		}
		i++;
	}
	if (incs){
		ds[sz] = K;
		dsk[sz] = V;
		i = 1;
		sz++;
		long long ek;
		long long ev;
		while (i < sz){
			if (ds[i] > ds[0]){
				ek = ds[i];
				ev = dsk[i];
				ds[i] = ds[0];
				dsk[i] = dsk[0];
				ds[0] = ek;
				dsk[0] = ev;
			}
			i++;
		}
	}
}
void pop(){
    ds[0] = ds[sz-1];
    dsk[0] = dsk[sz-1];
    sz = sz-1;
}
int main(){
	freopen("C-large.in","r",stdin);
    freopen("C-large.out","w",stdout);
	int T;
	scanf("%d", &T);
	long long N;
	long long K;
	long long Ans = 0;
	long long Ansk = 0;
	int i = 0;
	while (i < T){
		sz = 0;
		scanf("%lld %lld", &N, &K);
		ins(N, 1);
		while (K > 0){
			Ans = ds[0];
			Ansk = dsk[0];
			K -= dsk[0];
			if ((Ans-1)%2 == 0){
				pop();
				ins((Ans-1)/2, 2*Ansk);
			}
			else{
				pop();
				ins((Ans-1)/2, Ansk);
				ins((Ans-1)/2+1, Ansk);
			}
		}
		if ((Ans-1)%2 == 0){
			printf("Case #%d: %lld %lld\n", i+1, (Ans-1)/2, (Ans-1)/2);
		}
		else{
			printf("Case #%d: %lld %lld\n", i+1, (Ans+1)/2, (Ans-1)/2);
		}
		i++;
	}
}
