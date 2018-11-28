#include <iostream>
#include <string>
#include <queue>
#include <stdio.h>
using namespace std;
typedef long long ll;
int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int t;
    cin>>t;
    for(int j=1;j<=t;j++){
        ll n,mx=1;
        scanf("%lld",&n);
        queue<ll>q;
        for(int i=1;i<=9;i++)
            if(i<=n){
                q.push(i);
                if(i>mx)mx=i;
            }
        while(!q.empty()){
            ll x=q.front();
            q.pop();
            for(int i=x%10;i<=9;i++)
                if(x*10+i<=n&&x*10+i>0){
                    q.push(x*10+i);
                    if(mx<x*10+i)mx=x*10+i;
                }
        }
        printf("Case #%d: %lld\n",j,mx);
    }
    return 0;
}
