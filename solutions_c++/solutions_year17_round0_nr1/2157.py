#include <bits/stdc++.h>
#define maxx 100005
#define inf 2000000000
#define mod 1000000007
#define pii pair<int,int>
#define piii pair<pii,pii>
#define pli pair<long long,int>
#define f first
#define s second
#define in(x) scanf("%d",&x)
#define IN(x) scanf("%lld",&x)
#define inch(x) scanf("%s",x)
#define indo(x) scanf("%lf",&x)
#define pb push_back

typedef long long ll;
typedef unsigned long long ull;

using namespace std;

int t, k, n;
int dp[1234];
char s[1234];
int main()
{
    freopen("input.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    in(t);
    for(int cases = 1; cases <= t; cases ++){
        inch(s); in(k);
        n = strlen(s);
        int ans = 0;
        bool IMPOSSIBLE = false;
        for(int i = 0; i <= n - k; i++){
            if(s[i] == '-'){
                for(int j = i; j < i + k; j++){
                    s[j] = (s[j] == '+' ? '-' : '+');
                }
                ans++;
            }
        }
        for(int i = n - k + 1; i < n; i++){
            if(s[i] == '-'){
                IMPOSSIBLE = true;
                break;
            }
        }
        printf("Case #%d: ",cases);
        if(IMPOSSIBLE){
            puts("IMPOSSIBLE");
        }else{
            printf("%d\n",ans);
        }
    }
    return 0;
}
