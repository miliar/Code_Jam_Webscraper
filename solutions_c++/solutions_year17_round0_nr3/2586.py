#include<iostream>
#include<cstring>
#include<algorithm>
#include<map>
#include<cstdio>
using namespace std;
#define f first
#define s second
#define lint long long
lint n,k;
void solve(){
    map < lint , lint > mp,tmp;
    map < lint , lint > :: reverse_iterator it;
    mp[n]=1;
    lint a,b;
    while(k){
        a=mp.rbegin()->f;
        b=mp.rbegin()->s;
        it=mp.rbegin();
        it++;
        tmp.clear();
        for(;it!=mp.rend();it++)
            tmp[it->f]=it->s;
        mp=tmp;
        if(b>=k){
            printf("%lld %lld\n",a/2,(a-1)/2);
            return;
        }
        k-=b;
        mp[a/2]+=b;
        mp[(a-1)/2]+=b;
    }
}
int main(){
    int t,i;
    freopen("C3.in","r",stdin);
    freopen("C3.out","w",stdout);
    cin>>t;
    for(i=1;i<=t;i++){
        cin>>n>>k;
        cout<<"Case #"<<i<<": ";
        solve();
    }
}

