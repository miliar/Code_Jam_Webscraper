#include<cstdio>
#include<queue>
using namespace std;

int main(){
    int T;
    scanf(" %d ", &T);
    for(int t=1; t<=T; ++t){
	long long N, K;
	scanf(" %lld %lld ", &N, &K);
	long long ns = 1;
	long long large = N;
	long long nlarge = 1;
	long long small = -1;
	long long nsmall = 0;
	while(ns < K){
	    K -= ns;
	    long long t1;
	    long long nt1;
	    long long t2 = -1;
	    long long nt2 = 0;
	    if(large % 2 == 1){
		t1 = (large-1) / 2;
		nt1 = nlarge*2;
	    }else{
		t1 = large / 2;
		nt1 = nlarge;
		t2 = large / 2 - 1;
		nt2 = nlarge;
	    }
	    if(small != -1){
		if(small % 2 == 1){
		    if((small-1)/2 == t1){
			nt1 += (nsmall*2);
		    }else{
			t2 = (small-1) / 2;
			nt2 += (nsmall*2);
		    }
		}else{
		    nt1 += nsmall;
		    nt2 += nsmall;
		    if(small/2 == t1){
			t2 = small / 2 - 1;
		    }else{
			t2 = small / 2;
		    }
		}
	    }
	    if(t1 > t2){
		large = t1;
		nlarge = nt1;
		small = t2;
		nsmall = nt2;
	    }else{
		large = t2;
		nlarge = nt2;
		small = t1;
		nsmall = nt1;
	    }
	    if(large == 0) nlarge = 0;
	    if(small == 0) nsmall = 0;
	    ns = nlarge + nsmall;
	}
	long long m = (nlarge >= K ? large : small);
	if(m % 2 == 1){
	    printf("Case #%d: %d %d\n", t, m/2, m/2);
	}else{
	    printf("Case #%d: %d %d\n", t, m/2, m/2-1);
	}
    }
    return 0;
}
