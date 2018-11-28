#include <bits/stdc++.h>
using namespace std;
#define D(x) cerr<<#x " = "<<(x)<<endl
#define pb push_back
#define ff first
#define ss second
#define mem(a) memset(a,0,sizeof(a))
#define _set(a) memset(a,-1,sizeof(a))
typedef long long int ll;
typedef unsigned long long ull;
typedef pair<int,int> pii;
#define eps 1e-9
#define MAX 100000
#define MAXL 20
#define MAXE 100000
#define inf (1<<30)
//ll mod = 1000000000+7;
//int dx[] = {0,0,1,-1};
//int dy[] = {1,-1,0,0};
//int dx[] = {-1,-1,-1,0,0,1,1,1};
//int dy[] = {-1,0,1,-1,1,-1,0,1};

int digit[20];
int main() {
    freopen("B-large.in", "r", stdin);
    freopen("output.out", "w", stdout);
    //ios_base::sync_with_stdio(false);
    int ncase, tcase = 1;
    ll n;
    scanf("%d", &ncase);
    while(ncase--) {
        scanf("%lld", &n);
        int d = 0;
        ll tmp = n;
        while(tmp) {
            digit[d] = tmp%10;
            d++;
            tmp /= 10;
        }
        reverse(digit, digit+d);
        ll ans = 0;
        ll num = 0;
        if(d == 1) {
            printf("Case #%d: %lld\n", tcase++, n);
            continue;
        }
        int i, j;
        for(i = 0; i < d; i++) {
            if(i > 0) {
                num = num*10+digit[i-1];
                if(digit[i] < digit[i-1]) break;
            }
            if(digit[i] <= digit[i-1]) continue;
            tmp = num*10 + digit[i]-1;
            for(j = i+1; j < d; j++) {
                tmp = tmp*10 + 9;
            }
            ans = max(ans, tmp);
        }
        if(i == d) {
            num = num*10 + digit[i-1];
            ans = max(ans, num);
        }
        printf("Case #%d: %lld\n", tcase++, ans);
    }
    return 0;
}


