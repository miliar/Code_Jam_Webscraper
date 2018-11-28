#include<bits/stdc++.h>
using namespace std;
typedef long long ll;

int main(){
    freopen("in2.txt","r",stdin);
    freopen("out.txt","w",stdout);
    ll t;
    scanf("%lld",&t);
    for(ll tt = 1;tt <= t;tt++){
        ll n,k;
        scanf("%lld %lld",&n,&k);
        ll min1,max1;
        while(true){
            if(k == 1 || k == n){
                if(k == n){
                    min1 = max1 = 0;
                }else{
                    if(n%2){
                        min1 = max1 = n/2;
                    }else{
                        min1 = n/2 - 1;
                        max1 = n/2;
                    }
                }
                break;
            }
            if(n%2){
                k--;
                if(k%2){
                    n = n/2;
                    k = k/2 + 1;
                }else{
                    n = n/2;
                    k = k/2;
                }
            }else{
                k--;
                if(k%2){
                    k = k/2 + 1;
                    n = n/2;
                }else{
                    k = k/2;
                    n = n/2 - 1;
                }
            }
        }
        cout << "Case " << "#" << tt << ": " << max1 << " " << min1 << "\n";
    }
}
