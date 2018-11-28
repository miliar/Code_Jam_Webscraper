/*************************************************************************
	> File Name: C.cpp
	> Author: tyxxzjpdez
	> Mail: tyxxzjpdez@163.com
	> Created Time: 2017年04月08日 星期六 13时14分34秒
 ************************************************************************/

#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef pair<ll,ll> pii;
ll n,k;

ll Ceil(ll a,ll b){
    return a%b==0?a/b:a/b+1;
}
void upd(pii &a,pii &b){
    ll num1=a.first,num2=b.first;
    ll t[2];
    t[0]=a.second,t[1]=b.second;
    ll vis[5];
    ll sum1=t[0],sum2=0,k=-1;
    vis[0]=(num1-1)/2;vis[1]=Ceil(num1-1,2);
    vis[2]=(num2-1)/2;vis[3]=Ceil(num2-1,2);
    if(num1==num2 && (num1&1)){
        a=make_pair(vis[0],t[0]*2);
        b=make_pair(vis[2],t[1]*2);
        return;
    }
    for(int i=1;i<4;i++){
        if(vis[i]==vis[0])
            sum1+=t[i/2];
        else sum2+=t[i/2],k=i;
    }
    a=make_pair(vis[0],sum1);
    b=make_pair(vis[k],sum2);
}

ll cal(ll x){
    ll tot=0;
    while(x){
        x>>=1;
        tot++;
    }
    return tot;
}
int main(){
    //ios::sync_with_stdio(false);
    freopen("C.in","r",stdin);
    freopen("C.out","w",stdout);
    int T;scanf("%d",&T);
    for(int kase=1;kase<=T;kase++){
        cin>>n>>k;ll ans;
        if(k>1){
            ll len=cal(k);
            ll sta=1,tmp=len-2,rank=1;
            pii b=make_pair(Ceil(n-1,2),1),a=make_pair((n-1)/2,1);
            while(sta<k){
                if((k>>tmp)==(sta<<1))
                    sta<<=1,rank=rank*2-1;
                else sta=(sta<<1|1),rank<<=1;
                if(tmp!=len-2)upd(a,b);
                tmp--;
            }
            ans=(rank>b.second)?a.first:b.first;
        }else ans=n;
        cout<<"Case #"<<kase<<": ";
        cout<<Ceil(ans-1,2)<<" "<<(ans-1)/2<<endl;
    }
    return 0;
}
