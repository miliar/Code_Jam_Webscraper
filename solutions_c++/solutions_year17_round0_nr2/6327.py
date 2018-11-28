#include <map>
#include <set>
#include <stack>
#include <cmath>
#include <queue>
#include <string>
#include <vector>
#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;
#define FOR(i, j, k) for(int i = j;i<= k;i++)
#define ll long long
const int maxn  =50;

//ll dp[maxn][5];//flag 0 表示不含49前位不是4，1表示不含49前位是4，2表示含49
int digit[maxn];
int ans[maxn];
int len;
void cal(ll n)
{
    memset(digit,0,sizeof(digit));
    len = 0;
    while(n)
    {
        len++;
        digit[len] = n%10;
        n /=10;
    }
//    cout<<len<<endl;
//    FOR(i, 1, len) cout<<digit[i]<<" ";
    //return  dfs(len ,0 ,1 );
}
int main(){
    freopen("/Users/hermione/Desktop/in.txt","r",stdin);
    freopen("/Users/hermione/Desktop/temp.txt", "w", stdout);
    int T;
    cin>>T;
    FOR(z, 1, T){
        ll x;
        scanf("%lld", & x);
        cal(x);
        int t = 0;
        FOR(i, 2, len)
        {
            if(digit[i] > digit[i-1]){
                t = i -1;
                digit[i] --;
            }
        }
        FOR(i, 1, t) digit[i] = 9;
        printf("Case #%d: ",z);
        int flag = 0;
        for(int i = len; i>=1 ;i--){
            if(digit[i] == 0 && flag == 0)
                continue;
            if(digit[i] != 0) flag =1;
            printf("%d",digit[i]);
        }
        printf("\n");
    }
    return 0;
}