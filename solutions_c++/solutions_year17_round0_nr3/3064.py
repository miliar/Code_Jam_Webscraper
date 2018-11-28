#include <bits/stdc++.h>
#define LL long long int

using namespace std;

const int INF = 0x7FFFFFFF;

void
Filework(void){
	freopen("clarge.in", "r", stdin);
	freopen("clarge.out", "w", stdout);
}

LL n, k;
LL dn, dk;
LL a[105];

void
make_chart(){
    int i;
    a[0] = 1;
    for(i = 1; i <= INF; i ++){
        a[i] = a[i - 1] * 2;
        if(a[i] > (1e18) / 2)
            break;
    }
}

int
main(){

	Filework();

	int T;
	int t;
	int i, j;
	LL sum, space;

    make_chart();

	scanf("%d", &T);
	for(t = 1; t <= T; t ++){
        scanf("%lld%lld", &n, &k);
        dn = n;
        dk = k;
        sum = 0;
        space = 0;
        for(i = 0; i <= k; i ++){
            sum += a[i];
            if(sum >= dk){
                break;
            }
        }
        sum -= a[i];
        dk -= sum;
        dn -= sum;
        if((dn - a[i]) % a[i] >= dk){
            space = (dn - a[i]) / a[i] + 1;
        }
        else{
            space = (dn - a[i]) / a[i];
        }
        printf("Case #%d: ", t);
        printf("%lld %lld\n", max(space - space / 2, space / 2), min(space - space / 2, space / 2));
	}

return 0;
}
