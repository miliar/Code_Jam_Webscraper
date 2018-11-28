#include <bits/stdc++.h>

using namespace std;
typedef long long ll;
int sz = 0;
string str;
int cntSz(ll n){
    int ans = 0;
    str = "";
    while(n){
        ans ++;
        str += '0' + (n%10);
        n/=10;
    }
    reverse(str.begin(),str.end());
    return ans;
}

ll my_pw(ll x , int p){
    if(p == 0)return 1;
    if(p&1)return x*my_pw(x,p-1);
    ll y = my_pw(x,p/2);
    return y*y;
}
ll mem[19][11][2];
ll solve(int idx , int lastDigit,int isEq){
    if(idx == sz){
        return 0;
    }
    if(isEq && lastDigit>(str[idx]-'0'))
        return -1e18;
    ll &ret = mem[idx][lastDigit][isEq];
    if(ret != -1){
        return ret;
    }
    ret = -1e18;
    if(isEq){
        int toDig = str[idx] - '0';
        for(int i = lastDigit ; i <= toDig ; i++){
            if(i < toDig){
                ret = max(ret , solve(idx+1,i,0)+ (i * my_pw(10,sz-idx-1)));
            }else ret = max(ret , solve(idx+1,i,1) + (i * my_pw(10,sz-idx-1)));
        }
    }else{
        for(int i = lastDigit;i<10 ; i++){
            ret = max(ret , solve(idx+1,i,0) + (i * my_pw(10,sz-idx-1)));
        }
    }
    return ret;
}

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("TidyLarge.txt","w",stdout);
    int t;
    scanf("%d",&t);
    for(int I = 1 ; I <= t ; I++){
        memset(mem,-1,sizeof mem);
        ll n;
        cin >> n;
        sz = cntSz(n);
        ll ans = solve(0,1,1);
        if(ans <= 0){
            printf("Case #%d: ",I);
            for(int i = 0 ; i < sz-1 ; i++){
                printf("9");
            }
            printf("\n");
        }else {
            printf("Case #%d: ",I);
            cout << ans << "\n";
        }
    }
    return 0;
}
/*
6
132
1000
7
111111111111111110
929
1000000000000000000
*/

