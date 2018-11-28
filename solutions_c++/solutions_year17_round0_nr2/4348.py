#include<cstdio>
#include<cstring>
using namespace std;

typedef long long ll;

int T, cas, len;
int digit[20];
ll n, fac[20];

ll f(int pre, bool istop, int len) {
    if (len == 0) return 0;
    for (int i = istop? digit[len-1]: 9; i >= pre; i--){
        ll temp = f(i, istop&&i==digit[len-1], len-1);
        if (temp >= 0) return fac[len-1] * i + temp;
    }
    return -1;
}

int main()
{
    fac[0] = 1;
    for (int i = 1; i < 19; i++)
        fac[i] = fac[i-1] * 10;
    scanf("%d", &T);
    while(T--){
        scanf("%lld", &n);
        len = 0;
        while(n){
            digit[len++] = n % 10;
            n = n / 10;
        }
        printf("Case #%d: %lld\n", ++cas, f(0, true, len));
    }
    return 0;
}
