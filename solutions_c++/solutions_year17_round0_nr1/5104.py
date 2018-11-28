#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cassert>
#include<ctime>
#include<cmath>

#include<algorithm>
#include<bitset>
#include<complex>
#include<deque>
#include<iostream>
#include<map>
#include<numeric>
#include<queue>
#include<stack>
#include<string>
#include<set>
#include<vector>
using namespace std;

int dp[3000];
char str[3000];

int main(int argc, const char *argv[])
{
    int tn;
    int len, k;
    int cnt, ans;
    bool ac;

    cin >> tn;
    for (int z = 1; z <= tn; z++) {

        cin >> str >> k;

        /* Init */
        ans = 0;
        cnt = 0;
        ac = true;
        len = strlen(str);
        memset(dp, 0, sizeof(dp));

        for (int i = 0; i < len && ac; i++) {
            int state_i = (str[i] == '+');
            cnt -= dp[i];
            /* printf("i %d: statei %d cnt %d\n", i, state_i, cnt); */
            if((state_i ^ (cnt % 2)) == 0){
                if(i + k <= len){
                    ans++;
                    cnt++;
                    dp[i+k]++;
                }else
                    ac = false;
            }
        }
        printf("Case #%d: ", z);
        if(!ac) puts("IMPOSSIBLE");
        else printf("%d\n", ans);
    }
    return 0;
}
