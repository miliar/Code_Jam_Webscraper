#include<bits/stdc++.h>

#define INF 9223372036854775807
#define mod 1000000007
#define ll  long long int
#define ld double
#define endl '\n'
#define sz 2002
#define fast() ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0)

using namespace std;

string str;
ll n,arr[sz],parity[sz],final[sz],k;

bool check(){
    for(ll i = 1; i <= n; i++){
        if(final[i] == 0)
            return false;
    }
    return true;
}

int main(){
    ll t,i,j,ans,cnt;
    fast();
    cin>>t;
    for(ll test = 1; test <= t; test++){
        cin>>str>>k;
        n = str.size();
        memset(arr,0, sizeof(arr));
        memset(parity,0, sizeof(parity));
        memset(final,0,sizeof(final));
        ans = cnt = 0;
        for(i = 0; i <n ;i++){
            if(str[i] == '+')
                arr[i+1] = 1;
            else
                arr[i+1] = 0;
        }
        for(i = n; i >= k;i--){
            ans = (ans ^ parity[i]);
            if((arr[i]^ans) == 0){
                cnt++;
                ans = (ans^1);
                parity[i-k] = 1;
            }
            final[i] = (ans^arr[i]);
        }
        for(i = k-1; i > 0; i--){
        	ans = (ans^parity[i]);
            final[i] = (ans^arr[i]);
        }
        cout<<"Case #"<<test<<": ";
        if(check())
            cout<<cnt<<endl;
        else
            cout<<"IMPOSSIBLE"<<endl;
    }
    return 0;
}
