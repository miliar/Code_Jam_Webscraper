/**
Author:  ShivamRathore (Shivam010)
**/
#include <bits/stdc++.h>
using namespace std;
#define ll long long

int main(){
    int T;
    cin>>T;
    for(int t=1;t<=T;t++){
        ll n,k;
        cin>>n>>k;
        string ans = "Case #";
        cout<<ans<<t<<": ";
        priority_queue<ll> a;
        a.push(n);
        ll v,x,y;
        for(ll i=0;i<k;i++){
            v=a.top();
            a.pop();
            x=v/2;
            if(v&1) y=x;
            else    y=x-1;
            a.push(x);
            a.push(y);
        }
        cout<<x<<" "<<y<<endl;
    }
    return 0;
}
