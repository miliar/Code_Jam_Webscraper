#include<stdio.h>
#include<map>
#include<queue>

using namespace std;

typedef long long int lli;

int main(){
    freopen("C-large.in","r",stdin);
    freopen("C-large.out","w",stdout);
    int t;
    lli n,k,s;
    scanf("%d",&t);
    for(int c=1; c<=t; c++){
        scanf("%lld %lld",&n,&k);
        k--;
        priority_queue<lli> cola;
        map<lli, lli> cant;
        cola.push(n/2LL);
        cola.push((n-1LL)/2LL);
        cant[n/2LL] = 1LL;
        cant[(n-1LL)/2LL] = 1LL;
        s = 0LL;
        lli e = n;
        while(s<k){
                e = cola.top();
                s+=cant[e];
                cola.pop();
                lli l1=e/2LL,l2=(e-1LL)/2LL;
                if(cant[l1]>0LL) cant[l1]+=cant[e];
                else{
                    cola.push(l1);
                    cant[l1] = cant[e];
                }
                if(cant[l2]>0LL) cant[l2]+=cant[e];
                else{
                    cola.push(l2);
                    cant[l2] = cant[e];
                }

        }
        printf("Case #%d: %lld %lld\n",c,e/2LL,(e-1LL)/2LL);
    }
    return 0;
}
