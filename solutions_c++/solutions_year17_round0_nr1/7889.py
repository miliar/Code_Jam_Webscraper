#include <iostream>
#include <bits/stdc++.h>
#include <string>

#define ll long long int

using namespace std;

ll flips(string a,ll M,ll N,ll want){
    ll s[100005],i;
    for(i=0;i<M;i++)
        s[i]=0;
    ll sum=0,ans=0;
    for(i=0;i<M;i++){
        ll temp;
        if(a.at(i)=='+'){
            temp=1;
        }
        else{
            temp=0;
        }
        s[i]=(temp+sum)%2 != want;
        sum += s[i] - (i>=N-1?s[i-N+1]:0);
        ans += s[i];
        if(i>M-N and s[i]!=0) return -1;
    }
    return ans;
}

int main(){
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    ll t,k,i;
    string s;
    cin>>t;
    for(i=1;i<=t;i++){
        cin>>s;
        cin>>k;
        ll n=s.size();
       ll ans=flips(s,n,k,1);
        if(ans==-1){
            cout<<"Case #"<<i<<": "<<"IMPOSSIBLE"<<endl;
        }
        else{
            cout<<"Case #"<<i<<": "<<ans<<endl;
        }
    }
    return 0;
}
