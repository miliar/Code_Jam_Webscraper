#include<stdio.h>

long long tlen(long long n, long long k) {
    if(k==1)return n;
    if( (n-1)%2 == 0){
        if( (k-1)%2 == 0)return tlen((n-1)/2, (k-1)/2);
        else return tlen((n-1)/2, (k-1)/2+1 );
    }
    else {
        if( (k-1)%2 == 1)return tlen( (n-1)/2+1, (k-1)/2+1 );
        else return tlen( (n-1)/2, (k-1)/2);
    }
}


int main()
{
    int T, cases;
	long long N, K;
	freopen("c.in", "r", stdin);
    freopen("c.out", "w", stdout);
	scanf("%d", &T);
	for(cases=1; cases<=T; cases++) {
	    scanf("%I64d%I64d", &N, &K);
	    long long tt = tlen(N, K);
	    printf("Case #%d: %I64d %I64d\n", cases, tt/2, (tt-1)/2);
	}

    return 0;
}
