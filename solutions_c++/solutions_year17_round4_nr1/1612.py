#include <bits/stdc++.h>
#define maxx 100005
#define inf 2000000000
#define mod 1000000007
#define pii pair<int,int>
#define piii pair<pii,pii>
#define pli pair<long long,int>
#define pll pair<long long,long long>
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

int t, n, p;
int g[maxx], cnt[5];
int main()
{
    freopen("input.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    in(t);
    for(int cases = 1; cases <= t; cases ++){
        in(n); in(p);
        memset(cnt, 0, sizeof(cnt));
        for(int i = 1; i <= n; i++){
            in(g[i]);
            cnt[g[i] % p]++;
        }
        int ans = 0;
        if(p == 2){
            ans = ans + cnt[0] + (cnt[1] + 1) / 2;
        }else if(p == 3){
            ans = ans + cnt[0] + min(cnt[1], cnt[2]) + ((max(cnt[1], cnt[2]) - min(cnt[1], cnt[2])) + 2) / 3;
        }else{
            ans = ans + cnt[0];
            int best = 0;
            int say[6];
            for(int i = 0; i <= n / 2; i++){
                for(int j = 0; j <= n / 2; j++){
                    for(int k = 0; k <= n / 3; k++){
                        for(int l = 0; l <= n / 4; l++){
                            say[1] = say[2] = say[3] = say[4] = 0;
                            say[1] += i;
                            say[3] += i;
                            say[2] += (j + j);
                            say[2] += k;
                            say[4] += (k + k);
                            say[4] += (l + l + l + l);
                            if(say[1] <= cnt[1] && say[2] <= cnt[2] && say[3] <= cnt[3] && (say[1] + say[3] + say[4]) <= cnt[1] + cnt[3]){
                                if(say[1] + say[2] + say[3] < cnt[1] + cnt[2] + cnt[3]){
                                    best = max(best, i + j + k + l + 1);
                                }else{
                                    best = max(best, i + j + k + l);
                                }
                            }
                        }
                    }
                }
            }
            ans = ans + best;
        }
        printf("Case #%d: ",cases);
        printf("%d\n",ans);
    }
    return 0;
}
