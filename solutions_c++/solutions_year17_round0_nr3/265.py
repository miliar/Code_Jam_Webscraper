#include <stdio.h>

long long Work(long long len, long long N){
	long long ct=0; //counter udah berapa orang masuk 
	long long n0=1, n1=0; //ada n0 gap sebesar len, ada n1 gap sebesar len+1
	
	//simulasi
	while(true){
		long long tlen = (len-1) / 2; //temp var panjang gap baru
		long long tn0 = 0, tn1 = 0; //temp var banyaknya gap baru (tn0 gap sebesar tlen, tn1 gap sebesar tlen+1)
		
		ct += n1;
		if(len % 2 == 0){
			tn1 += 2*n1;
		}
		else{
			tn1 += n1;
			tn0 += n1;
		}
		if(ct >= N){
			return len+1;
		}
		
		ct += n0;
		if(len % 2 == 1){
			tn0 += 2*n0;
		}
		else{
			tn0 += n0;
			tn1 += n0;
		}
		if(ct >= N){
			return len;
		}
		
		len = tlen;
		n0 = tn0;
		n1 = tn1;
	}
}

int main(){
	int jcase;
	long long L, N;
	
	freopen("C-large.in", "r", stdin);
	//freopen("C-large.out", "w", stdout);
	
	scanf("%d", &jcase);
	for(int icase=0; icase<jcase; icase++){
		scanf("%lld %lld", &L, &N);
		long long ans = Work(L, N);
		long long ans1 = ans / 2;
		long long ans2 = ans - ans1 - 1;
		printf("Case #%d: %lld %lld\n", icase+1, ans1, ans2);
	}
	return 0;
}
