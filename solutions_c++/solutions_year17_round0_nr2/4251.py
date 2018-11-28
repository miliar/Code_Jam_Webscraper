#include <bits/stdc++.h>
using namespace std;
char str[25];
int len;
long long dp[20][11][2];
long long powten[20];

long long f(int pos, int last, int isChoto){
    if(pos<0) return 0;
    if(dp[pos][last][isChoto]!=-1) return dp[pos][last][isChoto];
    long long res=-1000000000000000000LL;
    int low=last, high=9;
    if(!isChoto) high=str[len-1-pos]-'0';
    for(int i=low; i<=high; i++){
        res=max(res, i*powten[pos]+f(pos-1, i, isChoto || (i<high)));
    }
    return dp[pos][last][isChoto]=res;
}

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    powten[0]=1;
    for(int i=1; i<19; i++){
        powten[i]=10*powten[i-1];
    }
    int t, cs=0;
    scanf("%d", &t);
    while(t--){
        scanf("%s", str);
        len=strlen(str);
        memset(dp, -1, sizeof(dp));
        printf("Case #%d: %lld\n", ++cs, f(len-1, 0, 0));
    }
    return 0;
}
