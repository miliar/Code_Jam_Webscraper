#include <iostream>
#include <cstdio>
#include <map>
#define ll long long

using namespace std;

int T;
ll N,K;

int main(){
    freopen("data3.in","r",stdin);
    freopen("data3.out","w",stdout);
    scanf("%d",&T);
    for (int z = 1; z <= T; z++){
        scanf("%lld%lld",&N,&K);
        map<ll,ll> cnt;
        cnt[N] = 1;
        while(K){
            auto it = cnt.end(); it--;
            if (it->second >= K){
                printf("Case #%d: %lld %lld\n",z,it->first/2,(it->first%2)?it->first/2:it->first/2-1);
                break;
            }
            if (it->first%2) cnt[it->first/2] += it->second*2;
            else{
                cnt[it->first/2] += it->second;
                cnt[it->first/2-1] += it->second;
            }
            K -= it->second;
            cnt.erase(it);
        }
    }
    return 0;
}
