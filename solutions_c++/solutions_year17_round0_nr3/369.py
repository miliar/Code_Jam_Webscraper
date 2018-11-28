#include <bits/stdc++.h>
#include <unordered_map>

using namespace std;

typedef long long ll;

ll halfceil(ll n){
    if(n%2==0)return n/2;
    return 1+n/2;
}

int main(){
    freopen("hi.txt","r",stdin);
    freopen("hi2.txt","w",stdout);
    int tc;
    scanf("%d",&tc);
    char str[1010];
    for(int t=1;t<=tc;t++){
        ll n,k;
        scanf("%lld%lld",&n,&k);
        //1+2+4+...+? <n
        //?*2 <n+1
        int p=0;
        for(int i=20;i>=0;i--){
            if((k>>i)==1){
                p=i;
                break;
            }
        }
        p--;
        ll people=(1LL<<(p+1))-1;
        //printf("people=%lld\n",people);
        ll small,numsmall,numbig;
        small=(n-people)/(people+1);
        numbig=n-people-small*(people+1);
        numsmall=people+1-numbig;
        //printf("%lld %lld %lld\n",small,numbig,numsmall);
        ll remaining=k-people;
        //printf("rem=%lld\n",remaining);
        printf("Case #%d: ",t);
        if(remaining<=numbig){
            printf("%lld %lld\n",halfceil(small),small/2);
        }
        else{
            printf("%lld %lld\n",halfceil(small-1),(small-1)/2);
        }
    }
    return 0;
}
