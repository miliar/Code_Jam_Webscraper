#include<stdio.h>

unsigned long long int ans(unsigned long long int n) {
    unsigned long long int d = 1;
    while(1){
        if(d*10>n)break;
        if( n/d%10 < n/(d*10)%10){
            return ans((n/(d*10)-1)*(d*10) + (d*10-1));
        }
        d*=10;
    }
    return n;
}


int main()
{
    int T, cases;
	unsigned long long int N;
	freopen("b.in", "r", stdin);
    freopen("b.out", "w", stdout);
	scanf("%d", &T);
	for(cases=1; cases<=T; cases++) {
	    scanf("%I64u", &N);
	    printf("Case #%d: %I64u\n", cases, ans(N));
	}

    return 0;
}
