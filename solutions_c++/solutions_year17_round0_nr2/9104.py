

#include<bits/stdc++.h>


using namespace std;
typedef long long ll;
const int L = 19;
int num[L+2];
ll p10[L+2];
ll dp[L][L][3];
ll calc(int i,int p,int f){
    if(i == L) return 0;
    ll&ret = dp[i][p][f];
    if(ret!=-1) return ret;
    ret = -2;
    for(int d = p; d <= (f ? num[i] : 9); d++){
        ll nxt = calc(i+1,d,f&&(d==num[i]));
        if(nxt == -2) continue;
        ret = max(ret,d*p10[i]+nxt);
    }
//    cout<<i<<" "<<p<<" "<<f<<" = " <<ret<<endl;
    return ret;
}

void solve(int tc){

    ll n;
    cin>>n;
    ll ten = 1;
    for(int i = 0 ; i < L ; i++){
        num[i] = n%10ll;
        n/=10;
        p10[i] = ten;
        ten *= 10ll;
    }
    memset(dp,-1,sizeof dp);
    reverse(num,num+L);
    reverse(p10,p10+L);
    ll ans = calc(0,0,1);
    cout<<"Case #"<< tc <<": ";
    cout<<ans<<endl;
}

int main(){

        int t;
    cin>>t;
    int tc = 1;
    while(t--) solve(tc++);



    return 0;
}



/*

1
110


*/
