#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define ull unsigned long long
#define si(X) scanf("%d", &(X))
#define sll(X) scanf("%lld",&(X))
#define INFL 0x3f3f3f3f3f3f3f3fLL
const int mod = 1e9+7;
ll gcd(ll a,ll b){
	if(b==0)
	return a;return gcd(b,a%b);
}
ll expo(ll base,ll pow){
    ll ans = 1;
    while(pow!=0){
        if(pow&1==1){
            ans = ans*base;
            ans = ans%mod;
        }
        base *= base;base%=mod;
        pow/=2;
    }return ans;
}
ll inv(ll x){
    return expo(x,mod-2);
}

double pi = 3.141592653589793238462643;
double error = 0.0000001;
int dx[8] = {1 , 0 , -1 , 0 , 1 , -1 , -1 , 1};    // last 4 diagonal
int dy[8] = {0 , 1 , 0 , -1 , 1 , 1 , -1 , -1};
/* -------Template ends here-------- */

const int M = 1005;
int arr[M];
int main(){
   // freopen("input.txt", "rt", stdin);
   // freopen("output.txt", "wt", stdout);

    int T;
    si(T);

    for(int alp = 1 ; alp <= T ; alp++){
        int ans = 0;


        ll n , k;
        sll(n);  sll(k);

        ll hi = 0;
        ll nmax = n;
        ll nmin = n;
        if(k == 1){
            nmax = n/2;
            nmin = (n-1)/2;
        }
        else if (k == 2){
            nmax = (n - 1)/2;
            nmin = (n/2);
            nmin /= 2;
        }
        else{
        while(1){
            if((1LL<<(hi + 1)) - 1 == k){
                //special
                hi++;
                cout<<"sp  "<<hi<<endl;
                while(hi){
                    hi--;
                    nmax = nmax/2;
                    nmin = (nmin - 1)/2;
                }
                break;
            }
            else if((1LL<<(hi + 1)) - 1 < k){
                hi++;
            }
            else{
                // non special
               // hi++;
                cout<<"nsp  "<<hi<<endl;
                while(hi){
                    hi--;
                    nmax = nmax/2;
                }
                nmin = (nmax - 1)/2;
                break;
            }
        }
        }

       /* while(1){
            if((1LL<<(hi+1)) - 1 < k) hi++;
            else break;
        }
        //hi++;
        ll nmin = n;
        ll nmax = n;
        cout<<"hi is "<<hi<<endl;
        while(hi){
            hi--;
            nmax /= 2;
            nmin = (nmin - 1)/2;
        }
        ll ma = nmax/2;
        ll mi = (nmin-1)/2;
        */
        printf("Case #%d: " , alp);


        printf("%lld %lld\n" , nmax , nmin);

    }




















}












