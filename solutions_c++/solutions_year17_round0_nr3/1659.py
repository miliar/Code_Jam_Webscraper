/* -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
 * Created By : Aditya Agarwal
 * IT, MNNIT-ALLAHABAD 
 * aditya.mnnit15@gmail.com
 _._._._._._._._._._._._._._._._._._._._._.*/


#include<bits/stdc++.h>
using namespace std;

#define MP make_pair
#define pb push_back
#define rep(i,n) for(int i=0;i<n;i++)
#define REP(i,a,b) for(int i=a;i<=b;i++)
#define PER(i,a,b) for(int i=b;i>=a;i--)
#define X first
#define Y second

 //i/o
#define inp(n) scanf("%d",&n)
#define inpl(n) scanf("%lld",&n)
#define inp2(n,m) inp(n), inp(m)
#define inp2l(n,m) inpl(n), inpl(m)


//cost
#define MOD 1000000007
#define MOD_INV 1000000006
#define MAX 100009
#define INF 999999999
#define mp make_pair
typedef long long ll;
typedef pair< pair<ll,ll>,ll > pairs;

ll x,y;

void func(ll e_s,ll o_s,ll e_c,ll o_c,ll placed,ll k){
    if(e_s>o_s){
        placed+=e_c;
        if(placed>=k){
            x=e_s/2;
            y=x-1;
            return;
        }
        placed+=o_c;
        if(placed>=k){
            x=y=o_s/2;
            return;
        }
    }
    else{
        placed+=o_c;
        if(placed>=k){
            x=y=o_s/2;
            return;
        }
        placed+=e_c;
        if(placed>=k){
            x=e_s/2;
            y=x-1;
            return;
        }
    }
    ll ne_s=0,ne_c=0,no_s=0,no_c=0;
    if(o_s>1){
        if((o_s/2)%2){
            no_s=o_s/2;
            no_c=2*o_c;
        }
        else{
            ne_s=o_s/2;
            ne_c=2*o_c;
        }
    }
    if(e_s==2){
        no_c+=e_c;
    }
    if(e_s>2){
        no_c+=e_c;
        ne_c+=e_c;
        if((e_s/2)%2){
            no_s=e_s/2;
            ne_s=no_s-1;
        }
        else{
            ne_s=e_s/2;
            no_s=ne_s-1;
        }
    }
    func(ne_s,no_s,ne_c,no_c,placed,k);
}
int main(){
    int t,p=1;
    inp(t);
    while(t--){
        ll n,k;
        inp2l(n,k);
        ll e_s=0,o_s=0,e_c=0,o_c=0;
        if(n%2){
            o_s=n;
            o_c=1;
        }
        else{
            e_s=n;
            e_c=1;
        }
        func(e_s,o_s,e_c,o_c,0,k);
        printf("Case #%d: %lld %lld\n",p++,x,y);
    }

    return 0;
}
