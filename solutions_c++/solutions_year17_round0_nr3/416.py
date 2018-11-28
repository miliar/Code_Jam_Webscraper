#include <cstdio>
#include <algorithm>
using namespace std;
typedef long long ll;


int main(){
    int tcn;
    scanf("%d",&tcn);
    for(int tc=1;tc<=tcn;tc++){
        printf("Case #%d: ",tc);
        ll n,k;
        scanf("%lld%lld",&n,&k);
        ll s = n, sc = 1;
        ll l = n+1, lc = 0;
        while(1){
            ll ns = (s-1)/2;
            ll nl = l/2;
            ll nsc = 0;
            ll nlc = 0;
            if(k <= lc){
                printf("%lld %lld\n",l/2, (l-1)/2);
                break;
            }
            k-= lc;
            
            if(l%2){
                nlc += lc * 2;
            }
            else {
                nlc += lc;
                nsc += lc;
            }

            if(k <= sc){
                printf("%lld %lld\n", s/2, (s-1)/2);
                break;
            }
            k -= sc;

            if(s%2){
                nsc += sc * 2;
            }
            else {
                nlc += sc;
                nsc += sc;
            }
            s = ns;
            l = nl;
            sc = nsc;
            lc = nlc;
        }
    }
}
        
