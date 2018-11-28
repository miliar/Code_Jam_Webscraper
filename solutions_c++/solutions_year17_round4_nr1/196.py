#include<bits/stdc++.h>
using namespace std;
string str;
int n , Tn , T , K;
int cnt[10];
int dp[101][101][101];
int calc(int one , int two , int three){
    if(one + two + three == 0) return 0;
    int token =  (cnt[1] - one) + 2 * (cnt[2] - two) + 3 * (cnt[3] - three);
    token %= K;
    token = (K - token)%K;
    int &ret = dp[one][two][three]; if(ret != -1) return ret;
    ret = 0;
    if(one)
        ret = max(ret , calc(one - 1 , two , three));
    if(two)
        ret = max(ret , calc(one  , two - 1 , three));
    if(three)
        ret = max(ret , calc(one  , two  , three - 1));
    if(token == 0) ++ret;
    return ret;
}
int main(){
    freopen("in.in","r",stdin);
    freopen("out.out","w",stdout);
    cin>>T;
    while(T--){
        printf("Case #%d: ",++Tn);
        memset(dp , -1 , sizeof(dp));
        memset(cnt , 0 , sizeof(cnt));
        cin>>n>>K;
        int ans = 0;
        while(n--){
            int x;
            cin>>x;
            if(x % K == 0) ++ans;
            else ++cnt[x%K];
        }
        cout<<ans + calc(cnt[1] , cnt[2] , cnt[3])<<endl;
    }
}

