#include <stdio.h>
#include <queue>
#include <map>
#include <iostream>
#include <algorithm>
using namespace std;
typedef long long ll;

void process(){
    ll n,k;
    priority_queue<ll> pq;
    map<ll,ll> mp;
    scanf("%lld %lld\n",&n,&k);
    ll mini = n, maxi = n;
    pq.push(n);
    mp[n] = 1;
    while(k>0){
        ll top = pq.top();
        k -= mp[top];
        pq.pop();
        ll q = top;
        top--;
        if(mp[top/2]==0&&(top/2)!=0) pq.push(top/2);
        if(mp[(top+1)/2]==0&&((top+1)/2)!=0) pq.push((top+1)/2);
        mp[top/2] += mp[q];
        mp[(top+1)/2] += mp[q];
        mini = min(mini,top/2);
        maxi = min(maxi,(top+1)/2);
        mp[q] = 0;
        if(pq.empty()){
            mini = maxi = 0;
            break;
        }
    }
    printf("%lld %lld",maxi,mini);
}


int main(){
    int t;
    //freopen("C.in","rt",stdin);
    //freopen("C.txt","wt",stdout);
    scanf("%d",&t);
    for(int i = 1 ; i <= t ; i++){
        printf("Case #%d: ",i);
        process();
        puts("");
    }
}
